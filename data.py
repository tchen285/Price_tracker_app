import pandas as pd

# Read the CSV file
data = pd.read_csv("/Users/taochen/Desktop/PythonCode/Price_tracker/Price_tracker_app/data.csv")

# Check the column names and remove leading/trailing whitespaces
data.columns = data.columns.str.strip()

# Iterate over rows and print email values
for row in data.itertuples(index=False):
    email_value = row.email
    print(f"Email: {email_value}")
