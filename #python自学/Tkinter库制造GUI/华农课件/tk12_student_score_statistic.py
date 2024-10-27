import tkinter
from tkinter import *
from tkinter import messagebox

class CalStdScore:
    def __init__(self):
        win=Tk()
        win.geometry('256x192')
        win.title('统计学生成绩')
    
        lblCpp=Label(win,text='c++程序设计') #创建标签
        lblCpp.grid(row=0,column=0,padx=5,pady=5,sticky='e')
        self.vCppScore=IntVar() #使用self创建文本框
        entCpp=Entry(win,width=15,textvariable=self.vCppScore)
        entCpp.grid(row=0,column=1,padx=5,pady=5,sticky='w')

        lblPython=Label(win,text='Python程序设计') #创建标签
        lblPython.grid(row=1,column=0,padx=5,pady=5,sticky='e')
        self.vpythonScore=IntVar() #使用self创建文本框
        entPython=Entry(win,width=15,textvariable=self.vpythonScore)
        entPython.grid(row=1,column=1,padx=5,pady=5,sticky='w')

        lblJava=Label(win,text='Java程序设计') #创建标签
        lblJava.grid(row=2,column=0,padx=5,pady=5,sticky='e')
        self.vJavaScore=IntVar() #使用self创建文本框
        entJava=Entry(win,width=15,textvariable=self.vJavaScore)
        entJava.grid(row=2,column=1,padx=5,pady=5,sticky='w')

        lblW=Label(win,text='物联网工程') #创建标签
        lblW.grid(row=3,column=0,padx=5,pady=5,sticky='e')
        self.vWScore=IntVar() #使用self创建文本框
        entW=Entry(win,width=15,textvariable=self.vWScore)
        entW.grid(row=3,column=1,padx=5,pady=5,sticky='w')
 
        btnCalculate=Button(win,text='统计学生成绩',command=self.Calculate,width=15,height=1)
        btnCalculate.grid(row=4,column=0,columnspan=2,pady=5)
        win.mainloop()#显示面体并无限监听事件循环
    
    def Calculate(self):
        try:
            xCppScore=int(self.vCppScore.get())
            xpythonScore=int(self.vpythonScore.get())
            xJavaScore=int(self.vJavaScore.get())
            xWScore=int(self.vWScore.get())
            xAvgScore=(xCppScore+xpythonScore+xJavaScore+xWScore)/4
            str1='ave: '+str(xAvgScore)+'\n'
            messagebox.showinfo(title="成绩统计",message=str1)
        except:
            messagebox.showinfo(title='提示',message='输入错误')
CalStdScore()