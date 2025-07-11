"""
an arthimetic operator is used to perform some mathematical \arthimetic 
the operators are:
+,-,*,/,//,%,**
NOTE:input() is a function which takes input from user
code 
"""
a=int(input("enter a number:"))
b=int(input("enter a number:"))  
print("the addition",a+b)
print("the subtraction",a-b)
print("the multiplication",a*b)
print("the division",a/b)#which returns the  quotient 
print("the floordivision",a//b)#which returns the integral quotient part in a division
print("the modulardivision",a%b)#which returns the remainder part before the decimal
print("the power",a**b)#which returns the power`
"""
Bitwise operators are used to perform binary operations they are:
Bitwise and (&)  : if both the bit are "1" it returns 1
Bitwise or(|) : if one of the bit is "1" it returns 1
Bitwise xor(^) : if both bits are "1" returns "0" it returns it"1"
"""
# and operator
a=5
b=9
c=a&b
print(c)


# or operator
d=15
e=13
f=d|e
print(f)

# xor operator
g=12
h=14
i=g^h
print(i)
""""
identity operators are used to compare the values
and return the boolean values..
the operators are "is" , "is not"
"""
x=[1,2,3]
y=[4,5,6]
z=x
print(x is y)
print(x is z)
print(y is not z)
print(z is not x)
print(x is not y) 
""""
logical operators are used to perform logical operations
they are logical & ,or,not
and..if both the conditions are true it returns the true
T T = T
F T = F
T F = F
F F = F
 or... if one of the condition is true it returns the true
 T F = T
 F T = T
 T T = T
 F F = F
 not.. it just negotiates the condition
 T F
 F T
"""
#and operator
a=13
b=45
c=a>=34 and b<=50
print(c)


#or operator
d=67
e=89
f=d!=67 or e==89
print(f)


#not operator
a=10
print(not(a))#F

b=0
print(not(b))#T
""""
membership operators are used to check the values in a sequence
and returns the boolean values
they operators are "in", not in
"""
x=["apple","banana"]
print("apple" in x)
print("pp" not in x)
print("banana" not in x)
print("dragon" in x)

"""
operators are used to compare the values and
return the boolean they are
<,>,<=,>=,==,!=
"""
a=int(input("enter a number:"))
b=int(input("enter a number:"))
print("the greater value",a>b)
print("the lesser than value",a<b)
print("the greater value",a>b)
print("the greater than or equal too value",a>=b)
print("the lesser thequal too value",a>=b)
print("the equal too value",a==b)
print("the not equals too value",a!=b)
