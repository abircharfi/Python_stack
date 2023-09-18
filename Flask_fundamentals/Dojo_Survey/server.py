from flask import Flask , render_template ,request , session

app = Flask(__name__)

app.secret_key ='sdqfcsdgrfvseg'

@app.route('/')

def index():
    return render_template('index.html')
 

@app.route('/result', methods=['POST'])

def result():
 name = request.form['name']
 location= request.form['location']
 language = request.form['language']
 comments= request.form['comments']
 return render_template('info.html', name=name, location=location, language=language, comments=comments)

if __name__ == '__main__':
    app.run(debug=True)