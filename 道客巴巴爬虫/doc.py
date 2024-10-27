from docx import Document
from docx.shared import Inches

doc = Document()  # doc对象
for page in range(1,188):
    doc.add_picture(str(page)+".png",width=Inches(6.5))  # 添加图, 设置宽度

doc.save("公共管理学——陈振明.doc")