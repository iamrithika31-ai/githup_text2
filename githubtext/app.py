from flask import Flask, render_template, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
app.config['SECRET_KEY'] = "database#123"


engine = create_engine("mysql+pymysql://root:rithi272@localhost:3306/emp_db")
meta = MetaData()

users = Table(
    'users', meta,
    Column('id', Integer, primary_key=True),
    Column('username', String(30), unique=True),
    Column('password', String(30))
)

alerts = Table(
    'alerts', meta,
    Column('id', Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey(users.c.id)),
    Column('message', String(200)),
    Column('time', String(5)),
    Column('shown', Integer, default=0)
)

meta.create_all(engine)
Session = sessionmaker(bind=engine)
db = Session()


class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField("Register")

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")

class AlertForm(FlaskForm):
    message = StringField("Message", validators=[DataRequired()])
    time = StringField("Time (HH:MM)", validators=[DataRequired()])
    submit = SubmitField("Save Alert")


@app.route("/", methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = db.execute(users.select().where((users.c.username==form.username.data) & (users.c.password==form.password.data))).fetchone()
        if user:
            session['uid'] = user.id
            session['name'] = user.username
            return redirect(url_for('dashboard'))
    return render_template("login.html", form=form)

@app.route("/register", methods=["GET","POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        db.execute(users.insert().values(username=form.username.data, password=form.password.data))
        db.commit()
        return redirect(url_for('login'))
    return render_template("register.html", form=form)

@app.route("/dashboard", methods=["GET","POST"])
def dashboard():
    if 'uid' not in session:
        return redirect(url_for('login'))
    form = AlertForm()
    if form.validate_on_submit():
        db.execute(alerts.insert().values(user_id=session['uid'], message=form.message.data, time=form.time.data, shown=0))
        db.commit()
    user_alerts = db.execute(alerts.select().where(alerts.c.user_id==session['uid'])).fetchall()
    return render_template("dashboard.html", form=form, alerts=user_alerts, name=session['name'])

@app.route("/edit/<int:id>", methods=["GET","POST"])
def edit(id):
    alert = db.execute(alerts.select().where(alerts.c.id==id)).fetchone()
    form = AlertForm(message=alert.message, time=alert.time)
    if form.validate_on_submit():
        db.execute(alerts.update().where(alerts.c.id==id).values(message=form.message.data, time=form.time.data, shown=0))
        db.commit()
        return redirect(url_for('dashboard'))
    return render_template("edit.html", form=form)

@app.route("/delete/<int:id>")
def delete(id):
    db.execute(alerts.delete().where(alerts.c.id==id))
    db.commit()
    return redirect(url_for('dashboard'))

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__=="__main__":
    app.run(debug=True)