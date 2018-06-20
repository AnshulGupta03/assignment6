#Q.1- Take 10 integers from user and print it on screen.
print("TAKE 10 INPUTS FROM USER THEN PRINT THEM")
for i in range(10):
    x=input("enter input %d:"%(i+1))
    print("your input is:",x)

print("\n\n",10*"*")


#Q.2Create an infinite loop which is always true.
print("INFINITE LOOP")
while True:
    print("hello")
    
print("\n\n",10*"*")



#Q.3- Create a list of integer elements by user input.
#Make a new list which will store square of elements of previous list.
list1=[]
num=int(input("enter the numbers you want to input:"))
for i in range(num):
    x=int(input("enter number"))
    list1.append(x)
print("list1:",list1)
list2=[]
for i in list1:
    list2.append(i*i)
print("list2:",list2)
    
print("\n\n",10*"*")


#Q.4- From a list containing ints, strings and floats.
#make three lists to store them separately
list1=[1,5,'hello','bye',2,7.9,6.8]
print("list=",list1)
str_list=[]
int_list=[]
float_list=[]
for i in list1:
    if (type(i) == str):
        str_list.append(i)
    elif (type(i) == int):
        int_list.append(i)
    elif (type(i) == float):
        float_list.append(i)
print("string list:",str_list)
print("float list:",float_list)
print("integer list:",int_list)
        
print("\n\n",10*"*")

#Q.5- Using range(1,101), make a list containing even and odd numbers. 
list1=[]
for i in range(1,101):
    list1.append(i)
even=[]
odd=[]
for j in list1:
    if(j%2==0):
        even.append(j)
    else:
        odd.append(j)
list2=even+odd
print("final list",list2)


print("\n\n",10*"*")





#Q.6- Print patterns:
print("TO MAKE PATTERN:")
for i in range(5):
    for j in range(i):
        print("* ",end="")
    print("\r")

print("\n\n",10*"*")


#Q.7- Create a user defined dictionary
#and get keys corresponding to the value using for loop.
n= int(input("enter number of keys :"))
dict={}
for i in range(n):
    k=input("enter name:")
    v=int(input("enter age"))
    dict[k]=v

for k,v in dict.items():
    print(k,v)


print("\n\n",10*"*")



#Q.8- Take inputs from user to make a list.
#Again take one input from user and search it in the list
#and delete that element, if found.Iterate over list using for loop.

x=int(input("enter the number of elements you want to input:"))
list1=[]
flag = 0
print("enter elements of a list:")
for i in range(0,x):
    y=input("enter element:")
    list1.append(y)
print("list is:",list1)
z=input("enter element which you want to delete:")
for j in list1:
    if (j == z):
        flag = 1
        list1.remove(j)
        break
    else:
        flag = 0
if(flag == 0):
    print("element not found")
else:
    print("element is removed from list.")
    print(list1)

print("\n\n",10*"*")
    


    
