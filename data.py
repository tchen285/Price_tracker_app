import pandas as pd
import smtplib

MY_EMAIL = "tony.chent6@gmail.com"
MY_PASSWORD = "ijfd bkrh ekji psqe"

# Read the CSV file
data = pd.read_csv("/Users/taochen/Desktop/PythonCode/Price_tracker/Price_tracker_app/data.csv")

# Check the column names and remove leading/trailing whitespaces
data.columns = data.columns.str.strip()

# Iterate over rows and print email values
for row in data.itertuples(index=False):
    url_value = row.url
    target_price_value = row.target_price
    email_value = row.email

    file_path = "email.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[TARGET_PRICE]", str(target_price_value))
        contents = contents.replace("[URL]", url_value)

    # print(f"Url: {url_value}")
    # print(f"target price: {target_price_value}")
    # print(f"Email: {email_value}")

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=email_value,
            msg=f"Subject:From Price Tracker: It's time to place your order!\n\n{contents}"
        )