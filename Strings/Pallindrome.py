#Evaluate pallindromes

user = input('Enter any word on your mind: ')

#You may make it caseless or you may choose to convert it to uniform
#case (upper or lower). We shall use the caseless version. 
word = user.casefold()

#Reverse the word
rev = reversed(word)

#Evaluate equivalence
if list(word)== list(rev) :
    #Print the Pallindrome
    print('The reverse of the word is '+"".join(reversed(word)))
    print ('You entered a Pallindrome')
else:
    print ('It is not a Pallindrome')