from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("")

WebDriverWait(driver, 10).until(EC.presence_of_element_located(By.XPATH, "")).send_keys("")

sleep(3)
driver.quit()
