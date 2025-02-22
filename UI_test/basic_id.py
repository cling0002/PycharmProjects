'''
元素定位
id      name     class_name  tag_name   link_text   xpath   css  partial_link_text
输入方法：元素对象.send_keys（“内容”）

class_name方法中 class属性值可能重复 需要确认唯一性才能使用
方法名为class_name 找元素的class属性值
如果元素的class存在多个属性值只能使用一个

超链接元素定位
link_text   取超链接文本信息

点击方法 元素对象.click()
    password.click()
 '''


'''
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "myElementId")))

'''
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
driver.get('http://119.91.231.179:9009/#/login')
# id定位
username=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "normal_login_username")))

    # driver.find_element(By.ID,"normal_login_username")
username.send_keys("admin")

password=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "normal_login_password")))

password.send_keys("123456")

login=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "login-form-button")))
login.click()
sleep(5)

driver.quit()
