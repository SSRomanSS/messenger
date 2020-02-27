# *REST DJANGO API MESSENGER* (test project)
## Simple messenger on REST API
<br />

## Installation
### (PostgreSQL is used in the project. You need to install it first)
<br/>

Make directory for the project:
```
$ mkdir <project_dir>
```
Run virtual environment into project directory:
```
$ python3 -m venv <env_dir> and activate it source bin/activate
```
Clone git repository into environment directory :
```
$ git clone https://github.com/SSRomanSS/messenger.git
```
Run installation in messenger directory:
```
$ pip install -r requirements.txt
```
```
$ python manage.py migrate
```
```
$ python manage.py createsuperuser (Remember superuser login and password!)
```
```
$ python manage.py runserver
```
After that you can check the result on: http://localhost:8000

Don't forget to use superuser credentials to view API on browser.

## Links
GET all messages
```
http://localhost:8000/api/messages/list/
```
GET messages with pagination by 10 messages per request
```
http://localhost:8000/api/messages/list/page_num
```
> page_num = 0 return messages 1-10, etc

GET method for getting single message by unique identifier
```
http://localhost:8000/api/messages/single/unique_message_identifier
```
> unique_message_identifier = Primary Key in a database

POST method for creating a new message
```
http://localhost:8000/api/messages/post_message/
