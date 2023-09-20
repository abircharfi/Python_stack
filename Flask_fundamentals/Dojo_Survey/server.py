from flask import Flask , render_template ,request , session , redirect

app = Flask(__name__)

app.secret_key ='sdqfcsdgrfvseg'

@app.route('/')

def index():

 return render_template('index.html')

@app.route('/process', methods=['POST'])

def create():
   session['name'] = request.form['name']
   session['location']= request.form['location']
   session['language'] = request.form['language']
   session['comments']= request.form['comments']
   return redirect('result')
@app.route('/result')
def show():
   return render_template('info.html')

if __name__ == '__main__':
    app.run(debug=True)