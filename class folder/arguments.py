def hello_f(greetings = "hi",name=" you"): # 1st case
    return "{}{}" . format(greetings,name)
print(hello_f())  




def hello_a(greetings,name=" you"):#2nd case
    return "{}{}" . format(greetings,name)
print(hello_f(greetings = "hi",name=" vidit")) 




def hello_b(greetings,name=" you"):# case 3
    return "{}{}" . format(greetings,name)
print(hello_f("hi ","vidit")) 