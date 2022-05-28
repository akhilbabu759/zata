from flask import Flask,render_template,request,redirect,session
app = Flask(__name__)

@app.route("/")
def hello():


    return render_template("/hai.html")


if __name__ == "__main__":
    app.run()