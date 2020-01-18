import requests
import re
import json
from pyquery import PyQuery

headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}

def GetStockList(stockListURL):
    r=requests.get(stockListURL,headers=headers)
    doc=PyQuery(r.text)
    list=[]
    #获取所有section中a节点，并迭代
    for i in doc('.stockTable a').items():
        try:
            href=i.attr.href
            list.append(re.findall(r"\d{6}",href)[0])
        except:
            continue
    list=[item.lower() for item in list]#转成小写
    return list

def GetStockInfo(list,stockInfoURL):
    count=0
    for stock in list:
        try:
            url=stockInfoURL+stock
            r=requests.get(url,headers=headers)
            #将获取到的数据封装进字典
            dict1=json.loads(r.text[14:int(len(r.text))-1])
            print(dict1)   
        except:
            print('异常')
            continue

def main():
    stockListUrl='https://hq.gucheng.com/gpdmylb.html'
    stockInfoUrl='http://qd.10jqka.com.cn/quote.php?cate=real&type=stock&callback=showStockDate&return=json&code='
    list=GetStockList(stockListUrl)
    GetStockInfo(list,stockInfoUrl)

if __name__=='__main__':
    main()