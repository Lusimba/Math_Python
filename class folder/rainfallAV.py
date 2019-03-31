def Convert(tup, di): 
    for a, b in tup: 
        di.setdefault(a, []).append(b) 
    return di       
# Driver Code     
citav = [('Bombay', 848), ('Madras', 103),('Bombay', 923),('Bangalore', 201), ('Madras', 128), ('Bangalore', 201.0)\
    ,('Bombay', 885.5), ('Madras', 115.5)] 
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
print(Bombay)
# Madras = rainaverage(M)
# Bangalore = rainaverage(Ba)n    
# Avlist = [ ('Bangalore', Bangalore), ('Bombay', Bombay), ('Madras', Madras)]
# print(Avlist)