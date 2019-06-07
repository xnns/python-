import urllib.request
import urllib.parse
import re
import random

ip=['123.122.154.20','58.247.127.145','183.129.207.89','219.245.3.4']
url="https://shouji.jd.com/"

def hide():
    proxy_suport=urllib.request.ProxyHandler({'http':random.choice(ip)})
    head={}
    head [ 'User-Agent']: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763'
    opener=urllib.request.build_opener(proxy_suport)
    opener.addheaders=[( 
   'User-Agent',' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763')]
    urllib.request.install_opener(opener)
    return head

def choose(html):
   s= re.findall(r'menu:\[\{(.*)\}\]',html)
   s= re.findall(r"children\:\[\{(.*)",s[0])
   s= re.findall("NAME: '(.{4,6})",s[0])
   #print(s)
   a=[]
   for i in range(0,6):
       #a=re.search("'.'",s[i])
       s[i]=re.search("((.*)')|(.*)",s[i]).group()
       a.append(s[i])
   #print(a)
   return a

def download(head):
    hide()
    response=urllib.request.urlopen(url)
    html=response.read().decode("gb2312")
   #print(html)
    return html

def main():
    head=hide()
    html= download(head)
    a= choose(html)
    print("         京东商城手机信息爬取工程        ")
    return a


if __name__=="__main__":
    main()
