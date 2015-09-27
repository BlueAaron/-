# -*- coding: utf-8 -*-
# import xml.dom.minidom
import re
import sys
class Analyze():
    
    def __init__(self, filename):
        self.filename=filename
        self.unicodelist=[]
        self.templist=self.unicodelist
        self.isGO=True
        
    #判断空行
    def CheckEmptyLine(self,line):
        return line.isspace()
    
    #转换编码
    def ReadfiletoUnicode(self):
        linelist = open(self.filename).readlines()
        for i in linelist:
            #过滤空行，continue到for
            if self.CheckEmptyLine(i): 
                continue
            #去前后空格
            i=i.strip() 
            s=unicode(i,'gbk')
            self.unicodelist.append(s)
#         print self.unicodelist;
#         for i in self.unicodelist:
#             print i
            
    def GreatXML(self,firstindex,f):

        #全局标记，如果有一项检查是吧，后续不会插入数据
        AllFlag=0
        #生成需要遍历的列表
        
        self.templist=self.templist[firstindex:]
        #防止无限递归
        print len(self.templist),"剩余长度："
        if len(self.templist)>1 and self.isGO==True:
            for index,line in enumerate(self.templist):
                if self.isGO==True:
                    pattern = re.compile(r'(\d)\..*')
                    match = pattern.match(line.encode('utf-8'))
#                     print "??????????????"
                    if match:
#                         print line,"找到题目了"
                        #获取题目编号ID
                        id=match.group(1)
                        #获取题目开头index
                        titlefirstindex=index
                        titlelastindex=0
                        tempindex=index
                        while AllFlag==0:
                            tempindex+=1
                            if tempindex<len(self.templist):
                                pattern = re.compile(r'A\..*')
                                match = pattern.match(self.templist[tempindex].encode('utf-8'))
                                if match:
                                    #获取到题目最后一行index=tempindex-1，下面range这里不减一
                                    titlelastindex=tempindex
                                    #打印题目
                                    title='''

            <question id="idflag">
                <title>
                    <![CDATA[titleflag]]>
                </title>                '''
                                    s=""
                                    for m in range(titlefirstindex,titlelastindex):
                                        if m!=(titlelastindex-1):
                                            s+=self.templist[m].encode('utf-8')+"\n"
                                        else:
                                            #处理最后一行不带回车
                                            s+=self.templist[m].encode('utf-8')
                                    title=title.replace("titleflag",s)
                                    title=title.replace("idflag",id)
                                    f.write(title)
                                    break
                            else:
#                                 print "sorry,can not find A"
    
                                AllFlag=1
                                break
                        #初始化答案index
                        answerfirstindex=titlelastindex
                        answerlastindex=0
                        tempindex=answerfirstindex-1
                        while AllFlag==0:
                            tempindex+=1
                            if tempindex<len(self.templist):
                                #找到“正确答案”开头，上面全是答案
                                x="正确答案"
                                pattern = re.compile(r'%SQT正则校验工具案例.*'% x)
                                match = pattern.match(self.templist[tempindex].encode('utf-8'))
                                if match:
                                    print "OK ,find 正确答案",tempindex
                                    #获取到题目最后一行index=tempindex-1，下面range这里不减一
                                    answerlastindex=tempindex
                                    #打印题目
                                    answer='''
                <answer>
                    <A><![CDATA[Aanswerflag]]></A>
                    <B><![CDATA[Banswerflag]]></B>
                    <C><![CDATA[Canswerflag]]></C>
                    <D><![CDATA[Danswerflag]]></D>
                </answer>                             '''
                                    Aanswer=""
                                    Banswer=""
                                    Canswer=""
                                    Danswer=""
                                    trueanswer='''
                <trueanswer>
                    <![CDATA[trueanswerflag]]>
                </trueanswer>                             '''
                                    s=""
                                    for m in range(answerfirstindex,answerlastindex):
                                        if "A." in self.templist[m].encode('utf-8'):
                                            print "ok,find (A.)"
                                            Aanswer=self.templist[m].encode('utf-8')
                                            if "B." not in self.templist[m+1].encode('utf-8'):
                                                Aanswer+=self.templist[m+1].encode('utf-8')
                                            else:
                                                break
                                        else:
                                            print "error,can not find A.XXX"
                                    for m in range(answerfirstindex,answerlastindex):
                                        if "B." in self.templist[m].encode('utf-8'):
                                            print "ok,find (B.)"
                                            Banswer=self.templist[m].encode('utf-8')
                                            if "C." not in self.templist[m+1].encode('utf-8'):
                                                Banswer+=self.templist[m+1].encode('utf-8')
                                                break
                                            else:
                                                break
                                        else:
                                            print "error,can not find B.XXX"
                                    for m in range(answerfirstindex,answerlastindex):
                                        if "C." in self.templist[m].encode('utf-8'):
                                            print "ok,find (C.)"
                                            Canswer=self.templist[m].encode('utf-8')
                                            if "D." not in self.templist[m+1].encode('utf-8'):
                                                Canswer+=self.templist[m+1].encode('utf-8')
                                                for n in range((m+2),answerlastindex):
                                                    Danswer+=self.templist[n].encode('utf-8')
                                                break
                                            else:
                                                for n in range((m+1),answerlastindex):
                                                    Danswer+=self.templist[n].encode('utf-8')
                                                break
                                        else:
                                            print "error,can not find C.XXX"

                                    # for m in range(answerfirstindex,answerlastindex):
                                    #     if m!=(answerlastindex-1):
                                    #         SQT正则校验工具案例+=self.templist[m].encode('utf-8')+"\n"
                                    #     else:
                                    #         #处理最后一行不带回车
                                    #         SQT正则校验工具案例+=self.templist[m].encode('utf-8')
                                    t=self.templist[tempindex].encode('utf-8')

                                    #写入答案
                                    # answer=answer.replace("answerflag",SQT正则校验工具案例)
                                    answer=answer.replace("Aanswerflag",Aanswer)
                                    answer=answer.replace("Banswerflag",Banswer)
                                    answer=answer.replace("Canswerflag",Canswer)
                                    answer=answer.replace("Danswerflag",Danswer)
                                    #写入正确答案
                                    trueanswer=trueanswer.replace("trueanswerflag",t)
                                    f.write(answer)
                                    f.write(trueanswer)
                                    break
                            else:
                                print "sorry,can not find answer"
                                AllFlag==1
                                break
    
                        #初始化答案解析index
                        analyzefirstindex=answerlastindex+1
                        analyzerlastindex=0
                        tempindex=answerlastindex-1
                        while AllFlag==0:
                            tempindex+=1
                            if tempindex<len(self.templist):
                                #找到“数字”开头，上面全是答案解析
                                pattern = re.compile(r'(\d)\..*')
                                match = pattern.match(self.templist[tempindex].encode('utf-8'))
                                #打印题目
                                analyze='''
                <analyze>
                    <![CDATA[analyzeflag]]>
                </analyze>
            </question>'''
                                if match:
#                                     print "OK ,find next question",tempindex
                                    #获取到题目最后一行index=tempindex-1，下面range这里不减一
                                    analyzerlastindex=tempindex
#                                     print "first is:",analyzefirstindex,"last is:",analyzerlastindex
                                    s=""
                                    for m in range(analyzefirstindex,analyzerlastindex):
                                        if m!=(analyzerlastindex-1):
                                            s+=self.templist[m].encode('utf-8')+"\n"
                                        else:
                                            #处理最后一行不带回车
                                            s+=self.templist[m].encode('utf-8')
                                    #写入答案
                                    analyze=analyze.replace("analyzeflag",s)
                                    f.write(analyze)
                                    #递归调用，遍历其他题目，当前最后一行index=
#                                     print analyzerlastindex,"%%%%%______%%%%%%"
#                                     print "*************递归开始***************"
                                    print analyzerlastindex,"找到后最后的index"
                                    self.GreatXML(analyzerlastindex,f)
                                    AllFlag=1
                                    
#                                     print "#######################递归结束#########################"
                                    break
                            else:
                                #找不到下行数字开头，则认为是最后一行，剩下全部写入答案解析
                                print "sorry,can not find any question"
                                self.isGO=False
                                AllFlag=1
                                s=""
                                for m in range(analyzefirstindex,len(self.templist)):
                                    if m!=(analyzerlastindex-1):
                                        s+=self.templist[m].encode('utf-8')+"\n"
                                    else:
                                        #处理最后一行不带回车
                                        s+=self.templist[m].encode('utf-8')
                                #写入答案
                                analyze=analyze.replace("analyzeflag",s)
                                f.write(analyze)
                                #写入XML最后一段
                                last='''
</unit>                             '''
    
                                f.write(last)
                                print "&&&&&&&&&&&&&&解析XML结束&&&&&&&&&&&&&&"
                                break

print "中"            
my= Analyze(u"mytest.txt");
my.ReadfiletoUnicode();
f=open('unit.xml','a')
template = """<?xml version="1.0" encoding="utf-8"?>
<unit>"""
f.write(template)
my.GreatXML(0,f);
f.close()
