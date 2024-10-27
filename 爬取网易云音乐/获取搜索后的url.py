from selenium import webdriver
from lxml import etree
from urllib import parse
# key_word
parses={
's':'当'
}
strs=parse.urlencode(parses)
url='https://music.163.com/#/search/m/?'+strs+'&type=1'

driver=webdriver.Chrome()
driver.get(url)
data=driver.page_source
html=etree.HTML(data)
first_url=html.xpath()
print(data)

# headers={
#
# }
# # data={
# #
# # }
# response=requests.get(url)  # ,headers=headers,data=data
# print(response.text)