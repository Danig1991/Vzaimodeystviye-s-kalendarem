import time
from datetime import datetime, timedelta

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# базовый url
base_url = 'https://demoqa.com/date-picker'

# добавить опции/оставить браузер открытым
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# автоматическая загрузка драйвера
service = ChromeService(ChromeDriverManager().install())

# открытие браузера с параметрами
driver_chrome = webdriver.Chrome(
    options=options,
    service=service
)

# переход по url в браузере/развернуть на весь экран
driver_chrome.get(base_url)
driver_chrome.maximize_window()

# сегодняшнее число +10 дней
date_now_plus_10_day = (
        datetime.now() + timedelta(days=10)
).strftime("%m/%d/%Y")
print(f"Дата для установки - {date_now_plus_10_day}")

# найти поле для ввода даты и очистить содержимое
date_input = driver_chrome.find_element(By.ID, "datePickerMonthYearInput")
date_input.send_keys(Keys.CONTROL + "a")
date_input.send_keys(Keys.DELETE)
print("Содержимое строки удалено.")

time.sleep(1)

# ввод даты позже на 10 дней
date_input.send_keys(date_now_plus_10_day)
date_input.send_keys(Keys.ENTER)
print("Дата установлена.")