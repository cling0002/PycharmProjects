'''

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

弹出框处理
        alert   警告框
        confirm 确认框
        prompt  提示框

切换到弹窗
    系统弹窗
            alert=driver.switch_to.alert
        去除弹窗，同意/移除
             alert.accept()   同意
            alert.dismiss()     移除

    自定义弹窗

滚动条
    设置JavaScript脚本控制滚动条
    js="window.scrollTo(0,1000)"
    selenium 中提供执行js的方法
    driver.execute(js)
fram切换
    切换fram
        driver.switch_to.frame(frame_reference=)
    切回默认页面
        driver.switch_to.default_content()




多窗口切换
    handle=driver.current_window_handle        获取窗口句柄

    driver.switch_to.window(handle[])           切换指定句柄窗口


窗口截图
        driver.get_screenshot_as_file(impath)   impath  图片保存路径

时间错防止覆盖
        from time import strftime
        now_time=strftime('%Y%m%d_%H%M%S')
        driver.get_screenshot_as_file('./info_{}.png'.format(now_time))

验证码处理
    cookie绕过登陆操作            必须为 name   和value
        driver.get_cookie()
        driver.add_cookie(cookie_dict)


'''

from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from  selenium.webdriver.support.wait import WebDriverWait



driver = webdriver.Chrome()

driver.get("")

username=WebDriverWait(driver, 10).until((EC.presence_of_element_located(By.XPATH, ""))).send_keys("")

alert=driver.switch_to.alert


driver.get_cookie()
driver.add_cookie(cookie_dict)


sleep(3)
driver.quit()
