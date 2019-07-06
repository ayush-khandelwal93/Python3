from flask import Flask, request

app = Flask(__name__)

@app.route('/',methods=["GET", "POST"])
def index():
    x = request.form['firstname']
    y = request.form['lastname']
    z = request.form['password']
    print('hello dune') # prints to server console # Use logging
    return x+y+z

if __name__ == '__main__':
    app.run(debug=True)