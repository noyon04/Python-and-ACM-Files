#!/usr/bin/env python
# coding: utf-8

# In[143]:


import numpy as np
def iteration(a,nth,b,x,ea,relax,lamda):
    if(lamda!=0):
        temp2=relax[nth]
    else:
        temp2=x[nth]
    temp=b[nth]
    for i in range(len(a[nth])):
        if(i!=nth):
            if(lamda!=0):
                temp=temp-a[nth][i]*relax[i]
            else:
                temp=temp-a[nth][i]*x[i]
    temp=temp/a[nth][nth]
    if(lamda!=0):
        relax[nth]=round((lamda*temp)+((1-lamda)*temp2),5)
    x[nth]=round(temp,5)
    if(lamda!=0):
        ea[nth]=abs(round((((relax[nth]-temp2)/relax[nth])*100),3))
    else:
        ea[nth]=abs(round((((x[nth]-temp2)/x[nth])*100),3))
    return x,ea,relax
def main():
    #a=[[3,-0.1,-0.2],[0.1,7,-0.3],[0.3,-0.2,10]]
    #a=[[0.8,-0.4,0],[-0.4,0.8,-0.4],[0,-0.4,0.8]]
    #a=[[15,-3,-1],[-3,18,-6],[-4,-1,12]]
    a=[[4,3,2],[1,3,1],[2,1,3]]
    #b=[7.85,-19.3,71.4]
    #b=[41,25,105]
    #b=[3300,1200,2400]
    b=[960,510,610]

    x=[0 for i in range(len(b))]
    ea=[0 for i in range(len(b))]
    es=5 #error limit for all x
    lamda=0
    relax=[0 for i in range(len(b))]
    count=0
    itr=0
    while(count<3):
        count=0
        itr=itr+1
        for i in range(len(a)):
            x,ea,relax=iteration(a,i,b,x,ea,relax,lamda)
        for i in range(len(ea)):
            if(ea[i]<es):
                count=count+1
        if(lamda!=0):
            print("\nAfter iteration no "+str(itr),"\nx= ",x,"\nAfter relaxation X= ",relax," \nEA= ",ea)
        else:
            print("\nAfter iteration no "+str(itr),"\nx= ",x," \nEA= ",ea)
main()

