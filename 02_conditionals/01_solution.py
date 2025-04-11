userage =int(input("enter the age of the user :"))

if userage < 13:
    print("child")
elif userage < 20 :
    print("teenager")
elif userage < 60 :
    print("adult")
else:   
    print("senior")
