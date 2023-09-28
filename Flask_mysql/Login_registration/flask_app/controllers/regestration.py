from flask_app import app
from flask import render_template, redirect, request
from flask_bcrypt import Bcrypt
from flask_app.models.user import User


bcrypt = Bcrypt(app)

@app.route('/')
def index():
 return render_template('index.html')

@app.route('/validation', methods=['POST'])
def verif_from():
   if not  User.validate_user(request.form):

        return redirect('/')
   
   User.create(request.form)
   return redirect( '/display')


@app.route('/display')
def show ():
  user=User.get_one() 
  return render_template('profil.html', user=user)   



@app.route('/validation', methods =['POST'])

def login():
   find=User.find_by_email_and_password(request.form)
   if find is None:
     response="User not found or password incorrect "
     return render_template('index.html' , response=response)
   else:
    return render_template('profil.html' )