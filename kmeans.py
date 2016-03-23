import numpy as np
from matplotlib import pyplot as plt
import random
import math

pts = np.array([[.1,.1,0],[.9,.6,0],[.2,.2,0],[.4,.3,10],[.5,.2,0],[.4,.1,0],[.6,.7,10],[.6,.8,0],[.8,.6,10],[.7,.6,10],[.8,.7,0],[.3,.3,0],[.6,.9,0]])
def dist(p1,p2):
    d = 0
    for i in range(len(p1)):
        d += (p1[i]-p2[i])**2
    return d
def k_means(pts,k):
    means = []
    temp = list(pts.copy())
    l = len(temp)
    for i in range(k):
        r = random.randint(0,l-1)
        means.append(temp.pop(r))
        l = l-1
##    print means
    iter = 0
    prev_rss = 0
    while(1):
        assocmeans = []
        nums = [0 for k in range(len(means))]
        sums = [[0 for l in range(len(means[0]))] for k in range(len(means))]
        for i in range(len(pts)):
            min = dist(pts[i],means[0])
            prefmin = 0
            for j in range(1,len(means)):
                min1 = dist(pts[i],means[j])
                if(min1 < min):
                    min = min1
                    prefmin = j
            assocmeans.append(prefmin)
            nums[prefmin]+= 1
            for k in range(len(pts[0])):
                sums[prefmin][k] += pts[i][k]
##        print assocmeans
        #print nums,sums
        for j in range(len(means)):
            if(nums[j]>0):
                for k in range(len(pts[0])):
                    means[j][k]  = sums[j][k]/nums[j]
        rss = 0
        for i in range(len(pts)):
            rss += dist(pts[i],means[assocmeans[i]])
##        print rss
##        print means
        iter += 1
        if(iter>10 or abs(rss-prev_rss)<0.001):
            break
        prev_rss = rss
    return means,rss,assocmeans
k_means(pts,2)
k_means(pts,3)
k_means(pts,4)
        
        
    
