'''
from selenium.webdriver import ActionChains
# 实例化鼠标对象
action=ActionChains(driver)
# 调用鼠标方法
右键单击
    action.context_click(username)
左键 鼠标双击
    action.double_click()
鼠标拖动
    源元素     source=WebDriverWait(driver, 10).until((EC.presence_of_element_located(By.XPATH, "kw")))
    目标元素    target=WebDriverWait(driver, 10).until((EC.presence_of_element_located(By.XPATH, "kw")))
    调用方法    action.drag_and_drop(source,target).perform()
鼠标悬停
    action.move_to_element()
    ActionChains(driver).move_to_element(xxx).perform()
# 执行方法，该方法必须调用否则无效
action.perform()


模拟键盘操作
         send_keys(Keys.BACK_SPACE)
        send_keys(Keys.SPACE)
        send_keys(Keys.TAB)
        send_keys(Keys.ENTER)
        send_keys(Keys.CONTROL,'a')
        send_keys(Keys.CONTROL,'C')


隐式等待
    driver.implicitly_wait()

显式等待
    from  selenium.webdriver.support.wait import WebDriverWait



下拉框操作

    select 类
    select=select(element)
        element:<select>标签对应的元素，

    操作方法：
        select_by_index(index)  根据option索引来定位 从0开始
        select_by_value(value)  根据option 属性value定位
        select_by_visible_text(text)    更具option显式的文本来定位

    from selenium.webdriver.support.select import Select
    sele=Select(WebDriverWait(driver, 10).until((EC.presence_of_element_located(By.XPATH, ""))))
    select.select_by_index(index=)
'''

from selenium import webdriver
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("")

# 定位目标元素
username=WebDriverWait(driver, 10).until((EC.presence_of_element_located(By.XPATH, "kw"))).send_keys("")

# 实例化鼠标对象
action=ActionChains(driver)
# 调用鼠标方法
action.context_click(username)

# 执行方法，该方法必须调用否则无效
action.perform()

sleep(3)
driver.quit()
