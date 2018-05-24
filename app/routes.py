from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'Nik'}
	post = { 'author': {'username': 'Jake'},'body': 'Infinity War was awesome! 10/10'}
	return render_template('index.html', title='Home', user=user, post=post)



	#{% if text %} is a conditional statement that works like this:
	#{% if title %}
	#<title>{{ title }} - Welcome!</title>
	#{% else %}
	#<title>Home, Welcome!</title>
	#{% endif %}
