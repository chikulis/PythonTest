import http.cookiejar,urllib.request
#实例化
cookie=http.cookiejar.CookieJar()
#
handler=urllib.request.HTTPCookieProcessor(cookie)
opener=urllib.request.build_opener(handler)
response=opener.open('https://www.baidu.com/')
print(cookie)
for item in cookie:
    print(item.name+"="+item.value)