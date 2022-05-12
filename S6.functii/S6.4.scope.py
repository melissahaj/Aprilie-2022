# global scope  - putem modifica valoarea in acelasi scop
rev = 20
PI = 3.14 
age = 20


def bar():
    # local scope
    age = 1
    age1 = age + 10
    print(age1)





# def reverse(n):
#     rev = 0
#     while n != 0:
#         c = n % 10  #rest
#         n = n // 10 #catul
#         rev = rev * 10 + c





