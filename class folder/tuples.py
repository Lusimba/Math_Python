#EXAMPLES OF TUPLES
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5 )
tup3 = "a", "b", "c", "d"
#empty tuple
tup1 = ()
#one value tuple (needs a comma after)
tup1 = (50,)
#Accessing Values in Tuples
tup4 = ('physics', 'chemistry', 1997, 2000)
tup5 = (1, 2, 3, 4, 5, 6, 7 )
print ("tup4[0]: ", tup1[0])
print ("tup5[1:5]: ", tup2[1:5])
tup6= (12, 34.56)
tup7 = ('abc', 'xyz')
# Following action is not valid for tuples
# tup1[0] = 100;
# So let's create a new tuple as follows
tup8 = tup6 + tup7
print (tup8)
#Basic Tuples Operations
len((1, 2, 3))
(1, 2, 3) + (4, 5, 6)
('Hi!',) * 4
3 in (1, 2, 3)
for x in (1,2,3) : print (x, end = ' ')
#Indexing, Slicing, and Matrixes
T=('C++', 'Java', 'Python')
print(T[2])
print(T[-2])	
print(T[1:])