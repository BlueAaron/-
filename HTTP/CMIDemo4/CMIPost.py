# -*- coding: utf-8 -*-
import time
import httplib, urllib
import cx_Oracle
import time
import CMIPublic

class CMIPost():
    def __init__(self,url,type,spid,areaid,checkresult,checkcache,timeout,Main):
        self.url=url
        self.type=type
        self.spid=spid
        self.areaid=areaid
        self.checkresult=checkresult
        self.checkcache=checkcache
        self.timeout=timeout
        #主界面对象，用户打印日志
        self.Main=Main

    def sedpost(self):

        print self.url,self.type,self.spid,self.areaid,self.checkresult,self.checkcache,self.timeout
        print time.strftime("%Y-%m-%d %H:%M:%S")

        cmiip=CMIPublic.cmiconfig['cmiip']

        text='''<?xml version="1.0" encoding="UTF-8"?>
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
<soapenv:Body>
<addHcsContent xmlns="http://engine.wsi.mdn.huawei.com">
   <req>
      <contentDir xsi:nil="true"/>
      <deliveryTime>%s
</deliveryTime>
      <dstAreaSet>
        <item>%s</item>
      </dstAreaSet>
      <param xsi:nil="true"/>
       <protectTime>72</protectTime>
      <serviceType>%s</serviceType>
      <serviceUrl>%s</serviceUrl>
      <spid>%s</spid>
   </req>
</addHcsContent>
</soapenv:Body>
</soapenv:Envelope>
'''% (time.strftime("%Y-%m-%d %H:%M:%S"),self.areaid,self.type,self.url,self.spid)
        headerdata = {"Host":cmiip+":32300",
                      "Content-type": "text/xml; charset=utf-8",
                      "Accept": "application/soap+xml, application/dime, multipart/related, text/*",
                      "User-Agent":"Axis/1.4",
                      "Cache-Control":"no-cache",
                      "Pragma":"no-cache",
                      "SOAPAction":""}

        requrl = "/services/CdncmsEngine"

        conn = httplib.HTTPConnection(cmiip,32300)
        # print text
        try:
            # CMI.MainWidget.printLog("正在发送请求")
            conn.request(method="POST",url=requrl,body=text,headers = headerdata)
            response = conn.getresponse()
            self.Main.printLog(u'post请求已经提交')
            # print response.status, response.reason
            # print response.msg
            #校验响应头
            print response.msg
            print response.status
            if response.status==200:
                self.Main.printLog(u'200 OK  发送成功')
                pass
            else:
                self.Main.printLog(u'%s OK  发送失败' %response.status)
                pass

            if self.checkresult:

                count=0
                #不设置超时时间默认60秒
                if int(self.timeout)==0:
                    timeout=60
                else:
                    timeout=int(self.timeout)
                self.Main.printLog(u'正在校验注入结果... 超时时间%s秒' %timeout)

                flag=True
                while True:
                    result=self.checkoracle(self.url)
                    if result==8 or  result==9:
                        # print "查询成功"
                        break
                    elif result==7:
                        if flag==True:
                            self.Main.printLog(u'URL：%s 注入Running' % self.url)
                            flag=False
                    elif count>=timeout and result==7:
                        self.Main.printLog(u'注入结果查询超时，当前Running,url is %s' % self.url)
                        break
                    elif count>=timeout and result==666:
                        # print "未知注入结果"
                        self.Main.printLog(u'未知注入结果,url is %s' % self.url)
                        break
                    elif count>=timeout:
                        # print "数据库查询超时失败"
                        self.Main.printLog(u'数据库查询超时失败,url is %s' % self.url)
                        break
                    time.sleep(1)
                    count+=1

            else:
                self.Main.printLog(u'不检查数据库')
                pass

            if self.checkresult:
                self.checkcache(self.url)
            else:
                self.Main.printLog(u'不检查cache')
                pass

        except:
            self.Main.printLog(u'post发送失败，请检查IP')
            pass
        finally:
            conn.close()

    def checkoracle(self,url):
        try:
            cmiip=CMIPublic.cmiconfig['cmiip']

            conn = cx_Oracle.connect('iptvmdn/Vtpimdn_2012@'+cmiip+':1526/iptvmdn')
            cursor = conn.cursor()
            url=self.url
            cursor.execute ("select task_status from (SELECT * FROM task_info where webcdn_url = '%s' and task_type = 1 order by submit_time desc) where rownum = 1" % url)
            rows = cursor.fetchall()

            for row in rows:
                print row[0]
                if row == None:
                    self.Main.printLog(u'数据库查询失败,url is %s' %url)
                else:
                    if row[0]==9:
                        self.Main.printLog(u'URL：%s 注入成功' %url)
                        return row[0]
                    elif row[0]==7:
                        # self.Main.printLog(u'URL：%s 注入Running' %url)
                        return row[0]
                    elif row[0]==8:
                        self.Main.printLog(u'URL：%s 注入失败' %url)
                        return row[0]
                    else:
                        # self.Main.printLog(u'URL：%s 未知注入结果' %url)
                        return 666

        except:
            self.Main.printLog(u'数据库连接失败,url is %s' %url)
            return 666
        finally:
            cursor.close()
            conn.close()

    def checkcache(self,url):
        try:
            conn1 = httplib.HTTPConnection("images.apple.com")
            conn1.request("GET", "/mac/home/images/productbrowser/mac/imac.png")
            r1 = conn1.getresponse()
            print r1.status, r1.reason
        except:
            self.Main.printLog(u'Cache发送失败，请检查IP')
        finally:
            conn1.close()
        print "检查cache"