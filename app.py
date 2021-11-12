from flask import Flask,render_template

app = Flask(__name__)

all_posts=[
    {
        'name':'Allen','id':1
    },
    {
        'name':'Maneesh','id':2
    }
]

@app.route('/post')
def home():
    return render_template('index.html',data=all_posts)

@app.route('/home/<string:name>')
def view(name):
    return "hello " +name

@app.route('/onlyget',methods=['GET'])
def getreq():
    return "bye"



if __name__=="__main__":
    app.run(debug=True)