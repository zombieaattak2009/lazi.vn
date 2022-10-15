


from curses.ascii import isalpha


check = False
words = input()
converted=[i for i in words]
tempt = 1

def bad():
    print("BAD INPUT")
for i in converted:
    if i.isalpha() == True:
        if i.isupper() == True and check == False:
                check = "UpperCase"
        if i.islower() == True and check == False:
                check = "LowerCase"
        if i.isupper() == True and check == "UpperCase":
            pass
        elif i.isupper() == False and check == "LowerCase":
            bad()
            break
        if i.islower() == True and check == "LowerCase":
            pass
        elif i.islower() == False and check == "LowerCase":
            bad()
            break
    else:
        pass

        
    
