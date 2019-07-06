from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World"

if __name__ == '__main__':
    app.run(debug=True)

# output
#Serving Flask app "app" (lazy loading)
#* Environment: production
#  WARNING: Do not use the development server in a production environment.
#  Use a production WSGI server instead.
#* Debug mode: on
#* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
# it runs flask on a port, but advises to use a wsgi like gunicorn



# RUNNING VIA GUNICORN
# gunicorn app1:app -b localhost:8000
#[2019-07-06 01:08:00 +0530] [9855] [INFO] Starting gunicorn 19.9.0
#[2019-07-06 01:08:00 +0530] [9855] [INFO] Listening at: http://127.0.0.1:8000 (9855)

# https://medium.com/ymedialabs-innovation/deploy-flask-app-with-nginx-using-gunicorn-and-supervisor-d7a93aa07c18
