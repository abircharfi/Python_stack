from flask import Flask, session, render_template, request, redirect
from flask_session import Session

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret key'

@app.route('/', methods=['GET', 'POST'])
def index():
    
    if 'counter' not in session:
        session['counter'] = 0

    if request.method == 'POST' and 'clear' in request.form:
        
        session.clear()
        return redirect('/')
    else:
       
       if request.method == 'POST' and 'btn_add' in request.form:
        
          session['counter'] += 2
    
       else:   
          session['counter'] += 1

    return render_template('index.html', counter=session['counter'])





if __name__ == '__main__':
    app.run(debug=True)