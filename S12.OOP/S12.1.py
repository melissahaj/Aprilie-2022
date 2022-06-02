# definire clasa
# naming rules:
#sa inceapa cu litera mare: NumeDeClasa - CapsCase
class Car: # -> este o clasa
    pass

class AirplaceTicket:
    pass

# print(Car)
# print(type(Car))

# instantiere, se creeaza un obiect de tip Car, obiect nou
# automobil -> este un obiect

automobil = Car()
# print(automobil)
# print(type(automobil))

# verifica daca un obiect face parte dintr`o clasa anume`
print("automobil este Car")
print(isinstance(automobil, Car)) 
