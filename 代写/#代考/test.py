#test.py
#警告：请不要对本文件做任何改动，否则可能使本题得零分
def test(fun1):
    f=open("data.in","rt")
    out = open("data.out","wt")
    for t in f.readlines():
        t=t.strip('\n') #去掉换行符
        t1 = fun1(t)#调用函数
        out.write(str(t1)+"\n")
    f.close()
    out.close()