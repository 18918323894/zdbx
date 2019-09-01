import pathlib
import re
p=pathlib.Path(r'C:\Users\MEACH\project\报销自动化')
a=list(map(lambda x:str(x.resolve()),filter(lambda x:not x.is_dir(),p.iterdir())))
print(list(filter(lambda x:pathlib.Path(x).match('*.txt'),a)))