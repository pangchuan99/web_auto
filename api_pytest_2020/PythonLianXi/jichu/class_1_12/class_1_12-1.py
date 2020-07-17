from selenium import webdriver
import HTMLTestRunnerNew

# webdriver=webdriver.Firefox()
webdriver=webdriver.Chrome()
webdriver.get("HTTPS://www.baidu.com")


HTMLTestRunnerNew.HTMLTestRunner