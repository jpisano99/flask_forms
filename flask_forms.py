from flask import Flask
from flask import render_template, flash, redirect, url_for, request, session
from flask_bootstrap import Bootstrap
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from forms import LoginForm
from my_secrets import passwords

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/success')
def success():
    print ("success")
    return render_template('success.html')

@app.route('/login',methods=['GET', 'POST'])
def login():
    form = LoginForm()
    print("Form Data:  ",form.data)
    print("URL for:  ",url_for('success'))
    print (app.config)

    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('success'))
    return render_template('login.html', title='Sign In', form=form)


if __name__ == '__main__':
    # Needed for csrf token in html page form.hidden_tag()
    app.config ['SECRET_KEY'] = passwords['CSRF_SECRET_KEY']
    app.run()
