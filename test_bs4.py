import requests
from bs4 import BeautifulSoup

url = 'https://www.bestbuy.com/site/microsoft-xbox-series-s-1tb-all-digital-console-disc-free-gaming-black/6547877.p?skuId=6547877'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

try:
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()  # Check for HTTP errors
    content = response.content
    # print(content)
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")

soup = BeautifulSoup(content, 'lxml')

name_list = soup.select('.priceView-hero-price')

print(name_list)


