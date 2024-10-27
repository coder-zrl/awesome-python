list1=['张华,’韩冠浩’,’刘斯,李弘,’关申海','李晓思','李思慧','刘潇斯','刘斯']
list1.append('张瀚')
for i in range(len(list1)):
    if list1[i]=='李弘':
        list1[i]='李泓'
        break
list1=list(set(list1))