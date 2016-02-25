import urllib2
import modPort1
from bs4 import BeautifulSoup as BS
import re
page = urllib2.urlopen("http://www.espncricinfo.com/blogs/content/story/906441.html")
s = str(page.readlines())
s = re.sub("<script.*?/script>"," ",s)
s = re.sub("<style.*?/style>"," ",s)
#soup = BS(page,"html.parser")
text = re.sub("<.*?>"," ",s)
exp = ['\n','\r','\t']
for c in exp:
    text = text.replace(c,' ')
specials = ['!','@','#','$','%','^','&','*','(',')','-','_','+','=','\\','|',']','}','[','{',';','.',',','/','?',':','~']
for i in specials:
    text = text.replace(i,' ')
l = text.split()
l1 = []
for i in l:
    if i.isalpha():
        l1.append(i.lower())
s = list(set(l1))
key=[]
keys = []
cnt = 0
for i in s:
    if(len(i)>3):
        st = modPort1.stem(i)
        key.append(st)
        keys.append([l1.count(i),st])
        if(i != st):
            cnt += 1
        print cnt,i,st

words=list(set(key))
#for i in words:
#    print i



measure=(float)(len(words))/(float)(len(s))
print measure
print len(key),len(words),cnt
    
    
