#creation of dictionaries
#1.empty dictionary
c1={}
print(type())
#2.key Value
mydict={1:"meena"2:"mtm"}
print(type(mydict))

#accessing the elements in dictionary
#using the keys we can get the value of dictionary
d2={100:"sai";200:"hima";"phon":9440882240;"place:""mtm"}
print(d2[100])#hima
print(d2["place"])#mtm
print(d2[600])

#updating the dictionaries
#using the keys we can update the dictionary
d2[100]="sunny"
print(d2)

#dictionary methods 
#to access the methods the syntax is variable name.method name()
#1.get()returns the value of a specified key
m={"name":raju,"s.no":1,"phon":9440882240}
print(m)
print(m.get(["name"]))
print(m.get(["s.no"]))
#keys():
#this method is used to get in a dictionary
m={"name":raju,"s.no":1,"phon":9440882240}
print(m)
print(m.get(["name"]))
print(m.get(["s.no"]))
#values():
#this method is used to retrive the values in a dictionary
print(m.value())
#items():
#this method is used to get all the item
print(m.items())
#updating the dictionary into list():
# in this particular sinarioa by converting the dictionary into list we can retrive only keys
#update method():
#to update any new key value base for an exsisting dictionary we use this updating function
m.update({"food":"biriyani"})
print(m)
#pop():
#this method is used to the keys in a dictionary 
m.pop("s.no")
print(m)
