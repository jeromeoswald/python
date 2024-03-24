"""
list = ["car","bike","lorry","bus",1,88,99,2.0,True]
print(list)
print(len(list))
print(type(list))
# list[3]="Plane"
# list[1:0]=["Van","Superbike"]
list.insert(3,"Plane")
print(list)


#Class and Object
# class Human:
#     x=10

# h1=Human()
# print(h1.x)

class Human:
    def __init__(self,name,age):
        self.name = name
        self.age = age


h1 = Human("Jerome", 27)

print(h1.name)
print(h1.age)


class Human:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def methods(self):
        print("Hi, My Name is " + self.name)

h1 = Human("Jerome", 27)
h1.methods()

h1.name ="Malini"
h1.age= 27
h1.methods()


#LAMBDA

# x =lambda a: a+20
# print(x(10))

# x =lambda a,b: a+b
# print(x(10,40))

def f1(n):
    return lambda a : a*n

doub= f1(2)

print(doub(20))

#filter

def prime(x):
    for n in range(2,x):
        if x%n == 0:
            return False
        else:
            return True
        
filtered = filter(prime,range(20))

print("The Prime Number Are ", list(filtered))

#map

def square(x):
    return x*x

Numbers = [1,2,3,4,5,6]

listsquare = map(square,Numbers)

print(list(listsquare))


#PIP

import camelcase

x= camelcase.CamelCase()

a= "understanding the document and window objects in javaScript"

print(x.hump(a))



# import xlrd

# loc = ("C:\\Users\\welcome\\Downloads\\Format.xlsx")

# # wb = xlrd.open_workbook(loc)

# # sheet = wb.sheet_by_index(0)

# # print(sheet.cell_value(0,0))

t = ("car","bike","lorry","bus",1,88,99,2.0,True)
x = iter(t)

print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))


class MyNumber:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x =self.a
        self.a += 1
        return x

myclass = MyNumber()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))



import pickle

mydict = {"1":"a","2":"b"}
pickle_file = open("sample1.txt","wb")
pickle.dump(mydict, pickle_file)

pickle_file = open("sample1.txt","rb")
new_dict = pickle.load(pickle_file)
print(new_dict)

"""

import json

mydict = '{"name":"Jerome","language":["Tamil","English"]}'

person_dict = json.loads(mydict)

print(person_dict)