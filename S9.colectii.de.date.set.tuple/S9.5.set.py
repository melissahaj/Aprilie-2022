# suma multiplilor de 3 si 5 in interbalul 0 - 1000

multipli_3 = list(range(3, 1001, 3))
multipli_5 = list(range(5, 1001, 5))

print(sum(set(multipli_3 + multipli_5)))

#never do this - one-liner
print(sum(list(range(3, 1001, 3)) + list(range(5, 1001, 5)))
