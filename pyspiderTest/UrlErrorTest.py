from urllib import request,error
try:
    response=request.urlopen('https://www.geekdigging.com/aa')
except error.HTTPError as e:
    print(e.reason,e.code,e.headers,sep='\n')
except error.URLError as e:
    print(e.reason)
else:
    print('request success')

try:
    response=request.urlopen('https://www.baidu.com',timeout=0.001)
except error.URLError as e:
    print(e.reason)