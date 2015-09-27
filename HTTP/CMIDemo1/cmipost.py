# -*- coding: utf-8 -*-
import httplib, urllib
text='''<?xml version="1.0" encoding="UTF-8"?>
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
<soapenv:Body>
<addHcsContent xmlns="http://engine.wsi.mdn.huawei.com">
   <req>
      <contentDir xsi:nil="true"/>
      <deliveryTime>2015-07-26 06:28:05
</deliveryTime>
      <dstAreaSet>
        <item>1</item>
      </dstAreaSet>
      <param xsi:nil="true"/>
       <protectTime>72</protectTime>
      <serviceType>176</serviceType>
      <serviceUrl>http://www.baidu.com/webpages/file_20150720142855.jpg<;/serviceUrl>
      <spid>2000000000</spid>
   </req>
</addHcsContent>
</soapenv:Body>
</soapenv:Envelope>
'''
headerdata = {"Host":"129.42.180.10:32300",
              "Content-type": "text/xml; charset=utf-8",
              "Accept": "application/soap+xml, application/dime, multipart/related, text/*",
              "User-Agent":"Axis/1.4",
              "Cache-Control":"no-cache",
              "Pragma":"no-cache",
              "SOAPAction":"",
              "Content-Length":"749"}
requrl = "https://10.13.1.1:32304/cdncms/login.action"
conn = httplib.HTTPConnection("10.13.1.1",32304)
conn.request(method="POST",url=requrl,body=text,headers = headerdata)
response = conn.getresponse()
print response.status, response.reason
data = response.read()
conn.close()