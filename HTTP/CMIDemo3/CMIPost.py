# -*- coding: utf-8 -*-
import time
import httplib, urllib
import CMIConfig

class CMIPost():
    def __init__(self,url,type,spid,areaid,checkresult,timeout):
        self.url=url
        self.type=type
        self.spid=spid
        self.areaid=areaid
        self.checkresult=checkresult
        self.timeout=timeout

    def sedpost(self):
        print "发送了post请求"
        print self.url,self.type,self.spid,self.areaid,self.checkresult,self.timeout
        print time.ctime()
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
'''% (time.ctime(),self.areaid,self.type,self.url,self.spid)
        headerdata = {"Host":"10.13.1.1:32300",
                      "Content-type": "text/xml; charset=utf-8",
                      "Accept": "application/soap+xml, application/dime, multipart/related, text/*",
                      "User-Agent":"Axis/1.4",
                      "Cache-Control":"no-cache",
                      "Pragma":"no-cache",
                      "SOAPAction":""}

        requrl = "/services/CdncmsEngine"
        conn = httplib.HTTPConnection("10.13.1.1",32300)
        conn.request(method="POST",url=requrl,body=text,headers = headerdata)
        response = conn.getresponse()
        print response.status, response.reason
        print response.msg

        #校验响应头
        if response.status==200:
            print "success"
        else:
            print "failed"

        if self.checkresult:
            print "waiting for ...",self.timeout
            self.checkoracle(self.url)
        else:
            print "不检查数据库"
            pass

    def checkoracle(self,url):
        print "数据库连接失败,url is:",url
        pass