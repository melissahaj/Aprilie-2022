# Ulizati functia de la pct 1 pentru a afisa toate numerele impare in intervalul
# [0, 50] si in intervalul [2000, 2100].


def is_even(n):
    """Check if number is even"""
    if n % 2 == 0: #formula ca un nr este par
        return True

    else:
        return False

for i in range(0, 51):
    if not is_even(i):
        print(i, end = " ")
for i in range(2000, 2101):
    if not is_even(i):
        print(i, end = " ")

   