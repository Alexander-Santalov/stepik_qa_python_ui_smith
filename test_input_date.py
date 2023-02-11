import datetime
import os

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service(os.path.abspath(os.path.join(os.path.dirname(__file__), 'chromedriver.exe')))
wd = webdriver.Chrome(options=options, service=g)
base_url = 'https://demoqa.com/date-picker'

current_date = datetime.datetime.now().date()
print(current_date)
result_date = current_date + datetime.timedelta(days=10)
print(result_date)

wd.get(base_url)
wd.set_window_size(1920, 1080)
date_picker = wd.find_element(By.CSS_SELECTOR, '#datePickerMonthYearInput')
date_picker.click()
date_picker.send_keys(Keys.CONTROL + 'a')
print('Clear field calendar')
date_picker.send_keys(result_date.strftime("%m/%d/%Y"))
date_picker.send_keys(Keys.RETURN)
print(f'Input result date: {result_date.strftime("%m/%d/%Y")}')
wd.quit()
