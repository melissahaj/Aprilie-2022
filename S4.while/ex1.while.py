
k = 1
# n = 6

n = input("n = ")
n = int(n)

while k <= n:
    print("*" * k, "+" * (n - k), sep = "")
    k = k + 1

# 1. n = 3; k = 1
# 2. n = 3; k = 2
# 3. n = 3; k = 3
# 4. n = 3; k = 4 - nu se executa

# *++ k - stelute; n - k plusuri