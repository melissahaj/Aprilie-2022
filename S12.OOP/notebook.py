# 1. Scrie o clasa care repr. o Agenda (Notebook).
# Atribute:
#     - nr pagini
#     - culoare
#     - continut - lista de stringuri

# Metode:
#     - scrie in Agenda
#     - vezi nr de pag goale
#     - vezi nr pag scrise



class Nothebook:
    
def __init__(self, nr_of_pag, color):
    self.nr_of_pag = nr_of_pag
    self.colour = color
    self.content = []

def write(self):
    if self.get_empty_pag() != 0:
        self.content.append(content)

def get_empty_pag(self):
    return self.nr_of_pag - len(self.content)

def get_written_pag(self):
    return len(self.content)

