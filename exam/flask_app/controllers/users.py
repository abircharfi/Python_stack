from flask_app import app
from flask_app.models.user import User
#from flask_app.models.recipe import Recipe
from flask import render_template , request, redirect, session

@app.route('/')
def log_reg():
    if 'user_id' in session:
        return redirect('/dashboard')

    return render_template('index.html')


@app.route('/register', methods = ['POST'])
def register():
    data = request.form
    if User.validate_register(data):
        user=User.create(data)
        print (user)
    return redirect('/')

@app.route('/login' , methods=['POST'])
def login():
    data = request.form
    if User.validate_login(data):
        user = User.get_by_email(data)
        session["user_id"] = user.id
        return redirect("/dashboard")
    return redirect('/')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/dashboard')
def dashboard():
    if not 'user_id' in session:
        return redirect('/')

    recipes = Recipe.get_all()
    user = User.get_by_id({'id': session['user_id']})

    return render_template("dashboard.html", logged_user = user, recipes = recipes)