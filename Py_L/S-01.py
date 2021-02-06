# download picture using python
import requests

pic_url = 'http://attach.bbs.miui.com/forum/201304/16/165817vb5xovskxfx5exvb.jpg'
pic_s = requests.get(pic_url)
print("===================request complete======================")

with open('star2.jpg', 'wb') as f:
    f.write(pic_s.content)
