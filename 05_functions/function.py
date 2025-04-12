# Problem 1 
# def square_of_num(number):
#     return number ** 2 
# result = square_of_num(4)
# print(result)


# Problem -2 
# def sum_of_num (a, b):
#     return a + b 

# result = sum_of_num(3,4)
# print(result)


# Problem - 3 

# def Multiply_two(a ,b):
#     return a * b 

# result = Multiply_two(4,5)
# print(result)
# print(Multiply_two('a',5))
# print(Multiply_two(5,'a'))

# Problem - 4 
# import math
# def area_of_circle(r):
#     circumference = round(2*r*math.pi ,2)
#     area = round(r*r*math.pi,2)
#     return area , circumference
# print(area_of_circle(4))

#Problem - 5 

# def greet(name):
#     if name == '':
#         return "hello anon"
#     else:
#         return 'hello,' + name

# print(greet("srajan"))
# print(greet(""))


# Problem - 6 
# cube = lambda x: x ** 3
# print(cube(3))


# Problem  - 7 

# def sum_all(*args):
#     return sum(args)

# print(sum_all(1,2))
# print(sum_all(1,2,3))
# print(sum_all(1,2,3,4))
# print(sum_all(1,2,3,4,5))


# Problem - 8 
# kwargs = keyword arguments 


# def print_kwargs(name , power):
#     print("name" ,name ,"power" , power)

# print_kwargs("shaktiman" , "fly")

# def print_kwargs(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}  {value}")
# print_kwargs(name = "shaktiman" , power = "fly")
# print_kwargs(name = "shaktiman")
# print_kwargs(name = "shaktiman" , power = "fly",enemy = "greed")


# problem - 9

# def even_gene (limit):
#     for i in range(0,limit+1):
#         if i%2 == 0:
#             print(i)

# even_gene(45)


# Probelm - 9 re 

# def even_generator (limit):
#     for i in range(2 , limit  + 1 ,2 ):
#         yield   i 

# for num in even_generator(12):
#     print(num)


# # recursive funtion to calculate the factorial 

# def factorial (n):
#     if n== 0 :
#         return 1 
#     return n * factorial(n-1)


# print(factorial(5))
