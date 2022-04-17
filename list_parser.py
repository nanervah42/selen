from selenium import webdriver
from selenium_stealth import stealth
from bs4 import BeautifulSoup
import time

def list_parser(url):

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

    driver.get(url)
    time.sleep(5)
    data = driver.page_source
    driver.quit()
    return data


def list_links(data):

    soup = BeautifulSoup(data, 'lxml')
    quotes = soup.find_all('div', class_='product-container__standard')
    for i in quotes:
        lnk = 'https://street-beat.ru' + i.find('a', class_='product-card__figure product-card__product').get('href')
        print(lnk)
