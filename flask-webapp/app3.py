from flask import Flask, request
import json
import boto3
app = Flask(__name__)

dynamodb = boto3.resource('dynamodb', region_name='ap-south-1', aws_access_key_id='*****',aws_secret_access_key= '****')

#dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('userdetails')

@app.route('/',methods=["GET", "POST"])
def index():
    print(request)
    #x = request.form['firstname']
    #y = request.form['lastname']
    #z = request.form['password']
    print('hello dune') # prints to server console # Use logging
    x = request.args['firstname']
    y = request.args['lastname']
    z = request.args['password']
    print((request.data))

    
    response = table.put_item(
        Item={
        'name': x,
        'password': z
    })

    return x+y+z

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80,debug=True)

