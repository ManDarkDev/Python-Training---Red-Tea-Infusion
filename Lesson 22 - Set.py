''' lesson 22 - SET!
'set
set()
add remove discard copy intersection difference union 
''' 
s = {1, 3, 2, 4, 5, 5, 5} # Creates a set with the unique elements {1, 2, 3, 4, 5}
print(type(s), s) # Prints the type of 's' and the set 's'

empty = set() #an empty set called empty is created using the set() constructor.
print(type(empty), empty) #This line prints the type of empty (also set) and the empty set itself.

s1 = {'a', True, 2, 3.14} # The variable s1 is assigned a set containing the elements 'a', True, 2, and 3.14.
print(s1)
try:
    print(s[0]) # tries to access the 1st element of s
except:
    print('You cannot access values by index') #Prints error message if indexing fails

if 1 in s: 
    print('1 is present')# prints if 1 is found in the sets

for element in s:
    print(element) # Prints each element in the set s

l = [1, 2, 1, 2, 1, 1, 3, 3, 3] #creates a list l
print(set(l)) #converts list l to a set removing duplicates

s.add(6)# adds the integer 6 to the set s 
print(s)
s.add(6)# adds the integer 6 to the set s
print(s)
s.remove(6)# removes the integer 6 from the set s 
print(s)
s.discard(5)# removes the integer 5 fromt the set s
print(s)
s2 = s.copy()# creates a copy of s and assigns it to s2
print(s)
print(s1.intersection(s))# prints the intersection of sets s2 and s 
print(s1.union(s))#prints the union of sets s1 and s 
print(s1.difference(s))#prints the difference between sets s1 and s