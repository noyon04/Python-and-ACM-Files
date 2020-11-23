#!/usr/bin/env python
# coding: utf-8

# In[38]:


import numpy as np
def iteration(a,nth,b,t_x,ea,t_rel,lamda,x2,relax):
    if(lamda!=0):
        temp2=t_rel
    else:
        temp2=t_x
    temp=b[nth]
    for i in range(len(a[nth])):
        if(i!=nth):
            if(lamda!=0):
                temp=temp-a[nth][i]*relax[i]
            else:
                temp=temp-a[nth][i]*x2[i]
    temp=temp/a[nth][nth]
    if(lamda!=0):
        t_rel=round((lamda*temp)+((1-lamda)*temp2),5)
    t_x=round(temp,5)
    if(lamda!=0):
        ea[nth]=abs(round((((t_rel-temp2)/t_rel)*100),3))
    else:
        ea[nth]=abs(round((((t_x-temp2)/t_x)*100),3))
    return t_x,ea,t_rel
def main():
    #a=[[3,-0.1,-0.2],[0.1,7,-0.3],[0.3,-0.2,10]]
    #a=[[0.8,-0.4,0],[-0.4,0.8,-0.4],[0,-0.4,0.8]]
    a=[[4,3,2],[1,3,1],[2,1,3]]

    #b=[7.85,-19.3,71.4]
    #b=[41,25,105]
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
        temp2_x=[]
        temp2_rel=[]
        for i in range(len(a[0])):
            temp_x,ea,temp_rel=iteration(a,i,b,x[i],ea,relax[i],lamda,x,relax)
            temp2_x.append(temp_x)
            temp2_rel.append(temp_rel)
        x=temp2_x
        relax=temp2_rel
        for i in range(len(ea)):
            if(ea[i]<es):
                count=count+1
        if(lamda!=0):
            print("\nAfter iteration no "+str(itr),"\nx= ",x,"\nAfter relaxation X= ",relax," \nEA= ",ea)
        else:
            print("\nAfter iteration no "+str(itr),"\nx= ",x," \nEA= ",ea)
main()

