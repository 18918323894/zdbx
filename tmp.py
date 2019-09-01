import base64
imageBase64=''
with open(r'C:\Users\MEACH\project\bxzdh-master\bxzdh-master\图片识别\Photo_1005_1a.jpg',"rb") as f:
    imageBase64=base64.b64encode(f.read())
    with open('1.txt','wb') as f:
        f.write(imageBase64)