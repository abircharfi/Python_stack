#1
def main (num):
    list = []
    if (num >=0):
       
        for i in range(num,-1,-1):

            list.append(i)

        return list
    
print(main(5))

#2
def print_and_return (list):
    num1 =list[0]
    num2 =list[1]
    print(num1)
    return num2 
   

print(print_and_return([5,6]))

#3

def first_plus_length (list):
    return list[0]+len(list)

print(first_plus_length([0,9,15,30]))

#4
 
def Values_Greater_than_Second (list):
    new_list= []
    for i in range(0,len(list)):
       if list[i]> list[1]: 
          new_list.append(list[i])   
    
    if len(list)<2:
       return False
    
    print(len(new_list) )
    return new_list

#5

print(Values_Greater_than_Second([5,2,3,2,1,4]))

def This_Length_That_Value(size,value):
    list=[]
    for i in range(0,size):
        list.append(value)

    return list

print (This_Length_That_Value(6,2))