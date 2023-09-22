from flask_app import app
from flask import  render_template , redirect , request
from flask_app.models.user import user


@app.route('/')
def all_users():
 users= user.read_all()
 return render_template('read_all.html', users=users)

@app.route('/users/new', methods=['POST'])
def create():
 user.create(request.form)
 return redirect('/')

@app.route('/user')
def form():
 return render_template('create.html')