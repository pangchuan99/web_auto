from selenium.webdriver.support.wait import WebDriverWait        #显示等待类
#显示等待类提供一系列期望发生的条件 1.元素存在 presence_of_element_located
                                # 2.元素可见 visibility_of_element_located
from selenium.webdriver.support import expected_conditions as EC
from  selenium.webdriver.common.by import By                     #八大元素
import random





class IndexPage:


    def __init__(self,driver):
        self.driver=driver


    def isExist_logout_ele(self):
        try:
              WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,'//a[contains(text(),"系统设置")]')))
              return True
        except:
            return False
        pass
        #如果存在就返回True，如果不存在，就返回False


    #选标操作---默认选择第一个，元素定位的时候，过滤掉不可以投的标
    def  click_first_bid(self):
        pass


    #随机选一个标
    def click_bid_by_random(self):
        eles=self.driver.find_elements()
        #随机数
        index=random.randint(0,len(eles-1))
        eles[index].click()
        pass

