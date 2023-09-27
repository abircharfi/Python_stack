from flask_app import app
from flask import render_template, redirect, request
from flask_bcrypt import Bcrypt
from flask_app.models.user import User
bcrypt = Bcrypt()

@app.route('/')
def index():
 return render_template('index.html')

@app.route('/profil', methods =['POST'])
def registration():
   data=User.create(request.form)
   print(data)
   user=User.get_one(data['id'])
   print(user.first_name)

   return render_template('profil.html' , user=user)

@app.route('/validation', methods =['POST'])
def validation():

   find=User.find_by_email_and_password(request.form)
   if find is None:
     response="User not found or password incorrect "
     return render_template('index.html' , response=response)
   else:
    return render_template('profil.html' )