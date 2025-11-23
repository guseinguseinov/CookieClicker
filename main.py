from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)


driver.get('https://ozh.github.io/cookieclicker/')
sleep(3)

english_button = driver.find_element(By.XPATH, '//*[@id="langSelect-EN"]')
english_button.click()
sleep(3)

cookie_button = driver.find_element(By.ID, 'bigCookie')

store_section = driver.find_element(By.ID, 'products')

buttons = store_section.find_elements(By.CLASS_NAME, 'product')

while True:
    cookie_count = driver.find_element(By.ID, 'cookies').text.split(' ')[0].replace(',', '')

    cookie_button.click()
    if int(cookie_count) > 1000:
        for button in buttons:
            if 'enabled' in button.get_attribute('class'):

                button.click()
# Göt-baş amma ok


