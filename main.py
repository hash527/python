# radius = 4
# pi =3.14
# pi
# perimeter = 2*pi*radius
# print(perimeter)

# area=pi*(radius**2)
# print(area)

#conditonal statements

# age=float(input("Enter your age: "))

# if True:
#     pass

# if 12<age<18:
#     growth_stage="Teen"
#     print("Growth Stage: " + growth_stage)
# elif 18<=age<21:
#     print("You are : Young" )
# elif age>=21:
#     print("You are an: Adult" )
# # else:
# #     print("You are a: Child" )

# print(str(age) + " years old")



#loops

'''n=int(input("Enter a number: "))
i=1;

while i<=n:
    print(i,end="")
    if i!=n:
        print(" ",end="")
    i=i+1'''
    
#lists

'''a=["hi","hello",2,0,3,"harsha",["vardhan","Duvvuru",527]]

list=[1,2,3,4]

val =int(input())

print(val in list)'''

#n=int(input("Enter a value: "))

i=1;

'''while i<=n:
    if(i%2!=0):
        print("the Given odd numbers are :"+str(i))
    i=i+1'''

        
'''def add(a,b,c):
    return a+b+c
    
print(add(c=1,b=2,a=3))'''

# all keyword argunments must appear before keyword arguments

def greet(name="harsha",greeting="hello"):
    print(greeting+" "+name)

#greet()

#greet("Developers",greeting="hi")

#greet("Developers")

#a=greet() # return None

#saving function in another variable

'''hello = greet

hello()

hello("Developers",greeting="hello")

hello("Developers")

a=hello()

print(a)'''

'''a=int(input())
b=int(input())

def add(a,b):
    return a+b
    
def multiply(a,b):
    return a*b
    
def operate(a,b,operation=add):
    return operation(a,b)

print(operate(a,b))

print(operate(a,b,operation=multiply))'''

if __name__=="__main__":
    import sys
    print(sys.argv)

