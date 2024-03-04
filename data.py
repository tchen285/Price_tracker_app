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
    email_value = row.email
    print(f"Email: {email_value}")

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(MY_EMAIL, MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs="tchen285@ucr.edu",
        msg="Subject:From Price Tracker: It's time to place your order!\n\nHi There"
    )