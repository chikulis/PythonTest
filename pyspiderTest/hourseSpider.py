import requests
from pyquery import PyQuery

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}

def getOuterList(maxNum):
    list=[]
    for i in range(1,maxNum+1):
        url='https://sh.lianjia.com/ershoufang/pg'+str(i)
        print('链接：%s'%url)
        response=requests.get(url,headers=headers)
        print('获取第%d页房源'%i)
        doc=PyQuery(response.text)
        num=0
        for item in doc('.sellListContent li').items():
            num+=1
            list.append(item.attr('data-lj_action_housedel_id'))
        print('当前页共%d套房'%num)
    return list

def getInnerInfo(list):
    for i in list:
        try:
            response=requests.get('https://sh.lianjia.com/ershoufang/'+str(i)+'.html',headers=headers)
            doc=PyQuery(response.text)  
            #基本属性解析
            baseLiItem=doc('.base.content ul li').remove('.label').items()
            baseLiList=[]
            for item in baseLiItem:
                baseLiList.append(item.text())

            #交易属性
            transactionLiItem=doc('.transaction .content ul li').items()
            transactionLiList=[]
            for item in transactionLiItem:
                transactionLiList.append(item.children().not_('.label').text())
            
            print("id:"+i+"总价"+doc('.price .total').text()+"区域"+doc('.areaName .info').text())
        except:
            print(i,'：异常')
            continue

def main():
    
    list=getOuterList(100)
    getInnerInfo(list)

if __name__=='__main__':
    main()

