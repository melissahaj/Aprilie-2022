from auto import Car

# metodele se apeleaza prin obiect.numele metodei
volvo = Car() # aici se apeleaza constructorul
vw = Car()

# accesare atribute
print("Volvo gas:", volvo.get_gas())
print("VW gas:", vw.get_gas())

volvo.refill(30)
print("-" * 50)

print("Volvo gas:", volvo.get_gas())
print("VW gas:", vw.get_gas())

