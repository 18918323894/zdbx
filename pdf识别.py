import sys
sys.path.append("../")
from usermodules import *
from usermodules.file_operate import *
from usermodules.MyException import *
import pathlib
import fitz
import os
import traceback
print(fitz.__doc__)
print(fitz.version)
# pdf识别路径
# pdf_file= get_files_by_extension(extension_name='pdf')

def pdf2text(file_path,output_path='.'):
    """

    :param filename: 文件路径
    :return: filename.txt
    """

    if not exist_file(file_path):
        raise FileErrorException(FILE_ERROR_INFOR['FILE_NOT_FOUNT'])
    if not check_extension(file_path):
        raise FileErrorException(FILE_ERROR_INFOR['FILE_EXTESION_ERROR'])
    pdf_file =fitz.open(file_path)

    page1=pdf_file[0]
    text=page1.getText('text')
    try:
        with open(os.path.join(output_path,f'{split_path(file_path)[1]}.txt'),'wt',encoding='UTF-8') as file:
            file.write(text)
            file.close()
            pdf_file.close()
    except Exception as e:
        print(e)
        pdf_file.close()
def cvt_pdf(folderPath:str):
    # pure_Path=pathlib.Path(folderPath)

    # pdf_file=list(map(lambda x: str(x.resolve()),filter(lambda x : x.match('*.pdf') ,pathlib.Path.iterdir(pure_Path))))

    pdf_file=get_files_by_extension(folderPath,'pdf')
    for pdf in pdf_file:
        try:
            pdf2text(pdf)
        except:
            current_path = os.getcwd()
            current_path = os.path.join(current_path, 'log.txt')
            traceback.print_exc(file=open(current_path,'w+',encoding='utf-8'))
            return False
        return True