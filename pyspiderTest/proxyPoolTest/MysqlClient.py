# MYSQL_HOST='localhost'
# MYSQL_PORT=3306
# MYSQL_USER='root'
# MYSQL_PASSWORD='password'
# MYSQL_DB='test'
# MYSQL_CHARSET='utf8mb4'#使用的字符集

import pymysql
import uuid

class MSsqlClient(object):
    # def __init__(self,host=MYSQL_HOST,port=MYSQL_PORT,user=MYSQL_USER,
    # password=MYSQL_PASSWORD,database=MYSQL_DB,charset=MYSQL_CHARSET):
    #     self.conn=pymysql.connect(
    #         host=host,
    #         port=port,
    #         user=user,
    #         password=password,
    #         database=database,
    #         charset=charset
    #     )

     def __init__():
        self.connect=pymssql.connect(host='XFXXCP14\MSSQLSERVER2012',user='sa',password='123456',database='TestDB',charset='utf8')
        # self.conn=pymysql.connect(
        #     host=host,
        #     port=port,
        #     user=user,
        #     password=password,
        #     database=database,
        #     charset=charset
        # )


    # def addProxy(self,proxy):
    #     #proxy代理字典
    #     sql='INSERT INTO <code>proxy_pool</code> VALUES (%(id)s, %(scheme)s, %(ip)s, %(port)s, %(status)s, %(response_time)s, now(), null )'
    #     data={
    #         "id":str(uuid.uuid1()),
    #         "scheme":proxy['scheme'],
    #         "ip":proxy['ip'],
    #         "port":proxy['port'],
    #         "status":proxy['status'],
    #         "response_time":proxy['response_time'],
    #     }
    #     self.conn.cursor().execute(sql.data)
    #     self.conn.commit()

    #获取所有可用代理
    def findAll(self):
        sql='SELECT * FROM proxy_pool WHERE status = "1" ORDER BY update_date ASC'
        cursor=self.conn.cursor()
        cursor.execute(sql)
        res=cursor.fetchall()
        cursor.close()
        self.conn.commit()
        return res

    def updateProxy(self,proxy):
        sql='UPDATE proxy_pool SET scheme = %(scheme)s, ip = %(ip)s, port = %(port)s, status = %(status)s, response_time = %(response_time)s, update_date = now()  WHERE id = %(id)s'
        data={
            "id":proxy['id'],
            "scheme":proxy['scheme'],
            "ip":proxy['ip'],
            "port":proxy['port'],
            "status":proxy['status'],
            "response_time":proxy['response_tiem'],
        }
        self.conn.cursor().execute(sql,data)
        self.conn.commit()