#!/usr/bin/env python
# coding: utf-8

# In[45]:


import numpy as np
import math

#Forward Finite Difference (First Derivative, Second Derivative)
def for_f_d(dc,h,order):
    if(order==1):
        fx=(dc["fx1"]-dc["fx0"])/h
    elif(order==2):
        fx=(-dc["fx2"]+4*dc["fx1"]-3*dc["fx0"])/(2*h)
    return fx
def for_s_d(dc,h,order):
    if(order==1):
        fx=(dc["fx2"]-2*dc["fx1"]+dc["fx0"])/(h*h)
    elif(order==2):
        fx=(-dc["fx3"]+4*dc["fx2"]-5*dc["fx1"]+2*dc["fx0"])/(h*h)
    return fx

#Backward Finite Difference (First Derivative, Second Derivative)
def bac_f_d(dc,h,order):
    if(order==1):
        fx=(dc["fx0"]-dc["fx-1"])/h
    elif(order==2):
        fx=(3*dc["fx0"]-4*dc["fx-1"]+dc["fx-2"])/(2*h)
    return fx
def bac_s_d(dc,h,order):
    if(order==1):
        fx=(dc["fx0"]-2*dc["fx-1"]+dc["fx-2"])/(h*h)
    elif(order==2):
        fx=(2*dc["fx0"]-5*dc["fx-1"]+4*dc["fx-2"]-dc["fx-3"])/(h*h)
    return fx

#Centered Finite Difference (First Derivative, Second Derivative)
def cen_f_d(dc,h,order):
    if(order==1):
        fx=(dc["fx1"]-dc["fx-1"])/(2*h)
    elif(order==2):
        fx=(-dc["fx2"]+8*dc["fx1"]-8*dc["fx-1"]+dc["fx-2"])/(12*h)
    return fx
def cen_s_d(dc,h,order):
    if(order==1):
        fx=(dc["fx1"]-2*dc["fx0"]+dc["fx-1"])/(h*h)
    elif(order==2):
        fx=(-dc["fx2"]+16*dc["fx1"]-30*dc["fx0"]+16*dc["fx-1"]-dc["fx-2"])/(12*pow(h,2))
    return fx


#The Given Equation
def equation(x):
    #temp=-0.1*pow(x,4)-0.15*pow(x,3)-0.5*pow(x,2)-0.25*x+1.2
    temp=(math.sin(x))
    return round(temp,5)

def main():
    x=(np.pi)/4
    #x=25
    h=(np.pi)/12
    #h=2
    dc={}
    for i in range(-3,4):
        t_x=x+i*h
        temp=equation(t_x)
        dc["fx"+str(i)]=temp
    print(dc)
    fx=for_s_d(dc,h,2)
    print("\nAfter_Forward_Second_Derivative_2nd_Order= ",round(fx,4),"\n")
    fx=bac_f_d(dc,h,1)
    print("After_Backward_First_Derivative_1st_Order= ",round(fx,4),"\n")
    fx=bac_f_d(dc,h,2)
    print("After_Backward_First_Derivative_2nd_Order= ",round(fx,4),"\n")
    fx=cen_s_d(dc,h,2)
    print("After_Centered_Second_Derivative_2nd_Order= ",round(fx,4),"\n")

main()


# In[ ]:




