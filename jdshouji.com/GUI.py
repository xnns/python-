# -*- coding: utf-8 -*-

from 手机品牌获取 import *
from 手机型号获取 import *
from tkinter import *

a=[]
array1=[]#每个元素都代表一个品牌手机的所有信息 0iphone 1荣耀 2小米 3华为 4一加 5vivo


def windows(a,array):
    window=Tk()
    window.title("京东商城手机信息爬取结果")
    for i in range(0,len(a)):
        btn=Button(window,text=a[i],bg="lightblue")
        btn.pack()
        btn.bind("<Button-1>", handlerAdaptor(createModel,i=i))
    window.mainloop()

def handlerAdaptor(fun, **kwds):
    return lambda event,fun=fun,kwds=kwds: fun(event, **kwds)


def createModel(event,i):
    window=Tk()
    #print(i)
    global a
    #print(len(a))
    len(array1[i][3][i])
    window.title("%s手机型号信息爬取结果"%a[i])
   
    for  p in range(0,len(array1[i][0])):
        btn=Button(window,text=array1[i][0][p],bg="lightblue")
        btn.pack()
        btn.bind("<Button-1>", handlerAdaptor(showMoney, q=p,i=i))
    window.mainloop()

def showMoney(event,q,i):
    window=Tk()
    window.title("%s价格颜色及评论信息"%array1[i][0][q])
    
    money=""
    color=""
    review=""
   
    money+=array1[i][1][q]
    for p in range(0,len(array1[i][2][q])):
        color=color+"\n"+array1[i][2][q][p]
    for p in range(0,len(array1[i][3][q])):
        review=review+"\n"+array1[i][3][q][p]
    
    Label(window,text = "价格为"+money+"颜色为\n"+color+"评论为\n"+review,bg = 'yellow',width = 1000,height = 1000,wraplength = 500,anchor = 'center').pack()
    window.mainloop()

def trans(a):
    for i in range(0,len(a)):
        array1.append(search(a,len(a),choose,i))
    return array1

def main2():
    a=main()
    #print(a)
    array1=trans(a)
    windows(a,array1)
    

if __name__=="__main__":
    
    a=main()
    main2()
