from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://www.baidu.com/s?wd=三国&ie=UTF-8')
# driver.execute_script('document.body.scrollTop=600')
import time
for i in range(20):
    # driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    driver.execute_script("window.scrollTo(0,{})".format(i*100))
    time.sleep(1)

# 只能存png
driver.save_screenshot('a.png')
driver.quit()