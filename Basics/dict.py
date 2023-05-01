#Defining a dict and using various methods
D_C = { "USA":"W.D.C", "India":"Del", "AP":"Vij", "Tel":"Hyd"}
print(D_C)
print(D_C["USA"])
D_C.items()

D = D_C.popitem()      #Removes the last item in the dict.
print(D_C)
print(D)

print(D_C.get("SA"))     #get() method can be used to avoid error

print(D_C.get("SA","Unkown"))   #setting a default value if the value doesn't exist

#using copy() method using dict
A = D_C.copy()
print(A)

#changing the values of a particular key in dict
D_C["AP"]="Tuluru"
print(D_C)


#working with complex dict
Sat = { "course":{ "title":"Learn ML", "Website":"coursera",}, "Fee":{ "amount":"In USD", "Transaction charge":"Based on the purchase"},
       "Mentor":{"Belyin":"Stanford", "Lex":"MIT"}}
print(Sat)
Sats = Sat.copy()
#changed the value in of a particular key after the copying
Sat["Fee"]["amount"]="Total fee for the course"
print(Sats)

#Making changes using intial key values for complex dict
Sat["Mentor"]={"Klein":"Unknown", "Lex":"MIT"}
print(Sat)

#working with clear method using dict
fri = {"India":"JR", "USA":"Onlyone", "SA":"NoOne"}
print(fri)
#After using clear() method
fri.clear()
print(fri)

#using update method for merging the dict
names = {"NM":"Albuquerque", "USA":"Albuquerque", "India":"Del"}
names1 = {"USA":"W.D.C", "AP":"Hyd"}
#After using update method the items have same keys in first dic will be over its values by second
names.update(names1)
print(names)

#iterating through dict
Actors = {"ST":"MBB", "AG":"IM"}
for key in Actors:
    print(Actors)
    print(Actors.values())   #just testing some random code

#converting dict to list using items() method
lst_ac = Actors.items()
la = list(lst_ac)
print(la)   #Will print list of tuples

#converting list to dict
countries = ["USA", "Italy", "India", "Australia"]
dishes   =  ["Hambuger", "Pizza", "Biryani", "Unkown"]
coun_dis = zip(countries, dishes)
CD = list(coun_dis)
print(CD)
# If incase of any one list contains extra element then the extra element will be ignored in the particular list


