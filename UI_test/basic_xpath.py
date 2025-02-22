# find_element_by_xpath('xpath策略'）
"""
路径：
    /html/xxx/xxx/xxxx    绝对路径
    //xxx    //*    相对路径  匹配任意节点

/html/body/div/div[1]/div/div[2]/div/form/div[4]/div/div/div/div/button
//*[@id="normal_login"]/div[4]/div/div/div/div/button
元素属性：
    //标签名[@属 性名=’属性值‘]               保证唯一性
    //*[@id="normal_login_password"]
    //指定标签[@id="normal_login_password"]

属性与逻辑结合
    //*[@id="normal_login_password" and @id="normal_login_password"  ]

层级和属性结合
    //*[@id='p1']/input

衍生
      //*[text()="XXX"]     文本内容是xxx的元素
      //*[contains(@attribute,'XXX')]   属性中含有xxx的元素
      //*[starts-with(@attribute,'xxx')]   属性以xxx开头的元素
"""

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
driver.get('http://119.91.231.179:9009/#/login')
# id定位
username=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div/div[2]/div/form/div[1]/div/div/div/div/span/input")))

username.send_keys("admin")

password=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="normal_login_password"]')))

password.send_keys("123456")

# login=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "login-form-button")))
# login.click()


sleep(5)

driver.quit()