from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

five_mins = time.time() + 300
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://orteil.dashnet.org/experiments/cookie/')

store_items_id = [item.get_attribute('id') for item in driver.find_elements(By.CSS_SELECTOR, value='#store div')]

cookie = driver.find_element(By.ID, value='cookie')
timeout = time.time() + 10
five_min = time.time() + 60*5

while True:
    cookie.click()

    if time.time() > timeout:
        prices = driver.find_elements(By.CSS_SELECTOR, value='#store b')
        item_prices = [int(price.text.split('-')[1].replace(',', ''))for price in prices if price.text != '']
        cookies_upgrades = {item_prices[i]: store_items_id[i] for i in range(len(item_prices))}
        cookie_count = int(driver.find_element(By.ID, value='money').text.replace(',', ''))

        affordable_upgrades = {cost: id for cost, id in cookies_upgrades.items() if cookie_count > cost}
        highest_affordable_item = max(affordable_upgrades)
        to_purchase = affordable_upgrades[highest_affordable_item]

        driver.find_element(By.ID, value=to_purchase).click()

        timeout = time.time()+10

    if time.time() > five_mins:
        cookie_per_s = driver.find_element(By.ID, value='cps').text
        print(cookie_per_s)
        break





