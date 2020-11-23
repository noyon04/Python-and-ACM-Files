#!/usr/bin/env python
# coding: utf-8

# In[19]:


import numpy as np
def elimin(a,nth,l):
    a_mod=[]
    for x in range(nth+1):
        a_mod.append(a[x])
    temp1=a[nth]
    j=nth+1
    while(j<len(a)):
        temp2=a[j]
        l[j][nth]=temp2[nth]/temp1[nth]
        temp3=[i * (temp2[nth]/temp1[nth]) for i in temp1]
        temp2=[x1 - x2 for (x1, x2) in zip(temp2 ,temp3)]
        a_mod.append(temp2)
        j=j+1
    return a_mod,l
def forward(a,l):
    for i in range(len(a)):
        a,l=elimin(a,i,l)
    return a,l
def main():
    a=[[3,-0.1,-0.2],[0.1,7,-0.3],[0.3,-0.2,10]]
    #a=[[3,2],[-1,2]]
    l=np.identity(len(a[0]))
    a,l=forward(a,l)
    print('after decomposition\n U\n',np.array(a),'\nL\n',l)
main()

