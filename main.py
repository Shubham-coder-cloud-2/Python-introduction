#this is a variable
y = -23

x = y + 22

#This is an if condition
if x < 5:
    print("yes it is good")
else:
    print("not it is not good")

#Variable is case sensitive

my_variable = "My vairable"

MY_VARIABLE = "MY VARIABLE"

print(my_variable)

print(MY_VARIABLE)

#1 value in many variable

a = b = c = "One value"

print(a)
print(b)
print(c)

#Many variable Many values

d , e , f = "D" , "E" , "F"

print(d)
print(e)
print(f)

#Unpack Collection

Letter = [ "G" , "H" , "I" ]

g , h , i = Letter

print(g)
print(h)
print(i)

#Vairables with string

j = "J"

print(j + " come after I " )

#Global Variables

h = "H"

def hfunc():
            print(h)

hfunc()