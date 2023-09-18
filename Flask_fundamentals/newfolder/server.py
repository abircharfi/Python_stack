from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response
@app.route('/dojo')          
def hello_dojo():
    return 'Dojo!'

@app.route('/say/<string:name>')          
def hello(name):
    print(name)
    return f'Hi {name} !'

@app.route('/repeat/<int:num>/<string:word>')
def repeat_word(num, word):

    res = ''

    for i in range(0,num):
        res += f"<p>{word}</p>"

    return res

@app.route('/<path:catch_all>')
def handle_catch_all(catch_all):
    return "Sorry! No response. Try again."

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.