import requests
from bs4 import BeautifulSoup

# url = 'https://www.bestbuy.com/site/microsoft-xbox-series-s-1tb-all-digital-console-disc-free-gaming-black/6547877.p?skuId=6547877'
# url = 'https://www.bestbuy.com/site/samsung-galaxy-watch6-classic-stainless-steel-smartwatch-47mm-bt-black/6546701.p?skuId=6546701'
url = 'https://store.steampowered.com/app/582010/Monster_Hunter_World/'
# url = 'https://www.amazon.com/Premier-Protein-Shake-Chocolate-11-5/dp/B07MJL8NXR/?_encoding=UTF8&pd_rd_w=a7JbV&content-id=amzn1.sym.64be5821-f651-4b0b-8dd3-4f9b884f10e5&pf_rd_p=64be5821-f651-4b0b-8dd3-4f9b884f10e5&pf_rd_r=STQC9KAGYSFBEMAK7ASH&pd_rd_wg=5Z1ow&pd_rd_r=99e8e0df-7b79-42cf-b9c9-50cb22b785fe&ref_=pd_gw_crs_zg_bs_16310101'

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

product_name = soup.select_one('.apphub_AppName')

if product_name:
    product_name_text = product_name.stripped_strings.__next__()
    print(f"The product name is: {product_name_text}")
else:
    print("Product element not found.")