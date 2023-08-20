from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

driver.implicitly_wait(10)
driver.get("https://thirtydollar.website")

driver.maximize_window()

for i in range(547):
    driver.find_element(By.ID,"loadFile").send_keys(f"C:\\Users\\Brian\\BadApple\\30DollarHaircut\\files\\Frame{i}.🗿")
    time.sleep(0.5)

driver.quit()

