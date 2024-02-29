from selenium import webdriver
from selenium.webdriver.common.by import By


class SteamScraper:
    def get_steam_price(self, product_url):
        # Keep Chrome browser open after the program finishes
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)

        driver = webdriver.Chrome(options=chrome_options)

        # 3. Visit the website
        # driver.get("https://store.steampowered.com/app/1971650/OCTOPATH_TRAVELER_II/")
        driver.get(product_url)

        # 4. Find the price element using its class name
        price_element = driver.find_element(By.CLASS_NAME, "game_purchase_price.price")
        product_name = driver.find_element(By.CLASS_NAME, "apphub_AppName")
        product_name_str = product_name.text
        # print(product_name_str)
        # 5. Find the inner span with the actual price
        # price_span = price_element.find_element(By.CSS_SELECTOR, 'span[aria-hidden="true"]')

        # 6. Get the text content of the span
        price_str = price_element.text

        # Remove commas from the price string
        price_str = price_str.replace(',', '')

        price_float = float(price_str.replace('$', ''))
        # print(price_float)

        # 8. Close the browser
        driver.quit()

        return price_float, product_name_str