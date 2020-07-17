
from selenium.webdriver.support.wait import WebDriverWait        #显示等待类
#显示等待类提供一系列期望发生的条件 1.元素存在 presence_of_element_located
                                # 2.元素可见 visibility_of_element_located
from selenium.webdriver.support import expected_conditions as EC

import random
import datetime








#封装基本函数---执行日志---异常处理---失败截图
#所有的页面公共的部分

import logging
class BasePage:
    def __init__(self,driver):
        self.driver=driver



    #等待元素可见
    def wait_eleVisible(self,locator,times=30,poll_frequency=0.5,doc=""):
        """

        :param locator:元素定位。元组形式
        :param times:
        :param poll_frequency:
        :param doc:模块名——页面名称——操作名称
        :return:
        """
        logging.info("等待元素 {0} 可见".format(locator))
        try:
            start=datetime.datetime.now()
            #开始等待的时间
            WebDriverWait(self.driver,times,poll_frequency).until(EC.visibility_of_element_located(locator))
            #结束等待的时间点
            end=datetime.datetime.now()
            #求一个差值，写在日志当中。等待了多久
            logging.info("等待时长。等待时长为：{0}".format())
        except:
            logging.exception("等待元素可见失败！！！")
            #截图操作
            self.save_screenshot(doc)

            #异常
            raise

        pass


    #等待元素存在
    def wait_elePresence(self):
        pass


    #查找元素
    def get_element(self):

        pass

    #点击操作
    def click_element(self):
        pass

    #输入操作
    def input_text(self):
        pass

    #获取元素的文本内容
    def get_text(self):
        pass

    #获取元素的属性
    def get_elment_attribute(self):
        pass

     #alert处理
    def alert_action(self,action="accept"):
        pass
    #iframe切换
    def switch_iframe(self,iframe_reference):
        pass
    #上传操作
    def upload_file(self):
        pass
    #滚动条处理
    #窗口切换



    #截图操作
    def save_screenshot(self,name):
        #图片名称：模块名---页面名称——操作名称——（年_月_日_时分秒）--.png
        file_name="截屏存放的路径"+"{0}_{1}.png".format(name,)
        self.driver.save_screeshot(file_name)
        logging.info("截取网页成功。文件路径为：{}".format(file_name))
        pass







