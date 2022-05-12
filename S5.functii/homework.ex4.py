#  Scrieti o functie care returneaza volumul unui cub in litri. Aceasta va primi
# un singur agument reprezentand muchia cubului in metri

def cube_volume(edge):
    """Calculate cube volume in liters"""
    # vol cub ridicata la puterea a 3-a  ori 1000 l obtinem metrii cubi 1 m3 = 1000 litri
    return edge ** 3 * 1000

def convert_to_m3(liters):
    """Convert liters in m3"""
    return liters / 1000


# 7 - a

print("Volumul cubului: ", convert_to_m3(cube_volume(18)) , "m3")

# ierarhie de apelare, o functie in alta functie
# 1 cube_volume - prima functie care se apeleaza, functie de conversie
# 2 convert_volume
# 3 print
