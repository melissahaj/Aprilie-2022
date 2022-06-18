list1 = ["a", "b", "c"]
# vrem sa obtinem a>b>c
# sau a_b_c

# join

new_str = ">".join(list1)
print(new_str)

new_str1 = "_".join(list1)
print(new_str1)

new_str2 = "\\".join(list1) # trebuie dublat "\", ca sa il ia doar o data
print(new_str2)

# c-b-a
new_str3 = "-".join(reversed(list1))
print(new_str3)

