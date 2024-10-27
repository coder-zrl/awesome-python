# #-*- encoding:utf-8 -*-
# import sys   #reload()之前必须要引入模块
# reload(sys)
# sys.setdefaultencoding('utf-8')
import requests
import json
import os
from docx import Document
from docx.shared import Inches

# doc = Document()  # doc对象
for i in range(18,95):
    print(i)
    url='https://openapi.book118.com/getPreview.html?&project_id=1&aid=204530607&view_token=XY0cqObqp_8A3_OiJCnuy6gmr0knc2K9&aid_encode=5011012203002004&page='+str(6*i+1)+'&filetype=pdf'
    response=requests.get(url).text[12:-2]
    print(response)
    detail=json.loads(response)
    # print(detail)
    six_details=detail['data'].items()
    for j in six_details:
        page=j[0]
        true_url="https:"+j[1]
        print(page)
        print(true_url)
        res=requests.get(true_url).content
        filename=page+".png"
        if not filename in os.listdir('D:\PycharmProjects\道客巴巴爬虫'):
            with open(filename,'wb') as fp:
                fp.write(res)
        # doc.add_picture(page+".png")  # 添加图, 设置宽度
# doc.save("公共管理学——陈振明.doc")
