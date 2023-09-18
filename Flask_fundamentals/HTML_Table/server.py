from flask import Flask, render_template 
from flask_session import Session

app = Flask (__name__)
app.config['SECRET_KEY'] = 'secret key'

@app.route('/')
def index():
 users = [
   {'first_name' : 'Michael', 'last_name' : 'Choi'},
   {'first_name' : 'John', 'last_name' : 'Supsupin'},
   {'first_name' : 'Mark', 'last_name' : 'Guillen'},
   {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
 return render_template('index.html', users_info = users )

if __name__ == '__main__':
 app.run(debug=True)