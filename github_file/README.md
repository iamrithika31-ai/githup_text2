# Flask Contact Form with WTForms Validation

## Project Description
This is a Flask-based Contact Form application built using Flask-WTF and WTForms.  
It demonstrates form handling, server-side validation, and a Bootstrap 5 responsive UI.



## Features
- Contact form with Name, Email, Password, and Message fields
- Server-side validation using Flask-WTF
- Custom validation rules for Name and Password
- Email format validation
- Bootstrap 5 responsive design
- CSRF protection enabled


## Project Structure
github_file/
│
├── contact_form.py
├── templates/
│ └── contact_form.html
├── contact_form.png
└── README.md



## Technologies Used
- Python 3.11
- Flask
- Flask-WTF
- WTForms
- Bootstrap 5
- HTML5



## Installation & Run

1. Install required packages

pip install flask flask-wtf email-validator

## Run the application
python github_file/contact_form.py

## Open in browser
http://127.0.0.1:5000/

## Validation Rules

Name
- Required
- 5–15 characters
- Alphabets only

Email
- Required
- Valid email format

Password
- Exactly 4 characters
- One uppercase letter
- One lowercase letter
- One number
- One special character

Message
- Required


## Demo Screenshot

[Contact Form](contact_form.png)
