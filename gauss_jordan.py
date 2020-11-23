#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np
def gauss_jordan(a,nth):
    a_mod=[]
    for x in range(nth):
        a_mod.append(a[x])
    a_mod.append([round(i / a[nth][nth],5) for i in a[nth]])
    temp1=a[nth]
    j=0
    while(j<len(a)):
        if(j!=nth):
            temp2=a[j]
            temp3=[round(i * (temp2[nth]/temp1[nth]),5) for i in temp1]
            temp2=[round(x1 - x2,5) for (x1, x2) in zip(temp2 ,temp3)]
            if(j<nth):
                a_mod[j]=temp2
            else:
                a_mod.append(temp2)
        j=j+1
        #print("\n a_modified= ",np.array(a_mod),"\n")
    return a_mod
def forward(a):
    for i in range(len(a)):
        a=gauss_jordan(a,i)
        
    return a
def main():
    #a=[[3,-0.1,-0.2,7.85],[0.1,7,-0.3,-19.3],[0.3,-0.2,10,71.4]]
    #a=[[9,45,285,47.5],[45,285,2025,325],[285,2025,15333,2438]]
    #a=[[4,3,2,960],[1,3,1,510],[2,1,3,610]]
    a=[[3,9,1,6],[6,2,8,8],[9,6,3,3]]
    #a=[[3,2,18],[-1,2,2]]
    for i in range(len(a[0])-1):
        print(a[i][0:len(a)],"=",a[i][-1])
    result=forward(a)
    print("\nresult=\n",np.array(result))
main()


# In[ ]:




