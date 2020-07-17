

from  selenium.webdriver.common.by import By


class LoginPageLocator:
    # 元素定位
    # 用户名输入框
    name_text = (By.XPATH, '//input[@type="text"]')
    # 密码输入框
    pwd_text = (By.XPATH, '//input[@type="password"]')
    # 点击登录
    login_but = (By.XPATH, '//button[contains(text(),"登录")]')

    #值班管理
    zbgl=(By.XPATH,'//div[contains(text(),"值班管理")]')
    zbjl=(By.XPATH,'//a[contains(text(),"值班记录")]')#值班管理---值班记录
    zbjl_bc=(By.XPATH,'//button[contains(text(),"保存")]')#值班管理---值班记录---保存按钮
    zbcx=(By.XPATH,'//a[contains(text(),"值班查询")]')#值班管理---值班查询

