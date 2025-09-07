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

# 擬似的にDB代わりのデータ
users = {
    1: "Natsu",
    2: "Taro",
    3: "Hana"
}

@app.route('/user/<int:user_id>')
def user_page(user_id):
    name = users.get(user_id, "ゲスト") # IDがなければ「ゲスト」
    return render_template("user.html", name=name)

if __name__=="__main__":
    app.run(debug =True, port=5001)