from selenium import webdriver
from selenium_stealth import stealth
from bs4 import BeautifulSoup
import time

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options, executable_path=r".\chromedriver.exe")

stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

url = 'https://street-beat.ru/cat/man/aksessuary/?page=14'
driver.get(url)
time.sleep(5)
forsoup = driver.page_source
driver.quit()


soup = BeautifulSoup(forsoup, 'lxml')
quotes = soup.find_all('div', class_='product-container__standard')
for i in quotes:
        lnk = 'https://street-beat.ru' + i.find('a', class_='product-card__figure product-card__product').get('href')
        print(lnk)

a = soup.find('button', class_='app-button pagination-simple__btn pagination-simple__btn--next app-button--theme-transparent app-button--without-shadow')
if a:
        print('YES')
else:
        print('NOO')