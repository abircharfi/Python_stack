from flask import Flask , render_template ,request , redirect
from flask_app.models.dojo import Dojo


app = Flask(__name__)

app.secret_key ='sdqfcsdgrfvseg'

@app.route('/')

def index():

 return render_template('index.html')

@app.route('/process', methods=['POST'])

def validation():
 data=request.form
 if not Dojo.validate_dojo(data):
  return redirect('/')
  
 new_dojo=Dojo.create(data)
 dojo=Dojo.get_one_dojo(new_dojo) 
 return render_template('info.html', dojo=dojo) 

if __name__ == '__main__':
    app.run(debug=True)