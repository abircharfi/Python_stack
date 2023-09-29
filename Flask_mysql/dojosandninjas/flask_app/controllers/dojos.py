from flask_app import app
from flask import render_template, request ,redirect 
from flask_app.config import mysqlconnection
from flask_app.models.dojo import Dojo



@app.route('/dojos')
def dojos():
    dojos = Dojo.select_all()
    
    return render_template('dojo.html', dojos=dojos)

@app.route('/new_dojo' , methods=['POST'])
def new_dojo():
 Dojo.create(request.form)
 return redirect('/dojos')