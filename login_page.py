from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:

    def __init__(self, wd):
        self.wd = wd

    def authorization(self, login_name, login_password):
        user_name = WebDriverWait(self.wd, 5).until(
            EC.element_to_be_clickable((By.ID, 'user-name')))
        password = WebDriverWait(self.wd, 5).until(
            EC.element_to_be_clickable((By.ID, 'password')))
        user_name.send_keys(login_name)
        print('Ввод логина')
        password.send_keys(login_password)
        print('Ввод пароля')
        button_login = WebDriverWait(self.wd, 5).until(
            EC.element_to_be_clickable((By.ID, 'login-button')))
        button_login.click()
        print('Клак по кнопке Логин')
