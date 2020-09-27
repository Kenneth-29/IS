#Lists
l1 = [2,3,4.53,5,78,100,12,-1] # List 1 declared with same data types
l2 = ["Tshepo", "Kitso", " ", "Nkosi", "Sethunya"] # String data types
l3 = ['a', 3, 43, 'b', 'c', 103, 'd', 'e', 'Thabiso'] #mixed data types

l4 = l2 + l3 #concatnating two lists
print(l4)
print(len(l1)) # getting the length of list and printing it
print(l2[0]*l1[3])

print(l1[::-1]) # Prints l1 in reverse
print(l2[3:5])

if "Tshepo" in l2:
    print("Tshepo is a member of this list")

for i in l2:
    print(i)

for i in l1:
    print(i)
#Tuples
t0 = ()
t1 = (2, "Kitso", 3, 4, 6, "Jason")
t2 = ("Jane", 2.178, 2, 12, "Masego")

print(t1[1] + " " + t2[-1]) # tuples and concatenating from diffrent tuples
print(t1 + t2)

print(len(t1) + len(t2))

print(len(t1))

for i in t1:
    print(i)

#Sets
s0 = 'William Winnie' # setting a string
s01 = list(s0) # construting a list from a string
s02 = set(s0) # constructing a set from string
s00 = set() #defines\dclares an empty set
s1 = {} #defines an empty dictionary
s2 = {'Baseki', 'Resego', 'Rebaone', 'Stewart', 'Baseki', 'baseki'}
s3 = {'Stewart', 'PM', 1, 55.28, None, ('bida', 'cse', 'abc'), 'Resego'}

print(s00|s2)
print(s2.union(s3)) # print(s2|s3)
print(s2&s3)
print(len(s3)) #prints the length of set 3
print(s01)
print(s02)

if 'cse' in s3:
    print("CSE is a member of set 3")
else:
    print("CSE is not a member in set 3")

#Dictionaries
d1 = dict([
    ('Name', 'Kenneth'),
    ('Surname', 'Mogopodi'),
    ('ID', '18039'),
    ('is_a', 'student'),
    ('location', 'Gabs'),
    ('school', 'SCIS'),
    ('gender', 'Male')
])

d2 = dict(
    cource_name = 'CSE',
    venue_at = 'lecture theater',
    max_number = 60,
    resoucesneeded = ('laptop', 'pen', 'notebook')

)
d3 = {'ID':'cse18-039', 'IS': 70, 'AWD': 87, 'CSA':85}
up3 = {'IS': 75, 'CSA': 95} #new list
d3.update(up3) #update dictionary 3

#accessing dictionary contents, NB: key value is importatnt
print(d1['is_a'])
print(d2['resoucesneeded'])
print(d3['CSA'])

