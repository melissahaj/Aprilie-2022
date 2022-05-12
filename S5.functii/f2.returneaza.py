# o functie care returneaza produsul a 2 nr

def produs(a, b):
    """Product of two numbers"""
    res = 0
    for i in range(b):
        res += a
    return res

print(produs(3, 4))

x_result = produs(30, 23)
print(x_result)