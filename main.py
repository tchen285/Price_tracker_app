from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def select_url():
    return render_template("index.html")

@app.route("/left-sidebar.html")
def left_sidebar():
    return render_template("left-sidebar.html")

@app.route("/right-sidebar.html")
def right_sidebar():
    return render_template("right-sidebar.html")

@app.route("/no-sidebar.html")
def no_sidebar():
    return render_template("no-sidebar.html")

if __name__ == "__main__":
    app.run(debug=True)
