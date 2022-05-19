#  Make a function for printing the first 5 longest strings in a list ; (len("test"))

list = ("Mihai", "Andrei", "Maria", "Ana", "Elena", "Melissa")

for i in range(0, len(list)):
    if i <= 4:
        print(max(list, key=len))
        list.remove(max(list, key=len))


# cfr = ["petrescu", "omrani", "debeljiuc", "boateng", "deac" , "petrila", "grahovac"]

# def longest_strings (lst) :
#     def len_is (string):
#         return len(string)

#     lst.sort(key=len_is, reverse=True)
#     print (lst[:5])

# longest_strings (cfr)