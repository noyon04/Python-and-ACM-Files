#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
def elimin(a,nth):
    a_mod=[]
    for x in range(nth+1):
        a_mod.append(a[x])
    temp1=a[nth]
    j=nth+1
    while(j<len(a)):
        temp2=a[j]
        temp3=[i * (temp2[nth]/temp1[nth]) for i in temp1]
        temp2=[x1 - x2 for (x1, x2) in zip(temp2 ,temp3)]
        a_mod.append(temp2)
        j=j+1
    return a_mod
def forward(a):
    for i in range(len(a)-1):
        a=elimin(a,i)
    return a
def backward(am):
    x=[]
    for i in range(len(am),0,-1):
        x_i=len(x)-1
        temp=am[i-1]
        if(len(x)!=0):
            for j in range(len(temp)-2):
                if(temp[j]!=0.0):
                    temp2=temp2-x[x_i]*temp[j+1]
                    #print('temp2',temp2,'x[x_i]',x[x_i],'temp[j+1]',temp[j+1])
                    x_i=x_i-1
            temp2=temp[len(temp)-1]+temp2
            #print(temp2)
        else:
            temp2=temp[len(temp)-1]
        x.append(temp2/temp[i-1])
        temp2=0
    return x
def main():
    #a=[[3,-0.1,-0.2,7.85],[0.1,7,-0.3,-19.3],[0.3,-0.2,10,71.4]]
    #a=[[6,3,-11,-35],[30,-18,26,-16],[15,7,48,38]]
    #a=[[25,-48,-11,-27],[-49,-27,6,-22],[42,-33,-29,-50]]
    a=[[3,9,1,6],[6,2,8,8],[9,6,3,3]]
    #a=[[3,2,18],[-1,2,2]]
    for i in a:
        print(i[0:len(a)]," = ",i[len(a)])
    am=forward(a)
    print('\nAfter Forwarding\n')
    for i in am:
        print(i[0:len(am)]," = ",i[len(am)])

    x=backward(am)
    print('\nAfter Backwarding\n')
    for i in range(len(x),0,-1):
        print('x',-i+(len(x)+1),'= ',x[i-1])
main()  

