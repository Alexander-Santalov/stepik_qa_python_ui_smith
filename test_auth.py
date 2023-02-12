import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from login_page import LoginPage


class Test:

    def test_auth(self):
        users_list = ['standard_user', 'locked_out_user', 'problem_user', 'performance_glitch_user']
        for name in users_list:
            options = webdriver.ChromeOptions()
            options.add_experimental_option("detach", True)
            g = Service(os.path.abspath(os.path.join(os.path.dirname(__file__), 'chromedriver.exe')))
            wd = webdriver.Chrome(options=options, service=g)
            base_url = 'https://www.saucedemo.com/'
            wd.get(base_url)
            wd.set_window_size(1920, 1080)

            login = LoginPage(wd)
            login.authorization(name, 'secret_sauce')
            try:
                good_auth = WebDriverWait(wd, 6).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, 'span.title'))).text
                assert good_auth == 'PRODUCTS'
                print(f'Успешная авторизация пользователя {name}')
            except TimeoutException:
                auth_window = WebDriverWait(wd, 5).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, 'h3[data-test="error"]'))).text
                assert 'Epic sadface: Sorry, this user has been locked out.' == auth_window
                print(f"Пользователь {name} заблокирован")
            wd.quit()


Test().test_auth()



