import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service(os.path.abspath(os.path.join(os.path.dirname(__file__), 'chromedriver.exe')))
wd = webdriver.Chrome(options=options, service=g)
base_url = 'https://www.saucedemo.com/'
login_user = 'standard_user'
pass_user = 'secret_sauce'

wd.get(base_url)
wd.set_window_size(1920, 1080)

user_name = wd.find_element(By.ID, 'user-name')
user_name.send_keys(login_user)
print('Input login')
password = wd.find_element(By.ID, 'password')
password.send_keys(pass_user)
print('Input password')
btn_login = wd.find_element(By.ID, 'login-button')
btn_login.click()
print('Click login btn')

'''INFO Product #1'''
product_1 = wd.find_element(By.ID, 'item_4_title_link')
value_product_1 = product_1.text
print(value_product_1)

price_product_1 = wd.find_element(By.XPATH, '//a[@id="item_4_title_link"]/../..//div[@class="inventory_item_price"]')
value_price_product_1 = price_product_1.text
print(value_price_product_1)

select_product_1 = wd.find_element(By.ID, 'add-to-cart-sauce-labs-backpack')
select_product_1.click()
print('Select product 1')

'''INFO Product #2'''
product_2 = wd.find_element(By.ID, 'item_0_title_link')
value_product_2 = product_2.text
print(value_product_2)

price_product_2 = wd.find_element(By.XPATH, '//a[@id="item_0_title_link"]/../..//div[@class="inventory_item_price"]')
value_price_product_2 = price_product_2.text
print(value_price_product_2)

select_product_2 = wd.find_element(By.ID, 'add-to-cart-sauce-labs-bike-light')
select_product_2.click()
print('Select product 2')

cart = wd.find_element(By.CSS_SELECTOR, 'span.shopping_cart_badge')
cart.click()

'''INFO Cart Product 1'''
cart_product_1 = wd.find_element(By.ID, 'item_4_title_link')
value_cart_product_1 = cart_product_1.text
print(value_cart_product_1)
assert value_product_1 == value_cart_product_1

price_cart_product_1 = wd.find_element(By.CSS_SELECTOR, '#item_4_title_link ~div .inventory_item_price')
value_cart_price_product_1 = price_cart_product_1.text
print(value_cart_price_product_1)
assert value_price_product_1 == value_cart_price_product_1

'''INFO Cart Product 2'''
cart_product_2 = wd.find_element(By.ID, 'item_0_title_link')
value_cart_product_2 = cart_product_2.text
print(value_cart_product_2)
assert value_product_1 == value_cart_product_1
print('INFO Cart Product 1 Good')

price_cart_product_2 = wd.find_element(By.CSS_SELECTOR, '#item_0_title_link ~div .inventory_item_price')
value_cart_price_product_2 = price_cart_product_2.text
print(value_cart_price_product_2)
assert value_price_product_1 == value_cart_price_product_1
print('INFO Cart Product 2 Good')

checkout = wd.find_element(By.CSS_SELECTOR, '#checkout')
checkout.click()
print('Click checkout')

'''Selext User Info'''
first_name = wd.find_element(By.CSS_SELECTOR, '#first-name')
first_name.send_keys('Aleksander')
print('Input first name')

last_name = wd.find_element(By.CSS_SELECTOR, '#last-name')
last_name.send_keys('Santalov')
print('Input last name')

zip = wd.find_element(By.CSS_SELECTOR, '#postal-code')
zip.send_keys('02342')
print('Input zip')

button_continue = wd.find_element(By.CSS_SELECTOR, '#continue')
button_continue.click()
print('Click continue')

'''Info finish product 1'''
finish_product_1 = wd.find_element(By.CSS_SELECTOR, '#item_4_title_link')
value_finish_product_1 = finish_product_1.text
print(value_finish_product_1)
assert value_product_1 == value_finish_product_1
print('INFO finish product 1 Good')

price_finish_product_1 = wd.find_element(By.CSS_SELECTOR, '#item_4_title_link ~div .inventory_item_price')
value_finish_price_product_1 = price_finish_product_1.text
print(value_finish_price_product_1)
assert value_price_product_1 == value_finish_price_product_1
print('INFO finish price product 1 Good')

'''Info finish product 2'''
finish_product_2 = wd.find_element(By.CSS_SELECTOR, '#item_0_title_link')
value_finish_product_2 = finish_product_2.text
print(value_finish_product_2)
assert value_product_2 == value_finish_product_2
print('INFO finish product 2 Good')

price_finish_product_2 = wd.find_element(By.CSS_SELECTOR, '#item_0_title_link ~div .inventory_item_price')
value_finish_price_product_2 = price_finish_product_2.text
print(value_finish_price_product_2)
assert value_price_product_2 == value_finish_price_product_2
print('INFO finish price product 2 Good')

summary_price = wd.find_element(By.CSS_SELECTOR, 'div.summary_subtotal_label')
value_summary_price = summary_price.text
print(value_summary_price)
item_total = 'Item total: $' + str(float(value_price_product_1.replace('$', '')) +
                                   float(value_price_product_2.replace('$', '')))
print(item_total)
assert value_summary_price == item_total
print('Total')
wd.quit()