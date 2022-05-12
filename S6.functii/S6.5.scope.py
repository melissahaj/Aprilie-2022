# global scope
index = 189

for index in range(100, 20, -10):
    # local scope
    print(index)

# for loop variable leaking

print(index)