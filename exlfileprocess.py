import pandas as pd
import win32com.client as win32
import numpy as np




# inf=['2018.8.17', '宁国路', '上海站', '地铁', '检查样机', None, None, None, None, 4.0]
# data=pd.DataFrame([['2018.8.17', '宁国路', '上海站', '地铁', '检查样机', None, None, None, None, 4.0]],index=[11],columns=list('BCDEFGHIJK'))
# data.loc[12]=inf
# print(data)
from usermodules.file_operate import *


def get_excel_dididatas(filespath,reason):
    """

    :param filespath: 文件路径数组
    :param reason:出差原因
    :return: 滴滴pdf数据整合为需要excel填写的数据
    """
    data=[]
    for filepath in filespath:
        tmp=append_data(filepath,reason)
        if not len(tmp):
            print(f'文件路径：{filepath}   无法获取报销信息')
            continue
        if not len(data):
            data=tmp
            continue
        data=np.vstack((data,tmp))
    return data


def append_data(filepath,reason):
    """
    获取每个pdf上的报销信息
    :param filespath: 文件路径
    :param reason: 出差原因
    :return: 如果没有返回空数组，如果有返回[[...]]
    """
    inf=[]
    with open(filepath,'rt',encoding='utf-8') as f:
        txt=f.read()
        f.close()
    if txt is None:
        return []
    s_tuple=txt.split('\n')
    n='1'
    b=False
    for index,i in enumerate(s_tuple):
        if len(i)>0:
            if i[0] ==n:
                
                if len(i)>1:
                    data=i.split(' ')
                    if len(data)!=10:
                        break
                    data=[data[2],data[6],data[7],"出租车",reason,"","","","",data[9]]
                    inf.append(data)
                else:
                    b=True
                n=int(n)+1
                n=str(n)
            else:              
                if b:
                    if s_tuple[index+7][0]==n:
                        data=[s_tuple[index+1][:5],s_tuple[index+3],s_tuple[index+4],"出租车",reason,"","","","",s_tuple[index+6]]
                        inf.append(data)
                        b=False
                    else:
                        b=False
    return inf
# ------------------------填写的信息--------------------------
REASON="检查样机进度"
filelist=get_files_by_extension(r'C:\Users\MEACH\project\报销自动化\pdfFolder','txt')
inf = get_excel_dididatas(filelist,REASON)
print(inf)
print(len(inf[0]))
#---------------------------excel操作---------------------------
SRT_ROW=11
END_ROW=11
excel=win32.gencache.EnsureDispatch('Excel.Application')
wb=excel.Workbooks.Open(r'C:\Users\MEACH\project\报销自动化\template.xlsx')
excel.Visible=True
ws=wb.Worksheets(1)
for data in inf:
    cell_range=f'B{SRT_ROW}:K{END_ROW}'
    print(cell_range)
    print(data)
    ws.Range(cell_range).Value=tuple(data)
    SRT_ROW+=1
    END_ROW+=1
wb.SaveAs(r'C:\Users\MEACH\project\报销自动化\4.xlsx')
excel.Application.Quit()
