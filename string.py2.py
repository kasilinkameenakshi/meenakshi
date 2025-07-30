#string is a collection of characterstics
#acessing of elements in a string
#acessing elements using index and sciling
a="softwareindustry"
print(a[0:12])
print(a[2:17:3])

#representation of a string
#A string can be represented using the single code(' ')
#using the double codes('' '')
#using the thripple codes('' '' '')
V='IT'
print(type(V))
#STRING METHODS
'''syntax variable method()
1.upper():converts from lower to upper are'''
w="python"
print(w.upper())
'''lower():converts from upper to lower are'''
w1="PYTHON"
print(w1.lower())

#count():this method is count the number of repeated words in a string
m="i love python python"
print(m.count("python"))

#index():this method is used to return index position of the string
n="vijaywada"
print (n.index("v"))

#strip():this method is to remove the spaces in the strip
s1="this is my book"
print(len(s1))
print(s1)
s2=s1.strip()
print(len(s2))
print(s2) 
#strip():this method is Lstrip(),Rstrip()
s1="this is my book"
print(len(s1))
print(s1)
s1="s1.rstrip"
print(len(s2))
print(s2) 
s1="i love rabbit"
print(len(s1))
print(s1)
s2="s1.lstrip"
print(len(s2))
print(s2) 

#format():this method in used to reture the string in a automated/real formate
name=["meenakshi","kavya","ammu"]
for i in name:
    print("hi{}tinnara".format(i))

#find():it returns "-1" when the string element is not present
m="ists"
print(m.find("a"))
print(m.find("i"))

#startswith():it returns true when the string starts with string
n="i love food"
print(n.startswith("i"))

#endswith():it returns true when the string starts with string
m="i love python"
print(m.endswith("n"))

#variablename.method():
website=["amazon.com","myntra.in","ajio.in"]
in_website=[]
for i in website :
    if i.endswith (".in"):
        in_website.append(i)
print(in_website)
#isalpha(): check if all and return the boolean values
"openai".isalpha()#true
"openai123".isalpha()#false(contain number)
"openai".isalpha()#false(contain space)



