import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}


class SteamScraper:
    def get_steam_price(self, product_url):
        try:
            response = requests.get(product_url, headers=headers, timeout=10)
            response.raise_for_status()  # Check for HTTP errors
            content = response.content
            # print(content)
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")

        soup = BeautifulSoup(content, 'lxml')

        product_name = soup.select_one('.apphub_AppName')

        price_element = soup.select_one('.game_purchase_price')


        product_name_text = product_name.stripped_strings.__next__()

        product_price_text = price_element.stripped_strings.__next__()
        price = product_price_text.replace(',', '')
        current_price = float(price.replace('$', ''))

        return product_name_text, current_price
