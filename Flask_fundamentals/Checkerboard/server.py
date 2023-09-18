from flask import Flask , render_template

app = Flask ('__name__')

@app.route('/', defaults= { 'num1':8 , 'num2':8, 'color1':'red', 'color2':'white' })
@app.route('/4', defaults= { 'num1':4 , 'num2':8, 'color1':'red', 'color2':'white' })
@app.route('/<int:num1>/<int:num2>/', defaults= {'color1':'red', 'color2':'white' })
@app.route('/<int:num1>/<int:num2>/<string:color1>/<string:color2>')
def index(num1,num2, color1, color2):
    return render_template('index.html', number1= num1 , number2= num2, color1=color1, color2=color2)

if __name__ == '__main__':
    app.run(debug=True)
