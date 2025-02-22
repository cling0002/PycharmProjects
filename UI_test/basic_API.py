'''
maximize_window()   最大化窗口
set_window_size(width,height)       设置窗口大小
set_window_position(x,y)        设置窗口位置
back()      后退
forward()       前进
refresh()       刷新
close()        关闭窗口
quit()  关闭浏览器
title   获取当前页面title
current_url        获取当前页面url


size                        返回元素大小
text                         获取元素的文本
get_attribute("xxx")        获取属性值，传递的参数为元素的属性名
is_displayed()                 元素是否可见
is_enabled()                    元素是否可用
is_selected()                   元素是否选中






'''


from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.baidu.com")

# username=WebDriverWait(driver, 10).until(EC.presence_of_element_located(By.XPATH, "")).send_keys("")
WebDriverWait(driver,5).until(EC.presence_of_element_located((By.ID,"kw"))).send_keys("知乎")

WebDriverWait(driver,5).until(EC.presence_of_element_located((By.ID,'su'))).click()
sleep(2)

driver.back()
sleep(2)

driver.forward()
sleep(2)


driver.refresh()


sleep(3)
driver.quit()
