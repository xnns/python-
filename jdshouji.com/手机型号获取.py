# -*- coding: utf-8 -*-

from 手机品牌获取 import *
import urllib.request
import urllib.parse
import sys
import urllib.parse
import re

url1=" https://search.jd.com/Search?keyword=%s&enc=utf-8"
rv=[]#存储所有评论

def CreateData():
    data={}

    data['Accept']: '*/*'
    data['Accept-Encoding']: 'gzip, deflate, br'
    data['Accept-Language']: 'zh-Hans-CN, zh-Hans; q=0.5'
    data['Cache-Control']:' no-cache'
    data['Connection']: 'Keep-Alive'
    data['Content-Length']:' 10034'
    data['Content-Type']: 'application/x-www-form-urlencoded; charset=UTF-8'
    data['Host']: 'gia.jd.com'
    data['Origin']: 'https://search.jd.com'
    data['Referer']:' https://search.jd.com/Search?keyword=iphone&enc=utf-8&wq=iphone&pvid=7da4e4736bd64b4590c2d71f5e3b7c37'
    data['User-Agent']: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763'
    data=urllib.parse.urlencode(data).encode("gb2312")

def search(a,length,choose,i):
        hide() 
        #print(a[i])
        a[i]=urllib.parse.quote(a[i])
        url=url1%a[i]
        response=urllib.request.urlopen(url)
        html=response.read().decode("utf-8")
        #print(type(url))
        array=pick(html,urllib.parse.unquote(a[i]),choose)
        return array

def pick(str,model,choose):
    array=[]#综合数组 序号对应信息分别为0model 1money 2color 3review
    md=[]#型号
    mn=[]#价格
    rv=[]#评论
    cl=[]#颜色
    ul=[]#url
    str=re.sub('\s',"",str)
    str1=re.findall(r'<ulclass="gl-warp.*?</div></li></ul>',str)
    #print(str1[0])
    str1=re.findall(r'gl-item.*?</div></div></li>',str1[0])
    for i in range(0,len(str1)):
         #print('')
         #print(str1[i])
         url2=re.findall(r'//item\.jd\.com.*?html',str1[i])
         ul.append(url2[0])
         color=re.findall(r'<ahref="javascript:;.*?">',str1[i])
         cl.append(color)
         if model=="iPhone":
             money=re.findall(r'"><em>.*?.00</i>',str1[i])
             model1=re.findall(r'<fontclass=.*?</em>',str1[i])
             for p in range(0,len(model1)):
                 money[p]=money[p][6:7]+money[p][-10:-4]
                 model1[p]=model1[p][25:31]+model1[p][38:-5]
         elif model=="华为'":
             money=re.findall(r'price.*?</i>',str1[i])
             model1=re.findall(r'<atarget.*?href',str1[i])
             for p in range(0,len(model1)):
                 #money[p]=money[p][6:7]+money[p][-10:-4]
                 model1[p]=model1[p][25:31]+model1[p][38:-5]
         elif model=="荣耀'":
             money=re.findall(r'price.*?</i>',str1[i])
             model1=re.findall(r'<atarget.*?href',str1[i])
             for p in range(0,len(model1)):
                # money[p]=money[p][6:7]+money[p][-10:-4]
                 model1[p]=model1[p][25:31]+model1[p][38:-5]
         elif model=="小米'":
             money=re.findall(r'price.*?</i>',str1[i])
             model1=re.findall(r'<atarget.*?href',str1[i])
         elif model=="一加'":
             money=re.findall(r'price.*?</i>',str1[i])
             model1=re.findall(r'<atarget.*?href',str1[i])
             for p in range(0,len(model1)):
                 #money[p]=money[p][6:7]+money[p][-10:-4]
                 model1[p]=model1[p][25:31]+model1[p][38:-5]
         elif model=="vivo'":
             money=re.findall(r'price.*?</i>',str1[i])
             model1=re.findall(r'<fontclass=.*?</em>',str1[i])
             for p in range(0,len(model1)):
                 money[p]=money[p][6:7]+money[p][-10:-4]
                 model1[p]=model1[p][25:31]+model1[p][38:-5]
         mn.append(money[0])
         md.append(model1[0])
    review=printMoney(model,md,ul,cl,mn,choose)
    #print('')
    array.append(md)
    array.append(mn)
    array.append(cl)
    array.append(review)
    return array

def printMoney(brand,model,url,color,money,choose):
    print("爬取%s数据:\n"%brand)
    
    for p in range(0,len(url)):
        print("%s 主要价格及评论: \n"%model[p])  
        print("该手机价格为 %s ，主要颜色有：\n"%money[p])
        if(p!=1):
            for i in range(0,len(color[p])):
                print(color[p][i][28:-2])
        print("")
        html=pickReview(brand,model,url,p,choose)#html中每个元素代表一条评论
        rv.append(html)#rv中每个元素代表一个型号手机的评论
    return rv

def pickReview(str1,model,url,i,choose):
    if url[i]!="//item.jd.com/100000823724.html":
        print("评论为：\n")
        #print("https:"+url[i])
        response=urllib.request.urlopen("https:"+url[i])
        html=response.read().decode("gbk")
        html=re.sub('\s',"",html)
        html=re.findall(r'<divclass="comment-content".*?</div>',html)
        #print(html)
        for p in range(0,len(html)):
            i=str(p+1)
            html[p]=i+"----"+html[p][28:-6]
        print(html)
        return html 
    else :
        pass  

def main1(choose):
    a= main()
    #print(sys.getdefaultencoding())
    for i in range(0,len(a)):
        search(a,len(a),choose,i)
    return a
    #print(url)

if __name__=="__main__":
    main1(choose)
