import urllib2
from bs4 import BeautifulSoup as BS
import findM
u = "file:///C:/Users/Srijan%20Chattopadhyay/Desktop/"
urls = ['cric2','cric3']
def main(url):
    page = urllib2.urlopen(url)
    soup = BS(page,"html.parser")
    text = soup.get_text()
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
    s = l1
    commons = "a all an and are as at back be been both by can here do only then each your will easy even far flat for from get has have how i in is it its me more must near next no not now of off old on one onto or real same say so some such than that the they this to two us was we were what when where which who whom why with yet you early apart fully large these often their while"
    commons = commons.split()
    tags = []
    for i in s:
        if(commons.count(i.lower()) == 0):
            tags.append([l1.count(i),i])
    tags.sort()
    tags.reverse()
    key = []
    for i in range(len(tags)):
        if len(str(tags[i][1])) >3 :
    #        print str(tags[i][1]),findM.stem(str(tags[i][1]))
            key.append(findM.stem(str(tags[i][1])))
    sk = list(set(key))
    tagsNew = []
    for i in sk:
        tagsNew.append([key.count(i),i])
    tagsNew.sort()
    tagsNew.reverse()
    return set(sk)
s = u+"cric1.html"
taglist = main(s)
for i in urls:
    s = u+i+".html"
    taglist = taglist.intersection(main(s))
print sk
