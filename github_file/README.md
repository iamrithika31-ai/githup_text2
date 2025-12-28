# Flask Contact Form with WTForms Validation

##  Project Description
This project is a Flask-based contact Form application built using Flask-WTF and WTForms.  
It demonstrates form handling, server-side validation, and Bootstrap-based UI design.



##  Features
- Contact form with Name, Email, Password, and Message fields
- Server-side validation using Flask-WTF
- Custom validation rules for name and password
- Email format validation
- Bootstrap 5 responsive design
- CSRF protection enabled



##  Project Structure

github_file/
│
├── contact_form.py
├── templates/
│ └── contact_form.html
├── contact_form.png
└── README.md




##  Technologies Used
- Python 3.11
- Flask
- Flask-WTF
- WTForms
- Bootstrap 5
- HTML5



##  Installation
```bash
pip install flask flask-wtf email-validator

##  RUN THE APPLICATION 
python github_file/contact_form.py

## Open in browser:
http://127.0.0.1:5000/



## Validation Rules
   Name
     .Required
     .5–15 characters
     .Alphabets only

   Email
     .Required
     .Valid email format

  Password
     .Exactly 4 characters
     .One uppercase letter
     .One lowercase letter
     .One number
     .One special character
 Message
     .Required



### Clickable Image (Markdown)
 [Contact Form](contact_form.png)






