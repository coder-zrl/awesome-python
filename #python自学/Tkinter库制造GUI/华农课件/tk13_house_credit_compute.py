import tkinter
from tkinter import *
from tkinter import messagebox
class MortgageCalculator:
    def __init__(self):
        win=Tk() #创建窗口对象
        win.geometry('256x192')
        win.title("使用GUI界面的简单房贷计算器") #设置窗口标题 

        lblMoney=Label(win,text="贷款金额:  ") #创建label标签
        lblMoney.grid(row=0,column=0,padx=5,pady=5,sticky="e")
        self.vMoney=IntVar(); self.vMoney.set(10000) #设初值
        entMoney=Entry(win,width=15,textvariable=self.vMoney)
        entMoney.grid(row=0,column=1,padx=5,pady=5,sticky="w")

        lblYearRate=Label(win,text="贷款年利率%： ")
        lblYearRate.grid(row=1,column=0,padx=5,pady=5,sticky="e")
        self.vYearRate=DoubleVar(); self.vYearRate.set(6.5)
        entYearRate=Entry(win,width=15,textvariable=self.vYearRate)
        entYearRate.grid(row=1,column=1,padx=5,pady=5,sticky="w")

        lblYears=Label(win,text="还款年数： ")
        lblYears.grid(row=2,column=0,padx=5,pady=5,sticky="e")
        self.vYears=IntVar(); self.vYears.set(1)
        entYears=Entry(win,width=15,textvariable=self.vYears)
        entYears.grid(row=2,column=1,padx=5,pady=5,sticky="w")

        btnCalculate=Button(win,text="计算每月还款金额",command=self.Calculate)
        btnCalculate.grid(row=3,column=0,columnspan=2,pady=5)

        lblPayment=Label(win,text="等额本息，每月应还金额")
        lblPayment.grid(row=4,column=0,padx=5,pady=5,sticky="e")
        self.vPayment=DoubleVar()
        entPayment=Entry(win,width=15,state="readonly",textvariable=self.vPayment) 
        entPayment.grid(row=4,column=1,padx=5,pady=5,sticky="w")
        win.mainloop()

    def Calculate (self):
        try:
            xMoney=float(self.vMoney.get())
            xYearRate=float(self.vYearRate.get())
            xMonthRate=xYearRate/12
            xYears=int(self.vYears.get())
            xMonths=xYears*12
            xSum=xMoney*((1+xMonthRate/100)**xMonths)/xMonths
            self.vPayment.set(round(xSum,2))
        except:
            messagebox.showerror(title="error",message="输入错误")
MortgageCalculator()