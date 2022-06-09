class Pen:
    #atribute de clasa / statice
    brand = 'NOKI'


    def __init__(self, color):
        # atribute de instanta
        self.color = color
        self.is_empty = False

pen = Pen('red')
pen2 = Pen('black')

# print(pen.color)
# print(pen2.color)

# Pen.brand = "no-name"

print(pen.brand)
print(pen2.brand)

 # obiectele python pot fi modificate chiar si dupa ce au fost create
 # sa fim atenti sa nu modificam atribute statice prin intermedil obiectelor, 
 # deoarece creeaza un atribut de instanta, pt ca nu are voie sa creeze atributul static


