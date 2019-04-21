def convertToDict(tup):
    di = {}
    for a, b in tup: 
        di.setdefault(a, []).append(b) 
    return di

def average(arr):
    if len(arr) == 0:
        return 0
    else:
        return sum(arr)/len(arr)

tup = [('Bombay', 848), ('Madras', 103),('Bombay', 923),('Bangalore', 201), ('Madras', 128), ('Bangalore', 201.0),('Bombay', 885.5), ('Madras', 115.5)] 
dictionary = convertToDict(tup)
for k, v in dictionary.items():
    print("The average rainfall in {} was {}".format(k, average(v)))