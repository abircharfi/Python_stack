from flask_app import app
from flask import render_template, request ,redirect 
from flask_app.config import mysqlconnection
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja


@app.route('/')
def add_new_ninja():
    dojos = Dojo.select_all()  
    return render_template('ninja.html' ,  dojos=dojos)


@app.route('/dojos')
def dojos():
    dojos = Dojo.select_all()
    
    return render_template('dojo.html', dojos=dojos)


@app.route('/dojos/<int:id>')
def ninjas_in_dojo(id):
    data = {'id': id}
    ninjas=Ninja.all_ninjas_in_dojo(data)
    dojos = Dojo.get_one_dojo(data)
    return render_template('ninja_in_dojo.html', ninjas = ninjas, dojos=dojos)

@app.route('/new_dojo' , methods=['POST'])
def new_dojo():
 Dojo.create(request.form)
 return redirect('/dojos')

@app.route('/new_ninja', methods=['POST'])
def add_ninja():

    Ninja.create(request.form)
    return redirect('/dojos')
