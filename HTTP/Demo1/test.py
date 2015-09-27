# -*- coding: utf-8 -*-
#!/usr/bin/python
import httplib
conn = httplib.HTTPConnection("www.bluedoraemon.com", 80, False)
conn.request("GET", "/index.html")
r1 = conn.getresponse()
print r1.status
print r1.reason
print r1.version
print r1.getheaders()
print r1.msg

data1 = r1.read()
print len(data1)
# print data1
