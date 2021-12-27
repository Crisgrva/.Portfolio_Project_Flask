from flask import Flask, render_template
from apps.github import DataPackage
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", data=DataPackage)


@app.route("/aboutme/")
def aboutme():
    return render_template("about.html", data=DataPackage)


if __name__ == '__main__':
    app.run(debug=True)
