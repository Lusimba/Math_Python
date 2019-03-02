import pickle
from Encoder import *


def check(a):
    pickle_in = open("pass.pickle","rb")
    pa = pickle.load(pickle_in)

    for line in range(len(pa)):
        if pa[line][0] == a[0]:
            
            if pa[line][1] == encode(a[1]):
                return "positive"
                break
    return "negative"

        
def add(a):
    ca = True
    a.append(int(0))
    a[1] = encode(a[1])
    try:
        pickle_in = open("pass.pickle","rb")
    except Exception:
        pickle_out = open("pass.pickle", "wb")
        pickle_out.close
        pickle_in = open("pass.pickle", "rb")
        
    try:
        pa = pickle.load(pickle_in)
    except Exception:
        pa = []
    for i in pa:
        if i[0] == a[0]:
            ca = False       
        
    if ca == True:
        pa.append(a)

        pickle_out = open("pass.pickle", "wb")
        pickle.dump(pa,pickle_out)
        pickle_out.close()
        return "positive"
    elif ca == False:
        return "negative"

def money(account, password, money):
    
    try:
        int(money)
    except Exception:
        money = int(0)
    try:
        pickle_in = open("pass.pickle","rb")
    except Exception:
        pickle_out = open("pass.pickle", "wb")
        pickle_out.close
        pickle_in = open("pass.pickle", "rb")
        
    try:
        pa = pickle.load(pickle_in)
    except Exception as e:
        pa = []      

    for i in range(len(pa)):
        if pa[i][0] == account:
            if pa[i][1] == encode(password):
                pa[i][2] = pa[i][2] + int(money)
                pickle_out = open("pass.pickle", "wb")
                pickle.dump(pa, pickle_out)
                pickle_out.close()
                return "positive"
                break
    return "negative"

    
def exchange(giver, taker, money):
    try:
        int(money)
    except Exception:
        money = int(0)
        
    if int(money) < 0:
        money += int(money * 2)
        
 
        #continue
    try:
        pickle_in = open("pass.pickle","rb")
    except Exception:
        pickle_out = open("pass.pickle", "wb")
        pickle_out.close
        pickle_in = open("pass.pickle", "rb")
        
    try:
        pa = pickle.load(pickle_in)
    except Exception:
        pa = []
        
    for i in pa:
        if i[0] == taker:
            i[2] += int(money)
            l = True

    if l == True:
    
        for line in range(len(pa)):
            if pa[line][0] == giver[0]:
                
                if pa[line][1] == encode(giver[1]):
                    pa[line][2] -= int(money)

                    pickle_out = open("pass.pickle", "wb")
                    pickle.dump(pa, pickle_out)
                    pickle_out.close()                            
                    return "positive"
                    break
        return "negative0"
    
    elif l == False:
        return "negative1"

        
    
def evaluate(a):
    
        #continue
    try:
        pickle_in = open("pass.pickle","rb")
    except Exception:
        pickle_out = open("pass.pickle", "wb")
        pickle_out.close()
        pickle_in = open("pass.pickle", "rb")
        
    try:
        pa = pickle.load(pickle_in)
    except Exception:
        pa = []

    for i in pa:
        if i[0] == a[0]:
            if i[1] == encode(a[1]):
                
                return [i[0], i[1], i[2], "positive"]
                break
    return [None,None,None,"negative"]

if __name__ == "__main__":
    while True:
        print(check(['a','b']))
        print(evaluate(['a','b']))
    
