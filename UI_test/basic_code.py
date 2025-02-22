'''
web自动化基本代码
1.导入模块
2实例化浏览器对象:类名()
3.打开网页
4.观察效果
5.关闭页面


最新元素定位添加
            1.  from selenium.webdriver.common.by import By
                # 现在你可以使用 By 类来定位元素了
                driver.find_element(By.ID, "element_id")
         2.     from selenium.webdriver.common.by import By
                from selenium.webdriver.support.ui import WebDriverWait
                from selenium.webdriver.support import expected_conditions as EC
                # 等待页面加载出来之后再进行
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "myElementId")))
``
'''
from time import sleep
# 1.导入模块
from selenium import webdriver
# 2实例化浏览器对象:类名()
driver=webdriver.Chrome()
# 3.打开网页
driver.get('http://baidu.com')
# 4.观察效果
sleep(5)
# 5.关闭页面
driver.quit()





