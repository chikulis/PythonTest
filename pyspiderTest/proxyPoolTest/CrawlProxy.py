import requests
from pyquery import PyQuery
from MysqlClient import MysqlClient
from VerifyProxy import VerifyProxy
# 
class CrawProxy(object):
    def __init__(self):
        self.mysql=MysqlClient()
        self.verify=VerifyProxy()
    
    def getPage(self,url,charset):
        response=requests.get(url)
        response.encoding=charset
        return response.text
    #获取代理 ip3366
    def crawl_ip3366(self,page_num=3):
        startUrl='http://www.ip3366.net/?stype=1&page={}'
        urls=[startUrl.format(page) for page in range(1,page_num+1)]
        for url in ruls:
            print('crawl:',url)
            html=self.getPage(url,'gb2312') 
            if html:
                d=PyQuery(html)
                trs=d('.table-bordered tbody tr').items()
                for tr in trs:
                    scheme=tr.find('td:nth-child(4)').text().lower()
                    ip=tr.find('td:nth-child(1)').text()
                    port=tr.find('td:nth-child(2)').text()
                    verify_result=relf.verify.VerifyProxy(scheme,ip,port)
                    if verify_result["status"]=='1':
                        proxy={
                            "scheme":scheme,
                            "ip":ip,
                            "port":port,
                            "status":verify_result["status"],
                            "response_time":verify_result["response_time"],
                        }
                        #存入数据库
                        self.mysql.add_proxy(proxy)
                        print('代理',ip,'测试通过，保存成功')
                    else:
                        print('代理',ip,'测试未通过')

if __name__=='__main__':
    CrawProxy().crawl_ip3366()