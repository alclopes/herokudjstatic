# Deploy Django Application on Heroku - Heroku Project 02 - Dj-Static
* Static file management on Heroku server using dj-static library

Meet this application on [Heroku] (https://herokudjstatic.herokuapp.com/).

## Basic Features of this Application
##### 01. Single Page Design
##### 02. Using Static Image
##### 03. Media Upload Option (media - image POST)
##### 04. DeCouple Library to Protect Private Configuration Variables
##### 05. Using Whitenoise in Production Environment Only
##### 06. Managing Separate Production and Development Settings
##### 07. Managing Separate Production and Development Requirements
##### 08. Using signals to delete media files on server when exceeding three image limit
##### 09. Validation of media file availability on the server and later deletion of the DB reference in the absence of the file.
##### 10. Available Services:
###### Page 01 - My Images
   01. Upload and storage on Image server
   02. Listing and display of the last 3 upload images
   03. Deletion of all images uploaded to server

## Upcoming Developments
#### P3-S3
* Due to the different management of static files by the Heroku server (PaaS), in project P3-S3 I will include the images and media files in the S3 AWS server.
           
## Important Reminders and Cautions When Using Heroku
##### 01. Important to not have rework is to know that the default database used by Heroku is Postgres
* Heroku uses Postgres as the default database, so if you are using db.sqlite3 or another development database on your local machine, you should check for adherence and if necessary recreate your migrations before deploying to the server. .
##### 02. Remember in the free option Heroku does not store long term user uploads.
* Upload source images (application's MEDIA folder) are not maintained by HEROKU (one solution is to use amazon S3 to store them, if necessary see also project 3)
* Heroku Reasons to delete media files: An image server does not require complexity and can even be an apache server, but also to avoid overloading files on the free server and thus reducing its long term performance.
* I am not using an external static file server in this project and heroku deletes the physical files, so I created a condition to delete database records for these deleted files (there is no business rule involved in the records).
##### 03. Important Try Trying to Control In-App Store Content
* Since I will not control the content of uploads by users I have limited viewing of only up to 3 images (media) available on the server,
* I put the images in small percentage size to make their immediate visibility and distance difficult.

## Some tips for running the app
 In addition to the usual installation tips using GIT, you should follow the tips below:
 
#### Value in .env file the following configuration variables:
 
##### 1. To run the application create a .env file created for the decouple package.
            Use as variables base in the .env.var file
            
##### 2. Value Config Vars on Heroku Server the following configuration variables:
            DEBUG = False
            SECRET_KEY = ''
            SETTINGS_MODULE_PATH = testheroku.settings.production
            ALLOWED_HOSTS = .herokuapp.com
            DATABASE_URL = "Automatic" # Will be automatically included and configured by Heroku in the Postgres Resource / addon inclusion
            DISABLE_COLLECTSTATIC = 1
                          
## Current Project Status
##### 1. Deploy Django Application to Heroku
=> Status: Done / Success
##### 2. Static File Management
=> Situation: Incomplete for our need (more details below)
##### 3. Medium File Management
=> Status: Done / Success (more details below)

## Project Status Details

##### 1. Static Files - Status: Awaiting Solution
* Involved: Images and CSS
* If Debug = False gives error 500
* If Debug = True - OK

##### 2. Media File Upload - Situation: OK
* Involved user upload images
* No pending