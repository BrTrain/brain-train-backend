from flask import Flask

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    return ""


@app.route("/trainers")
def trainers():
    return ""


@app.route("/login")
def login():
    return ""


@app.route("/register")
def register():
    return ""


@app.route("/settings")
def settings():
    return ""


if __name__ == "__main__":
    app.run(debug=True)
