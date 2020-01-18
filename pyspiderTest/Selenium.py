from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
# browser=webdriver.Chrome()
# browser.get('https://www.baidu.com')
# input=browser.find_element_by_id('kw')
# input.send_keys('极客挖掘机')
# input.send_keys(Keys.ENTER)
# print(browser.current_url)
# print(browser.get_cookies())
# print(browser.page_source)

# chrome_options=Options()
# chrome_options.add_argument('--window-size=1366,768')
# driver=webdriver.Chrome(chrome_options=chrome_options)
# url='https://www.geekdigging.com/'
# driver.get(url)
# title=driver.find_element_by_xpath('//*[@id="text-4"]/div/div/div[1]/div[2]/a')
# print(title)
# print (title.get_attribute('href'))
# print(title.text)
# print(title.location)
# print(title.size)
# time.sleep(10000)

#执行javascript
# driver=webdriver.Chrome()
# driver.get('https://www.taobao.com/')
# driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
# time.sleep(10000)

browser=webdriver.Chrome()
browser.get('https://www.geekdigging.com/')
print(browser.get_cookies())
browser.add_cookie({'name':'name','domain':'www.geekdigging.com','value':'geekdigging'})
print(browser.get_cookies())
browser.delete_all_cookies()
print(browser.get_cookies())