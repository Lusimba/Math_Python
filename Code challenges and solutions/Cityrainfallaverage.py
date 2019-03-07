"""
We have a list of Annual rainfall recordings of cities. Each element in the list is of the form (c, r) where c is the city and r is
the annual rainfall for a particular year. The list may have multiple entries for the same city, corresponding to rainfall recordings
in different years. 
Write a Python function rainaverage(l) that takes as input a list of rainfall recordings and comptes the average rainfall for each city. 
The output should be a list of pairs (c, ar) where c is the city and ar is the average rainfall for this city among recordings in the same
input list. The output should be sorted in the dictionary with respect to the city name
"""

def Convert(tup, di): 
    for a, b in tup: 
        di.setdefault(a, []).append(b) 
    return di 
      
# Driver Code     
citav = [('Bombay', 848), ('Madras', 103),('Bombay', 923),('Bangalore', 201), ('Madras', 128), ('Bangalore', 201.0),('Bombay', 885.5), ('Madras', 115.5)] 
dictionary = {} 
x = Convert(citav, dictionary)
B = x['Bombay']
M = x['Madras']
Ba = x['Bangalore']
def rainaverage(B):
    for x in range(len(B)):
        sum = 0
        sum +=B[x]
    return sum
Bombay = rainaverage(B)
Madras = rainaverage(M)
Bangalore = rainaverage(Ba)
Avlist = [ ('Bangalore', Bangalore), ('Bombay', Bombay), ('Madras', Madras)]
print(Avlist)

