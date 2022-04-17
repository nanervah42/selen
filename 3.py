from fake_useragent import UserAgent
from selenium import webdriver  # Вебморда
from time import sleep  # Для таймаута
from selenium.webdriver.chrome.options import Options  # Опции селениума

ua = UserAgent()
opts = Options()
us_ag = ua.random  # Меняет регулярно юзер-агенты при запросе
url = 'https://street-beat.ru/cat/man/aksessuary/'  # Сайт для проверки измененного юзерагента
print(us_ag)
opts.add_argument(f"user-agent=Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27") #  Десктопный useragent
opts.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(chrome_options=opts)  # Иногда нужно явно указать адрес
driver.get(url)  # Открываем в браузере что бы убедиться в применении юзер-агента
sleep(5)
print(driver.page_source)
driver.close()