from bestbuy import BestBuyScraper
from flask import Flask, render_template


app = Flask(__name__)

bestbuy_scraper = BestBuyScraper()
bestbuy_price = bestbuy_scraper.get_bestbuy_price("https://www.bestbuy.com/site/microsoft-xbox-series-s-1tb-all-digital-console-disc-free-gaming-black/6547877.p?skuId=6547877")
print(bestbuy_price)
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
