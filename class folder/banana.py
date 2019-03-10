bankAc = {
    "name":"zara",
    "age":20,
    "city":"hyderabad",
    "account":123,
}
ac = int(input("enter the account number: "))
if ac == bankAc["account"]:
    print("welcome ",bankAc["name"])
else:
    print("what the heck")   
bankAc["age"] = 28
print(bankAc["age"])
