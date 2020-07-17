from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait #显示等待类
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.common.by import By  #定位的元素



driver=webdriver.Chrome()


driver.get("http://www.baidu.com")
driver.find_element_by_id('kw').send_keys("柠檬班")
driver.find_element_by_id("su").click()

WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,'//a[text()="柠檬班全栈"]')))
ele=driver.find_element_by_xpath('//a[text()="柠檬班全栈"]')

driver.execute_script("arguments[0].scrollIntoView(false);",ele)