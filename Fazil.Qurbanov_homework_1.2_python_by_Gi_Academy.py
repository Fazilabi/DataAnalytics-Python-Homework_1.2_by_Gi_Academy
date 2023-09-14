#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# ==========================================================
''' Question 1
 Divide the elements of the given list by 2 and replace the list with the new integers obtained.
 List=[2,8,18,26,42] '''
List=[2,8,18,26,42]
new_list=[]
for x in List:    
    x/=2
    new_list.append(x)
print(new_list)


# ==========================================================
 '''Question 2
Find the numbers in the list x that are divisible by 5 and are less than or equal to 150.'''

List=[1,7,15,38,40,55,150,200,549,655]
new_list = []
for x in List:
    if x%5==0 and x<=150:
        x/=5
        new_list.append(int(x))
print(new_list)
# ==========================================================
'''Question 3
Print whether the input is negative, positive or 0.'''
number = int(input("Enter a number: "))
if number>0:
    print("is positive")
elif number<0:
    print("is negative")
else: print("is zero")

# ==========================================================
 '''
 Question 4
 x = 600
 If the given number is divisible by 6, print x/6, if it is divisible by 3, 
 print x/3, if it is divisible by 2, print x/2.'''
number = int(input("enter only number: "))
if number%6==0:
    print("x/6")
elif number%3==0:
    print("x/3")
elif number%2==0:
    print("x/2")
else:print("this number is not divisible 6 , 3 or 2")


# ==========================================================
''' Question 5
 Print the cube of the elements of the list divisible by 3, the square of the elements divisible by 2, 
 5 times the elements divisible by 5, and 10 times the elements divisible by 10 '''
list1= []
for x in range( 1, 21):
    list1.append(x)    
print(list1)
list3 = []
list2 = []
list5 = []
list10 = []

for a in list1:
    if a%3==0:
        a=a**3        
        list3.append(a)
for a in list1:
    if a%2==0:
        a*=2
        list2.append(a)
for a in list1:
    if a%5==0:
        a*=5
        list5.append(a)
for a in list1:
    if a%10==0:
        a*=10
        list10.append(a)    
print(list3)
print(list2)
print(list5)
print(list10)
# ==========================================================
 '''Question 6
 The given dictionary consists of vehicles and their weight in kilograms. 
 Make a list of names of vehicles weighing less than 2000 kilograms. 
 dict={"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, 
 "Semi": 13600, "Bicycle": 7, "Motorcycle": 110 }'''
    dict1={"Sedan": 1500, 
      "SUV": 2000, 
      "Pickup": 2500, 
      "Minivan": 1600, 
      "Van": 2400, 
      "Semi": 13600, 
      "Bicycle": 7, 
      "Motorcycle": 110 
     }
dict2={}
for k,v in dict1.items():
    if v<2000:
        dict2[k]=v
print(dict2)    
    
# ==========================================================
 '''Question 7
 Write Python code to find the smallest number among three numbers:'''
list1=[]
for a in range(1,4):
    number = int(input(f"Enter {a} : "))
    list1.append(number)
list1.sort()
print(list1)
print(f"smallest number is {list1[0]} among three numbers")

