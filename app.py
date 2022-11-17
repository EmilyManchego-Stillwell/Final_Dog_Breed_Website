from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def index():
    with open('index.html') as f:
        return(f.read())

@app.route('/BreedInfo.html')
def BreedInfo():
    with open('BreedInfo.html') as f:
        return(f.read())    

@app.route('/about.html')
def about():
    with open('about.html') as f:
        return(f.read())