from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait #显示等待时间
from selenium.webdriver.support import  expected_conditions as EC#元素
from selenium.webdriver.common.by import By  #定位的元素
from selenium.webdriver.common.action_chains import ActionChains
import time

#
# driver=webdriver.Chrome()
# driver.implicitly_wait(30)
#
# driver.get("http://www.baidu.com")
# driver.find_element_by_xpath('//*[@id="u1"]//a[@name="tj_login"]').click()
#
# id="TANGRAM__PSP_10__footerULoginBtn"
# WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,id)))
#
#
# driver.find_element_by_id("TANGRAM__PSP_10__footerULoginBtn").click()
#
#
#
# ActionChains()
#
#
# driver.execute_script()





driver=webdriver.Chrome()


driver.get("http://svn.jdjinsui.com:55536/login")
name_text = '//input[@type="text"]'
pwd_text = '//input[@type="password"]'
login_but = '//button[contains(text(),"登录")]'
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, name_text)))
driver.find_element_by_xpath(name_text).send_keys("pc")
driver.find_element_by_xpath(pwd_text).send_keys("123456")
# 判断一下remeber_user的值，来决定是否勾选

driver.find_element_by_xpath(login_but).click()


WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,'//div[contains(text(),"值班管理")]')))
# 鼠标悬停
ele=driver.find_element_by_xpath('//div[contains(text(),"值班管理")]')

ActionChains(driver).move_to_element(ele).perform()

# 点击值班记录
WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,'//a[contains(text(),"值班记录")]')))
driver.find_element_by_xpath('//a[contains(text(),"值班记录")]').click()

WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,'//button[contains(text(),"保存")]')))
driver.find_element_by_xpath('//button[contains(text(),"保存")]').click()
# 点击投标按钮

# WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//p[contains(text(),"用户名")]')))
#
# re=driver.find_element_by_xpath('//p[contains(text(),"用户名")]').text
#
# print(re)
#

