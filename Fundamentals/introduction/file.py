
#variable declaration
 

# Primitive
#  Boolean
# Numbers
# Strings

num1 = 42 #Numbers
num2 = 2.3
boolean = True #Boolean
string = 'Hello World' #Strings

# # Composite
        # List 
      
        # Tuples

        # Dictionary

# List initialize
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] 

# Tuples initialize
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} 

# Dictionary initialize
fruit = ('blueberry', 'strawberry', 'banana')  

#log statement
print(type(fruit))

# access value list
print(pizza_toppings[1]) 

#add value list
pizza_toppings.append('Mushrooms') 

 # access value Tuples
print(person['name'])

#change value tuples
person['name'] = 'George' 


#add value tuples
person['eye_color'] = 'blue'

# access value dictionary
print(fruit[2]) 
print(fruit[0]) 

"""conditional
    - if
    - else if
    - else
 """
if num1 > 45:
    print("It's greater")
else:
    print("It's lower")



if len(string) < 5: #length check 
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")
"""
for loop
"""
for x in range(5):
    print(x)
for x in range(2,5):
    print(x)
for x in range(2,10,3):
    print(x)


"""while loop
    - start
    - stop
    - increment """
x = 0
while(x < 5):
    print(x)
    x += 1

pizza_toppings.pop()
pizza_toppings.pop(1)

print(person)
person.pop('eye_color')
print(person)

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# comment
# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)