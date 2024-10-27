#xpath提取后为列表，用循环可以显示每个元素的文字
from lxml import etree
for tr in trs:
    print(etree.tostring(tr.encoding('utf-8').decoding('utf-8')))
#有时候，xpath提取的是文字，本身为str类型，只需要按xpath语法即可，用//div/a/text()就行