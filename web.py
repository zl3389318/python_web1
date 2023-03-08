from flask import Flask,render_template

app = Flask(__name__)     #固定搭配

#创建了网址 /show/info 和 函数index 的对应关系
@app.route("/show/info")
def index():
    return "中国联通"

@app.route("/string")
def index1():
    return "<span style='color:red;'>朱晧瑜是个大聪明</span>"

@app.route("/")
def index2():
    return render_template("index.html")

@app.route("/user/list")
def user_list():
    return render_template("user_list.html")

@app.route("/user/register")
def register():
    return render_template("user_register.html")
if __name__== '__main__':
    app.run()
