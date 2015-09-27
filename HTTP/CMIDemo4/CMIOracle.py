# -*- coding: utf-8 -*-
#!/usr/bin/python
import cx_Oracle
import time
try:
    conn = cx_Oracle.connect('iptvmdn/Vtpimdn_2012@10.13.1.3:1526/iptvmdn')
except:
    print "数据库链接失败"

cursor = conn.cursor()
url="http://images.apple.com/support/assets/images/layout/psp/nav/nav_icon_phone.png"
count=0
for i in range(10):
    cursor.execute ("select task_status from (SELECT * FROM task_info where webcdn_url = '%s' and task_type = 1 order by submit_time desc) where rownum = 1" % url)
    rows = cursor.fetchall()
    if rows!=None and count< 10:
        break
    elif count>=10:
        print (u'数据库查询超时失败,url is %s' %url)
        break
    time.sleep(1)
    count+=1
    print count
# cursor.execute ("select task_status from (SELECT * FROM task_info where webcdn_url = '%s' and task_type = 1 order by submit_time desc) where rownum = 1" % url)
# rows = cursor.fetchall()
for row in rows:
    if row == None:
        print "查询数据库失败"
    else:
        print "查询结果是：",row[0]
cursor.close()
conn.close()