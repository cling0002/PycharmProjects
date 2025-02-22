# WebDriverWait(driver,10).until((EC.presence_of_element_located(By.CSS_SELECTOR,)))
'''
        css
    id选择器   #id
    class选择器       .class
    元素师选择器      element
    属性选择器       [attribute=value]      element[attribute=value]

层级选择器
    element1>element2
    element1 element2

衍生
    input[type^=‘p’]        type属性以p开头的元素
    input[type$=‘p’]        type属性以p结束的元素
    input[type*=‘p’]        type属性包含p 的元素

'''
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
driver.get('http://119.91.231.179:9009/#/login')
# id定位
# username=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#normal_login_username")))
username=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span input")))
username.send_keys("admin")



sleep(5)

driver.quit()