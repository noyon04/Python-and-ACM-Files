#!/usr/bin/env python
# coding: utf-8

# In[31]:


import numpy as np
def find_d(a,n):
    d=0
    sign=1
    temp=[]
    for i in range(n):
        r=small_mat(i,a,n)       
        d=d+sign*a[0][i]*r
        sign=sign*(-1)
    return d
def small_mat(m1,a,n):
    m0=0
    temp=[]
    temp2=[]
    for i in range(n):
        temp=[]
        if(i!=m0):
            for j in range(n):
                if(j!=m1):
                    temp.append(a[i][j])
            temp2.append(temp)
        
    result=temp2[0][0]*temp2[1][1]-temp2[0][1]*temp2[1][0]
    return result
def cramers_rule(a,n,x,b):
    d=find_d(a,n)
    
    tmp=[]
    a_mod=[]
    for i in range(n):
        for j in range(n):
            if(j==(x-1)):
                tmp.append(b[i])
            else:
                tmp.append(a[i][j])
        a_mod.append(tmp)
        tmp=[]
    d2=find_d(a_mod,n)
    
    result=d2/d
    return result
def main():
    #a=[[0.3,0.52,1],[0.5,1,1.9],[0.1,0.3,0.5]]
    #a=[[4,3,2],[1,3,1],[2,1,3]]
    a=[[4,3,2],[1,3,1],[2,1,3]]
    #b=[-0.01,0.67,-0.44]
    #b=[960,510,610]
    b=[960,510,610]
    n=len(a)
    x=[]
    for i in range(len(a)):
        result=cramers_rule(a,len(a),i+1,b)
        print(a[i]," = ", b[i]," ")
        x.append(round(result,5))
    print("\nX= ",x)


main()

