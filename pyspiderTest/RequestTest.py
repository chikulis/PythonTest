import requests
# params={
#     'name':'geekdigging',
#     'age':'19'
# }
# rl=requests.get('https://httpbin.org/get',params)
# print(rl.text)

# r3=requests.get("https://www.baidu.com/img/superlogo_c4d7df0a003d3db9b65e9ef0fe6da1ec.png")
# with open('baidu_logo.png','wb') as f:
#     f.write(r3.content)

#post
# headers={'User-Agent':'Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
# 'referer':'https://www.geekdigging.com/'}
# params={'name':'geekdigging','age':'18'}
# r=requests.post('https://httpbin.org/post',data=params,headers=headers)
# print(r.text)

# proxies_socket={'http':'socks5://user:pass@host:port','https':'socks5://user:pass@host:port'}
# requests.get("https://www.geekdigging.com/",proxies=proxies_socket)

#cookies
# r=requests.get("https://www.csdn.net")
# print(type(r.cookies),r.cookies)
# for key,value in r.cookies.items():
#     print(key+'='+value)

#设置Session?
requests.get('https://httpbin.org/cookies/set/number/123456789')
r=requests.get('https://httpbin.org/cookies')
print(r.text)

s=requests.Session()
s.get('https://httpbin.org/cookies/set/number/123456789')
r=s.get('https://httpbin.org/cookies')
print(r.text)




