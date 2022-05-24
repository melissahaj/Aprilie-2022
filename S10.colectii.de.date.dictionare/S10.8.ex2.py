colors = {
    "red": "#FF0000",
    "green": "#00FF00",
    "blue": "#0000F"
}

for k in colors.keys():
    colors[k] = colors[k].strip("#") #am eliminat # din toate liniile
  
print(colors)


#
def noner(dict_in, key):
    if key in dict_in.keys():
    dict_in[key] = None

noner(colors, "red")
print(colors) # s-a sters valoarea de la red, daca exista cheia o modifica, daca nu exista adauga o noua cheie. am adaugat if in fuct si doar o modifica
