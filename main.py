from flask import Flask

app = Flask(__name__)


@app.route("/")
def select_url():
    return """
        <html>
            <body>
                <button onclick="window.location.href='https://www.bestbuy.com'">Best Buy</button>
            </body>
        </html>
        """


if __name__ == "__main__":
    app.run(debug=True)