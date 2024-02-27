from bestbuy import BestBuyScraper
from flask import Flask, render_template, session, request, redirect, url_for
import csv

app = Flask(__name__)
app.secret_key = '123890'  # Set a secret key for session

bestbuy_scraper = BestBuyScraper()
bestbuy_price = bestbuy_scraper.get_bestbuy_price("https://www.bestbuy.com/site/alienware-aw3423dwf-34-quantum-dot-oled-curved-ultrawide-gaming-monitor-165hz-amd-freesync-premium-pro-vesa-hdmiusb-dark-side-of-the-moon/6536990.p?skuId=6536990")


@app.route("/")
def select_url():
    session['bestbuy_price'] = bestbuy_price
    return render_template("index.html", price=bestbuy_price)


@app.route('/left-sidebar.html', methods=['GET', 'POST'])
def left_sidebar():
    if request.method == 'POST':
        # Retrieve form data
        url = request.form.get('urlInput')
        target_price = request.form.get('targetPrice')
        email = request.form.get('email')

        # Process the form data (e.g., write to CSV file)
        with open('data.csv', 'a', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow([url, target_price, email])

        return redirect(url_for('no_sidebar'))

    # Render the template with the form
    return render_template('left-sidebar.html')


@app.route("/right-sidebar.html")
def right_sidebar():
    return render_template("right-sidebar.html")


@app.route('/no-sidebar.html', methods=['GET', 'POST'])
def no_sidebar():
    return render_template("no-sidebar.html")


if __name__ == "__main__":
    app.run(debug=True)
