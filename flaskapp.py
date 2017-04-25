import os
import boto3
from flask import Flask, request, make_response

app = Flask(__name__)

s3 = boto3.resource('s3',aws_access_key_id='AKIAJKUEEFY3SHCWIXDQ', aws_secret_access_key='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')

@app.route('/uploads', methods=['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		curr_file = request.files['file_upload']
	else:
		return 'No file selected'
	file_name = curr_file.filename
	file_contents = curr_file.read()
	s3.Bucket('aastha248-bucket').put_object(Key = file_name, Body = file_contents)
	return 'File Uploaded'

@app.route('/download', methods=['GET', 'POST'])
def download_file():
	file_name = request.args.get('file_name', '')
	if len(file_name) > 1 :
		dir = os.path.abspath(os.path.join(os.path.split(__file__)[0], ''))
		for bucket in s3.buckets.all():
			for object in bucket.objects.all():
				if object.key == file_name :
					file_contents = object.get()["Body"].read()
		response = make_response(file_contents)
        	response.headers["Content-Disposition"] = "attachment; filename=" + file_name
        	return response
  	else:
    		return 'No File Selected' 

@app.route('/list', methods=['GET', 'POST'])
def list_file():
	list = 'Files in the database are : <br>'
	for bucket in s3.buckets.all():
		for object in bucket.objects.all():
			list = list + '<li> ' + str(object.key) + '</li>'
  	return list

@app.route('/delete', methods=['GET', 'POST'])
def delete_file():
	file_name = request.args.get('file_name', '')
	if len(file_name) > 1:
		for bucket in s3.buckets.all():
			for object in bucket.objects.all():
				if file_name == object.key :
					object.delete()
   					return 'File Deleted'
    		return 'File not found'
	else:
		return 'No File Selected'

@app.route('/login', methods = ['GET', 'POST'])
def login_user():
	user_name = request.args.get('user_name','')
	password = request.args.get('password', '')
	for bucket in s3.buckets.all():
		for object in bucket.objects.all():
			if object.key == 'credentials.txt' :
				file_contents = object.get()['Body'].read()
				credentials = file_contents.split(',')
				for cred in credentials :
					if (" " + user_name + " " in cred ) & (" " + password + " " in cred) :
						return app.send_static_file('index.html')
				return 'User not authenticated'

@app.route('/')
def first_page():
	return app.send_static_file('login.html')

if __name__ == '__main__':
  app.run()
