from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class AmazonScraper:
    def get_amazon_price(self, product_url):
        # Configure Chrome options
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

        # Create WebDriver instance with configured options
        driver = webdriver.Chrome(options=chrome_options)

        try:
            # Visit the website
            driver.get(product_url)

            # Find the price and product name elements using their class names
            price_element = driver.find_element(By.CLASS_NAME, "a-price-whole")
            product_name_element = driver.find_element(By.CLASS_NAME, "a-size-large.product-title-word-break")

            # Get the text content of the elements
            price_str = price_element.text.replace(',', '')
            product_name_str = product_name_element.text

            # Convert the price string to float
            price_float = float(price_str.replace('$', ''))

            return price_float, product_name_str

        finally:
            # Close the browser
            driver.quit()