import tkinter
from tkinter import messagebox

root=tkinter.Tk()
root.geometry('256x192')
root.title('窗口LI')

def show():
    str1=''
    for i in range(len(list1)+1): #从第1行第0列开始， 每行取20个字符
        str1+=t.get(str(i+1)+'.0',str(i+1)+'.20')+'\n'
    messagebox.showinfo(title='文本框获得信息',message=str1)

t=tkinter.Text(root,width=40,height=10) #创建Text文本框
t.insert(1.0,'三门程序设计课程\n') #1.0表示第1行第0列位置写入内容
                                  #注意0行空着保留不用
list1=['C++','Python','Java']
for i in range(len(list1)):
    t.insert(str(i+2) +'.0',list1[i]+'\n') #从第2行第0列开始
t.pack()
b=tkinter.Button(root,text='获取文本框内容',width=15,height=1,command=show).pack()
root.mainloop()