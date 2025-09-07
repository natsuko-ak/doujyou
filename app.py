from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'

@app.route('/Test')
def index_test():
    return 'Hello Test'

@app.route('/flask')
def index_flask():
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug =True, port=5001)