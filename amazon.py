from selenium import webdriver
from selenium.webdriver.common.by import By

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Keep Chrome browser open after the program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

# 3. Visit the website
driver.get("https://www.amazon.com/TAGRY-Bluetooth-Headphones-Earphones-Waterproof/dp/B09LD2D1TV/?_encoding=UTF8&ref_=dlx_gate_sd_dcl_tlt_b1749c31_dt_pd_gw_unk&pd_rd_w=2Vh8T&content-id=amzn1.sym.26a365d6-3002-449e-bfff-1848c98a3efd&pf_rd_p=26a365d6-3002-449e-bfff-1848c98a3efd&pf_rd_r=317PNYP89JQBHN81HK5H&pd_rd_wg=Y3Jh6&pd_rd_r=15290888-f7c7-483f-8800-b36d5dc6cb32&th=1")
# driver.get(product_url)

# 4. Find the price element using its class name
price_element = driver.find_element(By.CLASS_NAME, "a-price-whole")
product_name = driver.find_element(By.CLASS_NAME, "a-size-large.product-title-word-break")
product_name_str = product_name.text
print(product_name_str)
# 5. Find the inner span with the actual price
# price_span = price_element.find_element(By.CSS_SELECTOR, 'span[aria-hidden="true"]')

# 6. Get the text content of the span
price_str = price_element.text
#
# # Remove commas from the price string
price_str = price_str.replace(',', '')
#
print(price_str)
# price_float = float(price_str.replace('$', ''))
# print(price_float)

# 8. Close the browser
driver.quit()