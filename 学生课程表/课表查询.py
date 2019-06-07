from tkinter import *
infile=open("curriculum.txt",'r')
for line in infile:
    listVar=[line.rstrip() for line in infile]
infile.close()

      
def Class_time(i):
 if(i==0):  return "8:00-8:40" 
 elif (i==1): return "8:50-9:30"
 elif(i==2): return "9:40-10:20"
 elif(i==3): return "10:30-11:10"
 elif(i==4): return "11:20-12:00"
 elif(i==5): return "12:10-12:50"

 
def Show_time1():
     print("第一节课：8:00-8:40\n")
def Show_time2():
    print( "第二节课：8:50-9:30\n")
def Show_time3():
    print("第三节课：9:40-10:20\n")
def Show_time4():
    print("第四节课：10:30-11:10\n")
def Show_time5():
    print("第五节课：11:20-12:00\n")
def Show_time6():
   print("第六节课：12:10-12:50\n")

def print_1():
    print("第",1,"节课:\n",listVar[0][4:],"上课时间:",Class_time(0))
    print('\n')

def print_2():
    print("第",2,"节课:\n",listVar[1][4:],"上课时间:",Class_time(1))
    print('\n')

def print_3():
    print("第",3,"节课:\n",listVar[2][4:],"上课时间:",Class_time(2))
    print('\n')

def print_4():
    print("第",4,"节课:\n",listVar[3][4:],"上课时间:",Class_time(3))
    print('\n')

def print_5():
    print("第",5,"节课:\n",listVar[4][4:],"上课时间:",Class_time(4))
    print('\n')

def print_6():
    print("第",6,"节课:\n",listVar[5][4:],"上课时间:",Class_time(5))
    print('\n')
   
def Print_1():
    for i in range(6):
      print(listVar[i][4:6],"(第",i+1,"节)","上课时间:",Class_time(i))
    if(i==5):print('\n')  
      

def Print_2():
    for i in range(6):
        print(listVar[i][7:9],"(第",i+1,"节)","上课时间:",Class_time(i))
    if(i==5):print('\n')  
       

def Print_3():
    for i in range(6):
        print(listVar[i][10:12],"(第",i+1,"节)","上课时间:",Class_time(i))
    if(i==5):print('\n')   
       

def Print_4():
    for i in range(6):
        print(listVar[i][13:15],"(第",i+1,"节)","上课时间:",Class_time(i))
    if(i==5):print('\n')


def Print_5():
   for i in range(6):
        print(listVar[i][16:18],"(第",i+1,"节)","上课时间:",Class_time(i))
   if(i==5):print('\n')   
       

def show_Chinese():
    for line in range(0,6):
        for i in range(0,5):
            if listVar[line][4+3*i:6+3*i]=="语文":
                print("time:第",line+1,"节，星期",i+1)

def show_Math():
    for line in range(0,6):
        for i in range(0,5):
           if listVar[line][4+3*i:6+3*i]=="数学":
                print("time:第",line+1,"节，星期",i+1)


def show_English():
    for line in range(0,6):
        for i in range(0,5):
           if listVar[line][4+3*i:6+3*i]=="英语":
                print("time:第",line+1,"节，星期",i+1)     
                
def show_Physics():
    for line in range(0,6):
        for i in range(0,5):
           if listVar[line][4+3*i:6+3*i]=="物理":
                print("time:第",line+1,"节，星期",i+1)

def show_Chemistry():
    for line in range(0,6):
        for i in range(0,5):
           if listVar[line][4+3*i:6+3*i]=="化学":
                print("time:第",line+1,"节，星期",i+1)

def show_History():
    for line in range(0,6):
        for i in range(0,5):
           if listVar[line][4+3*i:6+3*i]=="历史":
                print("time:第",line+1,"节，星期",i+1)

def show_Biology():
    for line in range(0,6):
        for i in range(0,5):
           if listVar[line][4+3*i:6+3*i]=="生物":
                print("time:第",line+1,"节，星期",i+1)


window=Tk()
window.title("17班 2018-2019第一学期课程表")
btnCurriculum1=Button(window,text="星期一",command=Print_1)
btnCurriculum1.grid(sticky=E,column=1,row=1,padx=10)
btnCurriculum2=Button(window,text="星期二",command=Print_2)
btnCurriculum2.grid(sticky=W,column=2,row=1,padx=10)
btnCurriculum3=Button(window,text="星期三",command=Print_3)
btnCurriculum3.grid(sticky=W,column=3,row=1,padx=10)
btnCurriculum4=Button(window,text="星期四",command=Print_4)
btnCurriculum4.grid(sticky=W,column=4,row=1,padx=10)
btnCurriculum5=Button(window,text="星期五",command=Print_5)
btnCurriculum5.grid(sticky=W,column=5,row=1,padx=10)

btnCurriculum9=Button(window,text="第一节",bg="light green",command=print_1)
btnCurriculum9.grid(sticky=S,column=0,row=3,pady=10)
btnCurriculum10=Button(window,text="第二节",bg="light green",command=print_2)
btnCurriculum10.grid(sticky=N,column=0,row=4,pady=10)
btnCurroculum11=Button(window,text="第三节",bg="light green",command=print_3)
btnCurroculum11.grid(sticky=N,column=0,row=5,pady=10)
btnCurroculum12=Button(window,text="第四节",bg="light green",command=print_4)
btnCurroculum12.grid(sticky=N,column=0,row=6,pady=10)
btnCurroculum13=Button(window,text="第五节",bg="light green",command=print_5)
btnCurroculum13.grid(sticky=N,column=0,row=7,pady=10)
btnCurroculum14=Button(window,text="第六节",bg="light green",command=print_6)
btnCurroculum14.grid(sticky=N,column=0,row=8,pady=10)
btnCurriculum=Label(window,text="课程名:",bg="light yellow")
btnCurriculum.grid(padx=50,pady=50)

time0=Label(window,text="时间查询:",bg="pink")
time0.grid(sticky=N,column=0,row=11,pady=10)
time1=Button(window,text="第一节",bg="purple",command=Show_time1)
time1.grid(sticky=S,column=1,row=11,pady=10)
time1=Button(window,text="第二节",bg="purple",command=Show_time2)
time1.grid(sticky=S,column=2,row=11,pady=10)
time1=Button(window,text="第三节",bg="purple",command=Show_time3)
time1.grid(sticky=S,column=3,row=11,pady=10)
time1=Button(window,text="第四节",bg="purple",command=Show_time4)
time1.grid(sticky=S,column=4,row=11,pady=10)
time1=Button(window,text="第五节",bg="purple",command=Show_time5)
time1.grid(sticky=S,column=5,row=11,pady=10)
time1=Button(window,text="第六节",bg="purple",command=Show_time6)
time1.grid(sticky=S,column=6,row=11,pady=10)

lesson1=Button(window,text="语文",bg="brown",command=show_Chinese)
lesson1.grid(column=1,row=9,pady=10)
lesson2=Button(window,text="数学",bg="brown",command=show_Math)
lesson2.grid(column=2,row=9,pady=10)
lesson3=Button(window,text="英语",bg="brown",command=show_English)
lesson3.grid(column=3,row=9,pady=10)
lesson4=Button(window,text="物理",bg="brown",command=show_Physics)
lesson4.grid(column=4,row=9,pady=10)
lesson5=Button(window,text="化学",bg="brown",command=show_Chemistry)
lesson5.grid(column=5,row=9,padx=10)
lesson6=Button(window,text="生物",bg="brown",command=show_Biology)
lesson6.grid(column=6,row=9,padx=10)
lesson7=Button(window,text="历史",bg="brown",command=show_History)
lesson7.grid(column=7,row=9,padx=10)
window.mainloop()


import tkinter as tk
from tkinter import messagebox
class Choose_Curriculum(tk.Frame):
    def __init__(self,master=None):
        tk.Frame.__init__(self,master)
        self.grid()
        self.creatWidgets()
    def creatWidgets(self):
        self.lbTitle=tk.Label(self,text="综合查询")
        self.lbdate=tk.Label(self,text="星期")
        self.lblessons=tk.Label(self,text="第几节")
        self.lbTitle.grid(row=0,column=0,columnspan=6)
        self.lbdate.grid(row=2,column=0)
        self.lblessons.grid(row=3,column=0)
        self.vdate=tk.IntVar()
        self.vdate.set(1)
        self.vdate1=tk.Radiobutton(self,text="星期一",value=1,variable=self.vdate)
        self.vdate2=tk.Radiobutton(self,text="星期二",value=2,variable=self.vdate)
        self.vdate3=tk.Radiobutton(self,text="星期三",value=3,variable=self.vdate)
        self.vdate4=tk.Radiobutton(self,text="星期四",value=4,variable=self.vdate)
        self.vdate5=tk.Radiobutton(self,text="星期五",value=5,variable=self.vdate)
        self.vdate1.grid(row=2,column=1)
        self.vdate2.grid(row=2,column=2)
        self.vdate3.grid(row=2,column=3)
        self.vdate4.grid(row=2,column=4)
        self.vdate5.grid(row=2,column=5)
        self.vlessons=tk.IntVar()
        self.vlessons.set(1)
        self.vlesson1=tk.Radiobutton(self,text="第一节",value=1,variable=self.vlessons)
        self.vlesson2=tk.Radiobutton(self,text="第二节",value=2,variable=self.vlessons)
        self.vlesson3=tk.Radiobutton(self,text="第三节",value=3,variable=self.vlessons)
        self.vlesson4=tk.Radiobutton(self,text="第四节",value=4,variable=self.vlessons)
        self.vlesson5=tk.Radiobutton(self,text="第五节",value=5,variable=self.vlessons)
        self.vlesson6=tk.Radiobutton(self,text="第六节",value=6,variable=self.vlessons)
        self.vlesson1.grid(row=3,column=1)
        self.vlesson2.grid(row=3,column=2)
        self.vlesson3.grid(row=3,column=3)
        self.vlesson4.grid(row=3,column=4)
        self.vlesson5.grid(row=3,column=5)
        self.vlesson6.grid(row=3,column=6)
        self.btnOk=tk.Button(self,text="确定",command=self.funOK)
        self.btnOk.grid(row=4,column=1,sticky=tk.E)
        self.btnCancel=tk.Button(self,text="取消",command=root.destroy) 
        self.btnCancel.grid(row=4,column=3,sticky=tk.W)
    def funOK(self):
       strDate=""   
       if (self.vdate.get()==1): 
           strDate="星期一"
       elif(self.vdate.get()==2):strDate="星期二"
       elif(self.vdate.get()==3):strDate="星期三"
       elif(self.vdate.get()==4):strDate="星期四"
       elif(self.vdate.get()==5):strDate="星期五"
       strlesson=""
       if (self.vlessons.get()==1):strlesson="第一节" 
       elif(self.vlessons.get()==2):strlesson="第二节"
       elif(self.vlessons.get()==3):strlesson="第三节"
       elif(self.vlessons.get()==4):strlesson="第四节"
       elif(self.vlessons.get()==5):strlesson="第五节"
       elif(self.vlessons.get()==6):strlesson="第六节"
       str1=strDate+"     "
       str1=str1+strlesson+"是\n"
       str1+=listVar[self.vlessons.get()-1][4+(3*(self.vdate.get()-1)):6+(3*(self.vdate.get()-1))]
       str1+=Class_time(self.vlessons.get()-1)
       tk.messagebox.showinfo("综合查询",str1)
root=tk.Tk()
root.title("综合查询")
app=Choose_Curriculum(master=root)
app.mainloop() 
