## The project is Python Flask REST API for Parent Child Relationship

### Can be used for following applications
	File System - where objects are files, folders and parents are folders
	E-commerce application - where objects are items and parents are stores / categories
	Active Directory - where objects are users and parents are groups / roles

### Pre-requisites:
	Python 3
	Flask
	JWT
	SQLAlchemy
	Flask-Restful

### Installation
	pip install Flask

### How to use?
	Run using "python app.py"

### Has following endpoints
	GET - /objects
	GET - /object/<name>
	POST - /object/<name>
	PUT - /object/<name>
	DELETE - /object/<name>
	POST - /auth
	POST - /register
	GET - /parents
	GET - /parent/<name>
	POST - /parent/<name>
	DELETE - /parent/<name>

### Testing the API 
#### Use the attached Postman Collection
	Flask API.postman_collection.json