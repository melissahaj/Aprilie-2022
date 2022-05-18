magic_numbers = [2.3, 4.5, 46.6, 29.29, 0.22, 23.3]
#                   0     1    2      3     4     5

# for i in range(5, -1, -1):
#     print(i)                        #am printat invers numerele de la 0 la 5


# for number in magic_numbers:
#     print(number)

for index in range(len(magic_numbers) -1, -1, -1):
    print(index, magic_numbers[index])