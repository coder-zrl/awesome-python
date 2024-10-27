from urllib import parse
key_word = input('请输入关键字：')
parses={
'keyword':key_word
}
strs=parse.urlencode(parses)
print(strs)  #word=%E9%93%B6%E8%A1%8C
print(type(strs))  #<class 'str'>
