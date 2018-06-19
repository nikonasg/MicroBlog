from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'Nik'}
	post = { 'author': {'username': 'Jake'},'body': 'Infinity War was awesome! 10/10'}
	return render_template('index.html', title='Home', user=user, post=post)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for user {}, Remember_me={}'.format(
			form.username.data, form.Remember_me.data))
		return redirect('/index')
	return render_template('login.html', title='Sign In', form=form)



	#{% if text %} is a conditional statement that works like this:
	#{% if title %}
	#<title>{{ title }} - Welcome!</title>
	#{% else %}
	#<title>Home, Welcome!</title>
	#{% endif %}
