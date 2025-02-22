import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class TestLogin(object):
    def test_account_does_not_exist(self):
        pass

    def test_wrong_password(self):
        driver = webdriver.Chrome()
        driver.get("http://119.91.231.179:9009/#/login")
        # driver.maximize_window()
        # username=WebDriverWait(driver, 10).until((EC.presence_of_element_located(By.ID, "normal_login_username")))
        username = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "normal_login_username"))
        )

        username.send_keys("admin")

        password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "normal_login_password")))
        password.send_keys("123123")

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "login-form-button"))).click()

        # msg=WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, "anticon-close-circle"))).text
        # print("错误信息：", msg)
        try:
            element = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.CLASS_NAME, "anticon-close-circle")))
            # 如果需要，您可以检查元素的文本内容，但请确保它确实包含文本
            msg = element.text if element.text else "图标没有文本内容"
            print("错误信息：", msg)
        except Exception as e:
            print("元素未找到或发生错误：", e)

        driver.quit()


if __name__=='__main__':
    pytest.main(['-s','test_02.py'])
