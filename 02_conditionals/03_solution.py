Marks = int(input ("enter the marks of the student : "))
if Marks >101:
    print('invalid input ')
    exit()

if Marks > 90:
    print("grade A")
elif Marks > 80 :
    print("grade B")
elif Marks >70 :
    print("grade C")

elif Marks > 60 :
    print("grade D")
else :
    print("grade F")