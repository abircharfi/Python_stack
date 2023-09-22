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

@app.route('/show/<int:id>')
def datails(id):
   data ={'id':id}
   return render_template('show.html' , user=user.get_one(data))

@app.route('/show_edit/<int:id>')
def show(id):
  data = {'id': id}
  return render_template('edit.html', user=user.get_one(data))

@app.route('/user/update', methods=['POST'])
def edit():
 data =request.form
 user.update(data)
 return redirect(f"/show/{data['id']}")

@app.route('/delete/<int:id>')
def user_delete(id):
  data ={'id':id}
  user.delete(data)
  return redirect('/')





  

