from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    with open('./Possible_Web_Page_Modifications/index.html') as f:
        return(f.read())

@app.route('/BreedInfo.html')
def BreedInfo():
    with open('./Possible_Web_Page_Modifications/index.html') as f:
        return(f.read())    

@app.route('/about.html')
def about():
    with open('./Possible_Web_Page_Modifications/index.html') as f:
        return(f.read())