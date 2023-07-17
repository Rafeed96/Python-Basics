email = input("Enter Your Email:")

if len(email)>= 6:
    if email[0].isalpha():
        if "@" in email and (email.count("a")==1):
            pass

    else:
        print(" Wrong Email 2")
else:
    print(" Wrong Email 1")