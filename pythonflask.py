from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def index():
    return "<h1>Welcome to API Development</h1>"
@app.route("/user/<name>",methods=['GET'])
def getuser(name):
    return"<h1>Hi %s ! welcome to api development</h1>" % name
@app.route("/home")
def home():
    return ("home Page")
if __name__=='__main__':
    app.run(port=5000,debug=True)


