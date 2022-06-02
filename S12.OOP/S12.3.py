from auto import Car

ford = Car(4, "manual", False) #ia de la init fiecare cuvant ce inseamna
vw = Car(2, "auto", False)
toyota = Car(4, False, True)

print(toyota.get_gas_level())

print("Alimentan 50 litri")
toyota.refill(50)

# ford.describe()

# vw.drive(100)

# print(vw.get_gas_level())

# vw.refill_full()

# vw.drive(200)

# print