from selenium import webdriver  # $ pip install selenium
import time


options = webdriver.ChromeOptions()
options.add_argument('--headless')
# get chromedriver from
# https://sites.google.com/a/chromium.org/chromedriver/downloads
browser = webdriver.Chrome(chrome_options=options)

browser.get('https://street-beat.ru/cat/man/aksessuary/')
# ... other actions
generated_html = browser.page_source
print(generated_html)
time.sleep(5)
browser.quit()