#-*- coding:utf-8 -*-
'''
发送txt文本邮件
'''
import smtplib  
from email.mime.text import MIMEText  


'''
函数名       : DMSMailSendInfo
功能描述     : 发送TXT文件消息邮件
输入参数     : DMSMsgContent(消息内容)
返回值       : to_list(发送的对象列表)，sub(邮件标题)，content(消息文本内容)
被调用函数   :
作者         : DMS
日期         : 2015-3-19
修改日期     :
修改内容     :
'''   
  
def DMSMailSendInfo(mail_host,frommail,to_list,sub,content,mail_user,mail_pass):  
    me="hello"+"<"+frommail+">"  
    msg = MIMEText(content,_subtype='plain',_charset='utf-8')  
    msg['Subject'] = sub  
    msg['From'] = me  
    msg['To'] = ";".join(to_list)
    try:  
        server = smtplib.SMTP()  
        server.connect(mail_host)  
        server.login(mail_user,mail_pass)  
        server.sendmail(me, to_list, msg.as_string())  
        server.close()  
        return True  
    except Exception, e:  
        return False  