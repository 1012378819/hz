#coding:utf-8
from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
import smtplib
import unittest
import time ,os

#---定义发送邮件---
def send_mail(file_new):
    f=open(file_new,'r+')
    mail_body=f.read()
    f.close()
    msg=MIMEText(mail_body,'html','utf-8')
    msg['Subject']=u'自动化测试报告'
    smtp=smtplib.SMTP()
    smtp.connect('smtp.163.com')
    smtp.login('yishui_lp@163.com','haoxueyishui204')
    smtp.sendmail('yishui_lp@163.com','1012378819@qq.com',msg.as_string())
    smtp.quit()
    print('email has send out!')


#---查找测试报告目录，找到最新生成的测试报告文件---
def new_report(testreport):
    lists=os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getmtime(testreport+"\\"+fn))
    file_new=os.path.join(testreport,lists[-1])
    return file_new

if __name__=='__main__':
    file_src='G:/useful/selenium+py/chongshi/test_project/test_case'
    file_des='G:/useful/selenium+py/chongshi/test_project/total_report/'
    discover=unittest.defaultTestLoader.discover(file_src,pattern='test_baidu1.py')
    now=time.strftime("%Y%m%d %H:%M:%S")
    filename=file_des+'%s result.html'%now
    fp=open(filename,'w+')
    runner=HTMLTestRunner(stream=fp,title=u'测试报告',description=u'用例执行情况')
    runner.run(discover)
    fp.close()
    newreport=new_report(file_des)
    send_mail(newreport) #发送测试报告


















