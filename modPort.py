import enchant
dict = enchant.Dict("en-us")
def findM(s):
    v = "aeiou"
    v = list(v)
    sl = list(s)
    cnt = 0
    for i in range(len(sl)-1):
            if(v.count(sl[i])>0):
                    if(v.count(sl[i+1]) == 0):
                            cnt += 1
    return cnt
def findV(s):
    v = "aeiou"
    v = list(v)
    sl = list(s[0:-1])
    for i in v:
        if(sl.count(i) >0):
            return 1
    return 0
def dc(s):
    if(len(s)<3):
        return s
    v = "aeiou"
    v = list(v)
    if((s[-1] == s[-2]) and v.count(s[-1])==0):
        return 1
    return 0
def cvc(s):
    if(len(s)<3):
        return s
    v = "aeiou"
    v = list(v)
    cc = "wxy"
    cc = list(cc)
    if(v.count(s[-1])==0 and v.count(s[-2]) >0 and v.count(s[-3])==0 and cc.count(s[-1])==0 ):
        return 1
    return 0
def oneA(s):
    rep = [['sses','ss'],['ies','y'],['s',''],['ally',''],['lly','ll'],['ly','']]
    for i in rep:
        s1 = str(i[0])
        s2 = str(i[1])
        if(s.endswith(s1)):
            if((len(s)-len(s1)+len(s2))<3):
                return s
            s = s[0:-len(s1)]+s2
            return s
    return s
def oneB(s):
    t=s
    
    if(s.endswith("eed") and findM(t[0:-3])>0):
        t=t[0:-3]
        s=t+"ee"
        return s
    
    if(s.endswith("ed")):
        t=t[0:-2]
        if(findV(t)!=0):
            s=t
            return s
    
    if(s.endswith("ing")):
        t=t[0:-3]
        if(findV(t)!=0):
            s=t
            return s
    return s
def oneB2(s):
    rep = [['at','ate'],['bl','ble'],['iz','ize']]
    for i in rep:
        s1 = str(i[0])
        s2 = str(i[1])
        if(s.endswith(s1)):
            s = s[0:-len(s1)]+s2
            return s
    if(dc(s) !=0 and s[-1] not in ['l','s','z']):
       s = s[0:-1]
       return s
    return s
def oneC(s):
    if(s.endswith('y')):
        if(findV(s[0:-1])!=0):
            s = s[0:-1]+'i'
    return s
def two(s):
    rep = [['ational','ate'],['tional','tion'],['enci','ence'],['anci','ance'],['izer','ize'],['abli','able'],['alli','al'],['entli','ent'],['eli','e'],['ousli','ous'],['ization','ize'],['ation','ate'],['ator','ate'],['alism','al'],['iveness','ive'],['fulness','ful'],['ousness','ous'],['aliti','al'],['iviti','ive'],['biliti','ble']]
    for i in rep:
        s1 = str(i[0])
        s2 = str(i[1])
        if(s.endswith(s1)):
            t = s[0:-len(s1)]
            if(findM(t) > 0):
                s = t+s2
                return s
    return s
def three(s):
    rep = [['icate','ic'],['ative',''],['alize','al'],['iciti','ic'],['ical','ic'],['ful',''],['ness','']]
    for i in rep:
        s1 = str(i[0])
        s2 = str(i[1])
        if(s.endswith(s1)):
            t = s[0:-len(s1)]
            if(findM(s) > 1):
                s = t+s2
                return s
    return s
def four(s):
    rep = ['al','ance','ence','er','ic','able','ible','ant','ment','ent','ou','ism','ate','iti','ous','ive','ize']
    for i in rep:
        s1 = str(i)
        if(s.endswith(s1)):
            t = s[0:-len(s1)]
            if(findM(s) > 1):
                s = t
                return s
    if(s.endswith('sion') or s.endswith('tion')):
        s = s[0:-3]
        return s
    return s
def fiveA(s):
    if(s.endswith('e') and findM(s) > 1):
        s = s[0:-1]
        return s
    if(findM(s) == 1 and cvc(s)==0):
        if s.endswith('e'):
            s = s[0:-1]
            return s
    return s
def fiveB(s):
    if(findM(s)>1 and dc(s) != 0 and s.endswith('l')):
        s = s[0:-1]
        return s
    return s
def stem(s):
    roots = []
    roots.append(s)
    s = oneA(s)
    if (roots.count(s)==0):
        roots.append(s)
    s = oneB(s)
    if (roots.count(s)==0):
        roots.append(s)
    s = oneB2(s)
    if (roots.count(s)==0):
        roots.append(s)
    s = oneC(s)
    if (roots.count(s)==0):
        roots.append(s)
    s = two(s)
    if (roots.count(s)==0):
        roots.append(s)
    s = three(s)
    if (roots.count(s)==0):
        roots.append(s)
    s = four(s)
    if (roots.count(s)==0):
        roots.append(s)
    s = fiveB(s)
    if (roots.count(s)==0):
        roots.append(s)
    print roots
    for i in range(len(roots)):
        if(dict.check(roots[-1-i]) == True and len(roots[-1-i])>2):
            return roots[-1-i]
    return roots[0]
