# numbers = [1,-2,-3,4,5,-6,7,-8,-9,10]
# positive_number_count = 0 
# for num in numbers :
#     if(num > 0 ):
#         positive_number_count += 1
#     # print(num)

# print(positive_number_count)

# # QUESTION -2 
# n = 4 
# sum_even = 0 

# for i in range(1,n+1) :
#     if(i%2==0):
#         sum_even = sum_even + i 
# print(sum_even)


# QUESTION - 3 

# # multiplication table generator 

# num = 9 

# for i in range(1 ,11):
#     if i== 5:
#         print("skip")
#     else :
#         print(i*num)


# Question - 4

# Reverse a String 

# str ="srajan"
# new_str = ""
# for char in str:
#     new_str =char +  new_str

# print(new_str)



#Question - 5

# str = "teeth"

# for char in str : 
#     if str.count(char) ==1 :
#         print(char)
#         break

# Question 6 


# number = 5 
# factorial = 1 
# while  number > 0 :
#     factorial = factorial * number
#     number -= 1 

# print(factorial)



# Question 7 

# while True :
#     number = int(input("enter the value between 1 and 10 "))
#     if  1 <= number <=10: 
#         print("thanks")
#         break 
#     else :
#         print("invalid number , try again")


# # Question 8 


# number = int(input("enter the value of number "))

# is_prime = True 

# if number > 1 :
#     for i in range(2, number):
#         if(number % i) == 0:
#             is_prime= False
#             break


# print(is_prime)


#Question - 9 

items = ["apple","banana","orange","apple","mango"]
unique_item = set()
for item in items:
    if item in unique_item:
        print("duplicate")
        break 
    unique_item.add(item)