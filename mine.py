import urllib2
from bs4 import BeautifulSoup as BS
import findM
import math
import kmeans
import pca_min
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import proj3d

u = "file:///C:/Users/Srijan%20Chattopadhyay/Desktop/pages/"
##urls = ['tennis1','tennis2','tennis3','cric1','cric2','cric3','hockey1']
urls = ['c1','c2','c3','c4','c5','c6','c7','c8','c9','f1','f2','f3','f4','f5','f6','f7','f8','k1','k2','k3','k4','k5','k6','k7']
def findtags(url):
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
    return tagsNew


def termfreq(url,taglist):
    page = urllib2.urlopen(url)
    soup = BS(page,"html.parser")
    text = soup.get_text()
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
    freq = []
    key = []
    for i in range(len(tags)):
        if len(str(tags[i][1])) >3 :
            key.append(findM.stem(str(tags[i][1])))
    for i in taglist:
        freq.append(key.count(i))
    return len(key),freq

def plot(pts):
##    print pts
    fig = plt.figure(figsize=(8,8))
    ax = fig.add_subplot(111, projection='3d')
    plt.rcParams['legend.fontsize'] = 10
    colors = ['blue','red','green']
    for i in range(len(pts)):
        ax.plot(pts[i][:,0], pts[i][:,1], pts[i][:,2],'o', markersize=8, color=colors[i%3], alpha=0.5, label='class'+str(i))
    plt.title('Clusters')
    ax.legend(loc='upper right')
    plt.show()


    
s = u+urls[0]+".html"
taglist = findtags(s)
for i in urls[1:]:
    s = u+i+".html"
##    print s
    taglist += findtags(s)
tagnum , tag_list = zip(*taglist)
s = list(set(tag_list))
tags = [[0,i] for i in s]
for i in range(len(tags)):
    t = tags[i][1]
    num = 0
    for j in range(len(taglist)):
        if(taglist[j][1]==t):
            num += taglist[j][0]
    tags[i][0] = num
tags.sort()
tags.reverse()
tagnum , taglist = zip(*tags)
taglist = taglist[0:50]
print taglist
tf = []
idf = [0 for i in range(len(taglist))]
for i in urls:
    total,terms = termfreq(u+i+".html",taglist)
##    print total,terms
    temp = []
    for j in range(len(taglist)):
        temp.append(float(terms[j])/float(total))
        if(terms[j]>0):
            idf[j] += 1
    tf.append(temp)
for j in range(len(taglist)):
    if(len(urls)>0):
        idf[j] = float(idf[j])/float(len(urls))
        if(idf[j]==0):
            idf[j] = -10
        else:
            idf[j] = math.log(idf[j])
for i in range(len(urls)):
    for j in range(len(taglist)):
        tf[i][j] *= idf[j]

t = np.array(tf)
t = t.transpose()
mat,trans = pca_min.pca(t,3)
plot([trans[:9],trans[9:17],trans[17:]])
#print mat
#print trans
##m,r,a = kmeans.k_means(np.array(tf),2)
##print r,a
##c0 = np.array([[trans[i][0],trans[i][1],trans[i][2]] for i in range(len(trans)) if a[i]==0])
##c1 = np.array([[trans[i][0],trans[i][1],trans[i][2]] for i in range(len(trans)) if a[i]==1])
##plot([c0,c1])
m,r,a = kmeans.k_means(np.array(trans),3)
for i in range(10):
    m1,r1,a1 = kmeans.k_means(np.array(trans),3)
    print r1,a1
    if(r1<r):
        m = m1
        r = r1
        a = a1
print r,a
c0 = np.array([[trans[i][0],trans[i][1],trans[i][2]] for i in range(len(trans)) if a[i]==0])
c1 = np.array([[trans[i][0],trans[i][1],trans[i][2]] for i in range(len(trans)) if a[i]==1])
c2 = np.array([[trans[i][0],trans[i][1],trans[i][2]] for i in range(len(trans)) if a[i]==2])
plot([c0,c1,c2])
