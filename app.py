from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Test Instance Deployment</h1><br><br><p>To be tested for GET response prior to deploying to prodcution.</p><br><br><h3>Good luck Jedi scum!</h3>'
