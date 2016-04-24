import random
import sys
import os

print("List Operations")

grocery_list=['Juice', 'Tomatoes', 'Bananas', 'Grapes', 'Lemon'] #create a grocery list

print('First item : ', grocery_list[0]) #print first element
grocery_list[0] = "Green Juice" #update an element from the list
print('First item : ', grocery_list[0])
print(grocery_list[1:3]) #print multiple elements from the list
other_list = ['Car Wash', 'Bring Milk', 'Cash Check']
to_do_list = [other_list, grocery_list] #add multiple lists into one list
print(to_do_list)
print((to_do_list[1][2])) #print specific element from either lists
grocery_list.append('Onions') #append a new element into the list
print(to_do_list)

grocery_list.insert(1,'Pickle') #insert an element at specific position
print(to_do_list)

grocery_list.sort() #sort the list
print(to_do_list)

grocery_list.reverse() #reverse the list
print(to_do_list)

del grocery_list[2] #delete a element at a specific location from the list
print(to_do_list)

grocery_list.remove('Pickle') #remove an element from the list
print(to_do_list)

to_do_list2 = other_list + grocery_list #create a new list by adding multiple lists
print(len(to_do_list2)) #print number of elements in the list
print(max(to_do_list2)) #print maximum element from the list
print(min(to_do_list2)) #print minimun element from the list

#---------OUTPUT-----------#
'''
List Operations
First item :  Juice
First item :  Green Juice
['Tomatoes', 'Bananas']
[['Car Wash', 'Bring Milk', 'Cash Check'], ['Green Juice', 'Tomatoes', 'Bananas', 'Grapes', 'Lemon']]
Bananas
[['Car Wash', 'Bring Milk', 'Cash Check'], ['Green Juice', 'Tomatoes', 'Bananas', 'Grapes', 'Lemon', 'Onions']]
[['Car Wash', 'Bring Milk', 'Cash Check'], ['Green Juice', 'Pickle', 'Tomatoes', 'Bananas', 'Grapes', 'Lemon', 'Onions']]
[['Car Wash', 'Bring Milk', 'Cash Check'], ['Bananas', 'Grapes', 'Green Juice', 'Lemon', 'Onions', 'Pickle', 'Tomatoes']]
[['Car Wash', 'Bring Milk', 'Cash Check'], ['Tomatoes', 'Pickle', 'Onions', 'Lemon', 'Green Juice', 'Grapes', 'Bananas']]
[['Car Wash', 'Bring Milk', 'Cash Check'], ['Tomatoes', 'Pickle', 'Lemon', 'Green Juice', 'Grapes', 'Bananas']]
[['Car Wash', 'Bring Milk', 'Cash Check'], ['Tomatoes', 'Lemon', 'Green Juice', 'Grapes', 'Bananas']]
8
Tomatoes
Bananas
'''