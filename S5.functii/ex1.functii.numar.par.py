# Scrieti o functie care def un nr par. Daca este par returneaza True. altfel False. Functia are un singur argument.

def is_even(n):
    """Check if number is even"""
    if n % 2 == 0: #formula ca un nr este par
        return True

    else:
        return False

# print(is_even(10)) #10 a inlocuit n
# print(is_even(5))

# for i in range(101):
#     print(is_even(i)) #am creat o alternanta

# for i in range(10):
#     if is_even(i):
#         print("**")
#     else:
#         print("--")



for i in range(10):
    if is_even(i):
        print(i, "este par")
    else:
        print(i, "este impar")