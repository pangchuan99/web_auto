


from selenium import  webdriver
from selenium.webdriver.support.wait import WebDriverWait        #显示等待类
#显示等待类提供一系列期望发生的条件 1.元素存在 presence_of_element_located
                                # 2.元素可见 visibility_of_element_located
from selenium.webdriver.support import expected_conditions as EC
from  selenium.webdriver.common.by import By                     #八大元素

from selenium.webdriver.common.action_chains import ActionChains #鼠标事件

#这个是页面的元素定位，那么另一个网页就是元素的操作（要分离彻底）



class Bidpage:


    def __init__(self,driver):
        self.driver=driver

          # 登录操作




    #投资操作
    #值班管理---值班记录
    def invest(self):
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(loc.zbgl))
        #鼠标悬停
        ActionChains(self.driver).move_to_element(self.driver.find_element(*loc.zbgl)).perform()
        #点击值班记录
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(loc.zbjl))
        self.driver.find_element(*loc.zbjl).click()

        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(loc.zbjl_bc))
        self.driver.find_element(*loc.zbjl_bc).click()

        return self.driver.find_element_by_xpath('//td[text()="监控员"]').text
        #点击投标按钮


     #获取用户余额
    #值班管理---值班查询
    def get_uer_money(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.zbgl))
        # 鼠标悬停
        ActionChains(self.driver).move_to_element(self.driver.find_element(*loc.zbgl)).perform()
        #点击值班查询
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc.zbcx))
        self.driver.find_element(*loc.zbcx).click()

    #     pass
    # #投资成功的提示框---点击查看并激活
    # def click_activeButton_on_success_popup(self):
    #     pass
    #
    # #错误的提示框---页面中间
    # def get_errorMsg_pageCenter(self):
    #     #获取文本内容
    #     #关闭弹出框
    #     pass
    #
    #
    # def get_errorMsg_from_investButton(self):
    #     pass
    #
    #
    #
