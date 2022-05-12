# Scrie o functie care primeste 2 parametrii si printeaza primele 10 numere si le printeaza:
# 0
# ===
# 1
# === etc

def b_range(stop, sep="+", sep_c=10):
    for i in range(stop):
        print(i, end="")
        print(sep * sep_c)

# b_range(10, "*", 10)

# b_range(10, "=", 10)
# b_range(5, "=", 10)
# b_range(20, "=", 10)

# b_range(12)
# b_range(7)

b_range(5,sep_c=20)