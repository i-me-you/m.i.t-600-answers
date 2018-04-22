# -*- coding: cp1252 -*-
#mit-introduction to computer science and programming using python 6.0001
#problem set 1 A answers
"""Write a program to calculate how many months it will take you to save up enough money for a down  payment.
given the following parameters"""
total_cost = float(input('Total cost of \'your\' dream home: '))
portion_down_payment = 0.25 * total_cost
current_savings = 0.0
r = 0.04
annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(input('Enter the percent of your salary to be saved, as a decimal: '))
portion_saved_month = portion_saved * annual_salary / 12
number_of_months = 0
increment = (current_savings * r / 12) + portion_saved_month
while current_savings < portion_down_payment:
    current_savings +=(current_savings * r / 12) + portion_saved_month #even tho this is the exact thing as the variable 'increment', if used will give a different value
    number_of_months += 1
print ('The number of months it\'ll take to save up for the down payment of your dream'
       ' Home is ', number_of_months )

