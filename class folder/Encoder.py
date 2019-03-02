def encode(what):
    what = what.upper()
    newwhat = ""
    for i in range(len(what)):
        try:
            a = int(meow.index(what[i])) + 1
            newwhat += meow[a]
            
        except Exception:
            newwhat += what[i]

    return newwhat

def decode(what):
    newwhat = ''
    for i in range(len(what)):
        try:
            a = int(meow.index(what[i])) - 1
            newwhat += meow[a]
        except Exception:
            newwhat += what[i]
            
    newwhat = newwhat.lower()
    return newwhat

if __name__ == "__main__":
    while True:
        kaka = input("Encode: ")
        print(encode(kaka))

        mo = input("Decode: ")
        print(decode(mo))


        
