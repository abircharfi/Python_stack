from flask_app import app
from flask import render_template, redirect, request , session

from flask_app.models.user import User




@app.route('/')
def index():
 return render_template('index.html')

@app.route('/validation', methods=['POST'])
def verif_form():
   if not  User.validate_user(request.form):

        return redirect('/')
   
   User.create(request.form)
   return redirect( '/display')


@app.route('/display')
def show ():
  user=User.get_one() 
  return render_template('profil.html', user=user) 
  



@app.route('/login', methods =['POST'])
def login():
    data = request.form
    if User.validate_login(data):
        user =User.get_by_email(data)
        session['user_id'] = user.id
        return render_template('profil.html', user=user)
    return redirect('/')

@app.route('/logout')
def logout():
    session.clear()  
    return redirect('/')
