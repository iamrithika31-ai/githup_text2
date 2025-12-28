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
✅ Clickable Image (Markdown)
[![Contact Form](contact_form.png)](contact_form.png)

[![Contact Form](contact_form.png)](https://github.com/iamrithika31-ai/githup_text2/tree/main/github_file)




C:\Users\LENOVO\Desktop\github>cd cd github_file
The system cannot find the path specified.

C:\Users\LENOVO\Desktop\github>cd github_file

C:\Users\LENOVO\Desktop\github\github_file>notepad README.md

C:\Users\LENOVO\Desktop\github\github_file>git status
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        README.md

nothing added to commit but untracked files present (use "git add" to track)

C:\Users\LENOVO\Desktop\github\github_file>git add github_file/README.md
warning: could not open directory 'github_file/github_file/': No such file or directory
fatal: pathspec 'github_file/README.md' did not match any files

C:\Users\LENOVO\Desktop\github\github_file>git add README.md

C:\Users\LENOVO\Desktop\github\github_file>git commit -m "Add README inside github_file"
[main 48aea43] Add README inside github_file
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 github_file/README.md

C:\Users\LENOVO\Desktop\github\github_file>git push origin main
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 4 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 322 bytes | 161.00 KiB/s, done.
Total 3 (delta 2), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/iamrithika31-ai/githup_text2.git
   9a8ed48..48aea43  main -> main

C:\Users\LENOVO\Desktop\github\github_file>git status
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean

C:\Users\LENOVO\Desktop\github\github_file>git add contact_form.png

C:\Users\LENOVO\Desktop\github\github_file>git add README.md

C:\Users\LENOVO\Desktop\github\github_file>git commit -m "Added screenshot to README"
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean

C:\Users\LENOVO\Desktop\github\github_file>git push
Everything up-to-date

C:\Users\LENOVO\Desktop\github\github_file>git status
On branch main
Your branch is up to date with 'origin/main'.


