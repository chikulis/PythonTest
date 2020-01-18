# from urllib.error import URLError
# from urllib.request import ProxyHandler,build_opener
# _proxyHandler=ProxyHandler({
#     'http':'http://182.34.37.0:9999',
#     'https':'https://117.69.150.84:9999'
# })
# opener=build_opener(_proxyHandler)
# try:
#     response=opener.open('https://httpbin.org/get') 
#     print(response.read().decode('utf-8'))
# except URLError as e:
#     print(e.reason)


# import requests
# proxies={
#     'http': 'http://59.52.186.117:9999',
#     'https': 'https://222.95.241.6:3000',
# }
# try:
#     response=requests.get('https://httpbin.org/get',proxies=proxies)
#     print(response.text)
# except requests.exceptions.ConnectionError as e:
#     print('Error',e.args)


from selenium import webdriver
import time
proxy='222.95,241,6:3000'
chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument('--proxy--server=https://'+proxy)
driver=webdriver.Chrome(chrome_options=chrome_options)
driver.get('https://httpbin.org/get')
time.sleep(10)