from selenium import  webdriver
from selenium.webdriver.support.wait import WebDriverWait        #显示等待类
#显示等待类提供一系列期望发生的条件 1.元素存在 presence_of_element_located
                                # 2.元素可见 visibility_of_element_located
from selenium.webdriver.support import expected_conditions as EC
from  selenium.webdriver.common.by import By                     #八大元素


#这个是页面的元素定位，那么另一个网页就是元素的操作（要分离彻底）



class LoginPage:


    def __init__(self,driver):
        self.driver=driver

          # 登录操作

    def login(self, username, password):


        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.name_text))
        self.driver.find_element(*loc.name_text).send_keys(username)
        self.driver.find_element(*loc.pwd_text).send_keys(password)
        # 判断一下remeber_user的值，来决定是否勾选

        self.driver.find_element(*loc.login_but).click()

        # 做判断处理





    def get_errorMsg_from_pageCenter(self):

        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.XPATH,'//div[@class="ivu-notice-title"]')))

        return self.driver.find_element_by_xpath('//div[@class="ivu-notice-title"]').text





