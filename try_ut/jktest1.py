#-*-coding:utf-8 -*-
import requests
import xlrd,requests,MySQLdb,time,sys
from xlutils import copy # 从xlutils模块中导入copy这个函数

def readExcel(file_path):
    try:
        book=xlrd.open_workbook(file_path) # 打开文件读取数据
    except Exception as e:
        print('路径不在或Excel不正确')
        return e
    else:
        sheet=book.sheet_by_index(0) #通过索引顺序获取第一个sheet页
        rows=sheet.nrows #取这个sheet页所有行
        case_list=[] #保存每一条case
        for i in range(rows):
            if i!=0:
                case_list.append(sheet.row_values(i))
            interfaceTest(case_list,file_path)

def interfaceTest(case_list,file_path):
    res_flags=[]#存测试结果的list
    request_urls=[]#存请求报文的list
    responses=[]#存返回报文的list
    for case in case_list:
        try:
            product=case[0]
            case_id=case[1]
            interface_name=case[2]
            case_detail=case[3]
            method=case[4]
            url=case[5]
            param=case[6]
            res_check=case[7]
            tester=case[10]
        except Exception as e:
            return '测试用例格式不正确！%s'%e
        if param=='':
            new_url=url
            request_urls.append(new_url)
        else:
            new_url=url+'?'+urlParam(param)
            request_urls.append(new_url)
        if method.upper()=='GET':
            print(new_url)
            results=requests.get(new_url).text
            print(results)
            responses.append(results)
            res=readRes(results,res_check)
        else:
            results=requests.post(new_url).text
            responses.append(results)
            res=readRes(results,res_check)
        if 'pass' in res:
            res_flags.append('pass')
        else:
            res_flags.append('fail')
            # writeBug(case_id,interface_name,new_url,results,res_check)
    copy_excel(file_path,res_flags,request_urls,responses)

def urlParam(param):
    return param.replace(';','&')

def readRes(res,res_check):
    res=res.replace('":"','=').replace('":','=')
    res_check=res_check.split(';')
    for s in res_check:
        if s in res:
            pass
        else:
            return u'错误，返回参数和预期结果不一致'+str(s)
    return 'pass'

def copy_excel(file_path,res_flags,request_urls,responses):
    book=xlrd.open_workbook(file_path)
    new_book=copy.copy(book)
    sheet=new_book.get_sheet(0)#然后获取到这个复制的excel的第一个sheet页
    i=1
    for request_urls,responses,flag in zip(request_urls,responses,res_flags):
        sheet.write(i,8,u'%s'%request_urls)
        sheet.write(i,9,u'%s'%responses)
        sheet.write(i,11,u'%s'%flag)
        i=i+1
        new_book.save(u'%s_测试结果.xls'%time.strftime('%Y%m%d%H%M%S'))

def writeBug(bug_id,interface_name,request,response,res_check):
    bug_id=bug_id.encode('utf-8')
    interface_name=interface_name.encode('utf-8')
    res_check=res_check.encode('utf-8')
    response=response.encode('utf-8')
    requests=requests.encode('utf-8')
    now=time.strftime("%Y-%m-%d %H:%M:%S")
    bug_title=bug_id+'_'+interface_name+'_结果和预期不符'
    step='[请求报文]<br />'+requests+'<br />'+'[预期结果]<br />'+res_check+'<br />'+'[响应报文]<br />'+'<br />'+requests
    sql=""
    conn=MySQLdb.connect(user='root',passwd='123456',db='bugfree',port=3307,host='192.168.1.101',charset='utf8')
    cursor=conn.cursor()
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()

if __name__=='__main__':
    try:
        filename=sys.argv[1]
    except IndexError as e:
        print('Please enter a correct testcase! \n e.x: python jktest1.py test_case1.xls')
    else:
        readExcel(filename)
    print('Done!')




