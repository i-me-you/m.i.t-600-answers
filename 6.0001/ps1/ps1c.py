# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 08:20:20 2017

@author: me!"""


'''problem set 1c'''
semi_annual_raise = 0.07
r = 0.04
total_cost = 1000000
portion_down_payment = 0.25 * total_cost
starting_salary = int(input('Enter your starting salary: '))
numMonths = 36
#epsilon = 100
minRate = 0
maxRate = 10000
steps = 0
worked = False
current_savings = 0.0
portion_saved = int((minRate+maxRate)/2.0)
while abs(minRate - maxRate) > 1:
    
    annual_salary = starting_salary
    steps += 1
    #monthly_salary = annual_salary/12
    monthly_saved = (annual_salary/12.0) * (portion_saved/10000)
    #monthly_increment = (current_savings * r/12)
    current_savings = 0.0
    
    for rate in range(1,numMonths+1):
        monthly_increment = current_savings * (r/12)
        
        current_savings += monthly_saved + monthly_increment
        
        
        
        if abs(current_savings - portion_down_payment) < 100:
            minRate = maxRate
            worked = True
            break
        
        elif current_savings > portion_down_payment + 100:
            break
        
        if rate & 6 == 0:
            annual_salary += semi_annual_raise * annual_salary
            #annual_salary = starting_salary
            monthly_saved = (annual_salary/12.0) * (portion_saved/10000)
    
    
    if current_savings < (portion_down_payment - 100):
        minRate = portion_saved
    elif current_savings > (portion_down_payment + 100):
        maxRate = portion_saved
    
    portion_saved = int((minRate + maxRate)/2.0)
    
    #print (portion_saved/10000)

if worked:
    print ('Best savings rate ;', portion_saved/10000)
    print ('Steps in the bisection ;', steps)
else:
    print('It is not possible to save up for the down payment')
#works like a bitch on drugs
    