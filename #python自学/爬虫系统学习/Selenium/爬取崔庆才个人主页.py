from selenium import webdriver
import xlwt
import time
import re
def go_down(n):
    for i in range(n):
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")  # 先下滑到底    0代表坐标
        time.sleep(0.3)



#驱动谷歌浏览器
driver = webdriver.Chrome()
driver.get('https://cuiqingcai.com/author/cqcre')
go_down(20)

try:
    while 1:
        inputTag = driver.find_element_by_class_name("ias_trigger")
        inputTag.click()
        time.sleep(1)
        go_down(5)
except:
    pass

#拿到html数据
data = driver.page_source
driver.quit()
titles=re.findall('title=".*?">(.*?)  </a></h2>',data)
urls=re.findall('</a><h2><a target="_blank" href="(.*?)"',data)
workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('test')

detaildata=list(zip(titles,urls))
detaildata.sort()
print(detaildata)
row=0
for i in detaildata:
    worksheet.write(row,0,i[0])
    worksheet.write(row, 1,i[1])
    row+=1
workbook.save('excelwrite.xls')

