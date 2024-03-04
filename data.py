import pandas as pd
import smtplib
from bestbuy import BestBuyScraper
from steam import SteamScraper
from amazon import AmazonScraper

MY_EMAIL = "tony.chent6@gmail.com"
MY_PASSWORD = "ijfd bkrh ekji psqe"

# Read the CSV file
data = pd.read_csv("/Users/taochen/Desktop/PythonCode/Price_tracker/Price_tracker_app/data.csv")

# Check the column names and remove leading/trailing whitespaces
data.columns = data.columns.str.strip()

file_path = "email.txt"

def send_email(url, target_price, email, current_price, product_name):
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[TARGET_PRICE]", str(target_price_value))
        contents = contents.replace("[URL]", url_value)

# Iterate over rows and print email values
for row in data.itertuples(index=False):
    url_value = row.url
    target_price_value = row.target_price
    email_value = row.email

    # Go to the websites to find the current price
    if "bestbuy" in url_value:
        bestbuy_scraper = BestBuyScraper()
        price_bestbuy, product_name_bestbuy = bestbuy_scraper.get_bestbuy_price(url_value)

        # print(f"Price: {price_bestbuy}")
        # print(f"Product Name: {product_name_bestbuy}")

    if "steampowered" in url_value:
        steam_scraper = SteamScraper()
        price_steam, product_name_steam = steam_scraper.get_steam_price(url_value)
        print(f"Steam Price: {price_steam}")
        print(f"Steam Product Name: {product_name_steam}")

    if "amazon" in url_value:
        amazon_scraper = AmazonScraper()
        price_amazon, product_name_amazon = amazon_scraper.get_amazon_price(url_value)
        print(f"Amazon Price: {price_amazon}")
        print(f"Amazon Product Name: {product_name_amazon}")

    # file_path = "email.txt"
    # with open(file_path) as letter_file:
    #     contents = letter_file.read()
    #     contents = contents.replace("[TARGET_PRICE]", str(target_price_value))
    #     contents = contents.replace("[URL]", url_value)
    #
    #
    # with smtplib.SMTP("smtp.gmail.com") as connection:
    #     connection.starttls()
    #     connection.login(MY_EMAIL, MY_PASSWORD)
    #     connection.sendmail(
    #         from_addr=MY_EMAIL,
    #         to_addrs=email_value,
    #         msg=f"Subject:From Price Tracker: It's time to place your order!\n\n{contents}"
    #     )