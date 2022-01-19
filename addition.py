from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("start.html")

@app.route('/add/<msg>')
def add(msg):
    return render_template("result.html",message = msg)

@app.route('/procForm', methods=['POST'])
def processPost():
    x = request.form["x"]
    y = request.form["y"]
    return render_template("result.html", message = int(x)+int(y) )

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug = True)
