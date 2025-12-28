from flask import Flask,redirect,render_template,url_for,request
from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,EmailField,SubmitField,PasswordField,validators,ValidationError
import re
app=Flask(__name__)
app.config['SECRET_KEY']='FGYUJ6'

def only_alphabets(form,field):
     if not field.data.isalpha():
        raise ValidationError('name should contain only alphabets')
def password_rules(form,field):
    pwd=field.data
    if len(pwd)!=4:
        raise ValidationError('password must be exactly 4 characters long')
    if not re.search(f"[A-Z]",pwd):
        raise ValidationError('password must contain at least one uppercase letter')
    if not re.search(r"[a-z]",pwd):
        raise ValidationError("password must contain at least one lowercase letter")
    if not re.search(r"[0-9]",pwd):
        raise ValidationError('password must contain at least one number')
    if not re.search(r'[\w_]',pwd):
        raise ValidationError('password must contain at least one special character')
class contactForm(FlaskForm):
    name=StringField('name',[validators.DataRequired(message='please enter your name'),validators.Length(min=5,max=15,message='name must be 5 to 15 characters'),only_alphabets])
    email=EmailField('Email',[validators.DataRequired(message='please enter your email'),validators.Email(message='invalid email format')])     
    password=PasswordField('password',[validators.DataRequired(message='please enter a password'),password_rules])
    message=TextAreaField('message',[validators.DataRequired(message='please enter your message')])
    submit=SubmitField('submit')
@app.route('/',methods=['GET','POST'])
def contact():
    form=contactForm()
    if form.validate_on_submit():
        return 'form submitted successully'
    return render_template('success.html',form=form)
if (__name__=='__main__'):
    app.run(debug=True)

