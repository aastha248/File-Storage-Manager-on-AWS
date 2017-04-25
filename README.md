# File Storage Manager on AWS

Name : Aastha Gupta <br>
Email : aastha.gupta@mavs.uta.edu <br>
Affiliation : University of Texas at Arlington <br>
Website URL :  <br>

## Project Description : <br>

A utility to provide "Storage as a Service" which will securely store and retrieve files to a cloud service provider. The application offers the following service to a user : <br>

1. Configure EC2 as the webserver that host the python flask application. <br>
    Follow the following link to configure EC2 instance : "http://www.datasciencebytes.com/bytes/2015/02/24/running-a-flask-app-on-aws-ec2/" <br>
2. Authenticate user by using the file (contains authorized users to use the service) stored in S3. <br>
3. After authorizing the user, user should be able to upload, download and delete the images
   to and from S3. <br>

#### Run the app on AWS apache server using 'sudo apachectl restart' on Ubuntu Commandline Terminal. <br>

[Install Python]: https://www.python.org/downloads/