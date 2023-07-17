email = input("Enter Your Email:")

if len(email)>= 6:
    if email[0].isalpha():
        if "@" in email and (email.count("a")==1):
            if (email[-4]==".") ^ (email[-3]=="."):
                for i in email:
                    if i == i.isspace():
                        k = 1
                    elif i.isalpha():
                        if i==i.upper():
                            j==1
                    elif i.isdigit():
                        continue
                    elif i =="_" or i=="," or i=="@":
                        

            else:
                print(" Wrong Email 4")
        else:
            print(" Wrong Email 3")
    else:
        print(" Wrong Email 2")
else:
    print(" Wrong Email 1")