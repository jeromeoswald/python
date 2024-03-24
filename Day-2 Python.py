"""
a= str(10)
b= int(10)
c= float(10)


print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))


x,y,z = "Banana", "Apple", "Orange"

print(x)
print(y)
print(z)

x=y=z = "Banana"

print(x)
print(y)
print(z)

x= '''Oranges 
are
Orange in Color'''
print(x)


x= "Hello, World!  "
#print(x[12])

# for a in x:
#  print(a)
#print(len(x))
#print ("like" in x)
#print(x[6:13])
#print(x[-7:-1])
# print(x.upper())
# print(x.lower())
# print(x.replace("H", "Y"))
# print(x.strip())
print(x.split(","))


# #concodinate
# a ="Hello"
# b="world"
# print(a+" "+b)

#conditional statment
# a==b
# a!=b
# a>b
# a>=b
# a<b
# a<=b

a= 150
b= 99
c=111
# if a>b:
#     print("a is greater than b")
# elif a==b:
#     print("a and b are same")
# else:
#     print("b is greater than a")
#print("a is greater than b") if a>b else print("b is greater than a")
if a>b or c>a:
    print("a")
else:
    print("b")


#functions
def sampleFunction(x):
    # print("Hello, World!")
    print(x +" "+"world!")

sampleFunction("Hello")


def sampleFunction(x,y):
    # print("Hello, World!")
    print(x +" "+y)

sampleFunction("Hello","World!")

#for loop
numbers = [1,2,3,4,5,6,77,88,99,100]

for x in numbers:
    print(x)

a = "Fruits"

for x in a:
    print(x)

numbers = [1,2,3,4,5,6,77,88,99,100]

for x in numbers:
    print(x)
    if x ==77:
        break


numbers = [1,2,3,4,5,6,77,88,99,100]

for x in numbers:
    if x == 77:
        continue
    print(x)


for x in range(1,11):
    print(x)

#while loop
i=1

while i < 6:
 print(i)
 i += 1


i=0
while i < 6:
 i += 1
 if i == 4:
  continue
 print(i)

#function as arguments loop

# def sampleFunction(x,y):
#     # print("Hello, World!")
#     print(x +" "+y)

# sampleFunction("Hello","world!")

list = ["car","bike","lorry","bus"]

def loop(x):
    print(x*3)

def sample(love,list):
    for items in list:
        love(items)

sample(loop,list)



#List
list = ["car","bike","lorry","bus",1,88,99,2.0,True]
# print(list)
# print(len(list))
# print(type(list))
# list[3]="Plane"
# list[1:0]=["Van","Superbike"]
list.insert(3,"Plane")
print(list)


#Tuple
t = ("car","bike","lorry","bus",1,88,99,2.0,True)
# print(Tuple)
# print(len(Tuple))
# print(type(Tuple))
# Tuple[3]="Plane"
# Tuple[1:0]=["Van","Superbike"]
# Tuple.insert(3,"Plane")
y=list(t)
y[3]="Plane"
x=tuple(y)

print(x)

#Dictionaries
dictt={
    "name":"Jerome",
    "city":"trichy",
    "age":27,
    "fruits":["apple","orange"]
}

# print(len(dictt))
# print(type(dictt))
# print(dictt)
# x=dictt["city"]
# x=dictt.get("city")
# print(x)

# dictt["city"]= "Chennai"

# dictt.update({"city":"Chennai","name":"Oswald"})
dictt.pop("city")
dictt["color"] = "Green"
print(dictt)


#list comprehension
vechile = ["car","cab","bike","lorry","bus"]
# newvechile=[]

# for x in vechile:
#     if "a" in x:
#         newvechile.append(x)

# newvechile=[x for x in vechile if "a" in x]
# newvechile=[x for x in vechile if x != "lorry"]

# newvechile=[x for x in range(6) if x < 4]

# newvechile =[x.upper() for x in vechile]

newvechile =[x if x!= "bus" else "ship" for x in vechile]
print(newvechile)

#File Handling
f= open("sample.txt","w")
# print(f.read())
# print(f.read(10))

# print(f.readline()) 

# for x in f:
#     print(x)
# f.close()
f.write(" Always be Happy")
f.close()

f= open("sample.txt","r")
print(f.read())

f= open("New.txt","x")
f= open("Newwwww.txt","w")

# f= open("New.txt","x")
# import os
# os.remove("New.txt")

import os
if os.path.exists("Newwwww.txt"):
 os.remove("Newwwww.txt")
else:
 print("No Files")
 
"""

