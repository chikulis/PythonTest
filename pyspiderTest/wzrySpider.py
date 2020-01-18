import os
import requests
url='https://pvp.qq.com/web201605/js/herolist.json'
herolist=requests.get(url)
herolist_json=herolist.json()
hero_name=list(map(lambda x:x['cname'],herolist.json()))
hero_number=list(map(lambda x:x['ename'],herolist.json()))
# print (hero_name)

#下载图片
def downloadPic():
    i=0
    for j in hero_number:
        #创建文件夹
        os.mkdir("C:\\Users\\Administrator\\Desktop\\wzry\\"+hero_name[i])
        #进入文件夹
        os.chdir("C:\\Users\\Administrator\\Desktop\\wzry\\"+hero_name[i])
        i+=1
        for k in range(10):
            onehero_link='http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/'+str(j)+'/'+str(j)+'-bigskin-'+str(k)+'.jpg'
            im=requests.get(onehero_link)#请求URL
            if im.status_code==200:
                open(str(k)+'.jpg','wb').write(im.content)#写入文件

downloadPic()
