def hello_f(greetings = "hi",name=" you"): # 1st case to make it work
    return "{}{}" . format(greetings,name)
print(hello_f())  




def hello_a(greetings,name=" you"): # 2nd case to make it work
    return "{}{}" . format(greetings,name)
print(hello_f(greetings = "hi",name=" vidit")) 




def hello_b(greetings,name=" you"): # 3rd case to make it work 
    return "{}{}" . format(greetings,name)
print(hello_f("hi ","vidit")) 
