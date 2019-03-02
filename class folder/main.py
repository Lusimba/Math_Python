from manager import *
import getpass
import sys
import time
from os import system, name
import Encoder

def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 


def xchg():
    global a
    global p

    t = input("To: ")
    m = input("Amount: ")

    wrong(exchange([a,p],t,m))

    print("Transaction successful")
    time.sleep(5)
    options()
    
    



def wrong(b):
    global a
    global p
    
    if b == "negative" or b == "negative0":
        print("Invalid password or account username. Please try again.")
        clear()
        login()
    elif b == "negative1":
        print("Invalid username. Please try again.")
        clear()
        xchg()
    elif b == "positive":
        pass
        



def login():
    global a
    global p

    a = input("Account: ")
    p = getpass.getpass("Password: ")

    if a == "back":
        main()

    log = check([a,p])
    
    wrong(log)

    time.sleep(1)

    options()

def options():
    global a
    global p
    clear()

    
    op = input("""What do you want to do:
[A] Add money
[B] Exchange money
[C] Check Balance
[D] Log Out
""")

    if op == "A":
        clear()
        m = input("Amount: ")
        wrong(money(a,p,m))
        print("Transaction successful")
        time.sleep(5)
        options()
    elif op == "B":
        clear()
        xchg()
    elif op == "C":
        clear()
        w,c,s,d = evaluate([a,p])
        wrong(d)
        print("Account: " + w)
        print("Password: " + Encoder.decode(c))
        print("Balance: " + str(s))
        time.sleep(10)
        options()
    elif op == "D":
        clear()
        a = ""
        p = ""
        time.sleep(1)
        main()
    else:
        print("Invalid option")
        time.sleep(5)
        options()

def oana():
    clear()
    m = input("Account: ")
    n = getpass.getpass("Password: ")

    if m == "back":
        clear()
        time.sleep(1)
        main()

    k = add([m,n])

    if k == "positive":
        print("Account opened")
        time.sleep(5)
        main()
    elif k == "negative":
        print("Account username has already been taken. Please try again")
        time.sleep(5)
        oana()
        

def main():
    while True:
        clear()
        g = input("""What do you want to do:
[A] Log-IN
[B] Open a new account
[C] Close
[D] Open Instructions manuel
""")
        if g == "A":
            clear()
            time.sleep(1)
            login()
        elif g == "B":
            time.sleep(1)
            oana()
        elif g == "C":
            time.sleep(5)
            sys.exit()
        elif g == "D":
            time.sleep(5)
            instructions()
        else:
            print("Invalid Option. Please try again.")
            time.sleep(5)
            main()

def instructions():
    clear()
    print("This is a banking system made by Siddharth Maira. ALL COPYRIGHTS OWNED LEGALLY. IF YOU TRY TO SELL IT WITHOUT MY PERMISSION I AM GOING TO SUE YOU")
    print("Contact:- Email: archanasid27@gmail.com")
    print("""Instructions:
1)In order to go back to main menu, type 'back' from login or new account window in account username. 
2)It is just a dummy.
3)Do not tamper with files.
4)Only type in the case mentioned in the question.
5)Enjoy!!!
6)Paparazzi Banona says that mochacappachino is good.
7)Dingleshfrubins
""")

    print("To go to main menu, please type 'back' in the next line")
    a = input("Here: ")
    while True:
        if a == "back":
            break
        else:
            a = input("Here: ")

    time.sleep(5)
    main()

instructions()
    

        
    
    


            


        
        
        
    
    
