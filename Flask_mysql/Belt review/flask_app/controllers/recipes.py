from flask_app import app
from flask_app.models.recipe import Recipe
from flask_app.models.user import User


from flask import request, render_template, session, redirect

@app.route('/add_recipe')
def add_recipe():
    user = User.get_by_id({'id': session['user_id']})
    return render_template("add_recipe.html", logged_user = user)


@app.route('/create/recipe' , methods=['POST'])
def create():
    data = request.form
    if Recipe.validate_recipe(data):
     Recipe.create(data)
     return redirect('/dashboard')
    return redirect('/add_recipe')

@app.route('/recipe/<int:id>/edit')
def edit_recipe(id):
    recipe = Recipe.get_by_id({'id': id})
    if recipe.user.id != session['user_id']:
        return redirect('/dashboard')
    return render_template('edit_recipe.html', recipe = recipe)


@app.route('/recipe/update', methods=['POST'])
def update():
    data = request.form
    if int(request.form['user_id']) == int(session['user_id']):
        if Recipe.validate_recipe(data):
         Recipe.update(request.form)
         return redirect('/dashboard')
    return redirect(f'/recipe/{int(session["user_id"])}/edit')

@app.route('/recipe/<int:id>/delete')
def delete(id):
    recipe = Recipe.get_by_id({'id': id})
    
    if recipe.user.id == session['user_id']:
        
        Recipe.delete({'id': id})
    return redirect('/dashboard')

@app.route('/recipe/<int:id>')
def show_recipe(id):
    recipe = Recipe.get_by_id({'id': id})
    user = User.get_by_id({'id': session['user_id']})
    return render_template("show_recipe.html", recipe = recipe , logged_user = user)