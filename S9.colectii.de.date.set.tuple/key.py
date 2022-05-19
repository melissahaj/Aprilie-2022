
cfr = ["petrescu", "omrani", "debeljiuc", "boateng", "deac" , "petrila", "grahovac"]

def longest_strings (string):
    print("Key function called with:", string)
    def len_is (string):
        return len(string)

    string.sort(key=len_is, reverse=True)
    print (string[:5])

longest_strings (cfr)