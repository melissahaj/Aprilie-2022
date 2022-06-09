class Ticket:

    def __init__(self, price):
        # atribute de instanta
        self.price = price

    # metode de instanta
    def get_price_w_taxes(self):
        return self.price + self.price * Ticket.get_tva_ratio()

    # definire metoda statica = metoda de clasa
    @staticmethod
    def get_tva_ratio(): # metodele statice nu au nevoie de self. apelam metoda direct din clasa
        return 0.19

    @staticmethod
    def stm():
        print("TVA:", Ticket.get_tva_ratio())

    # metodele statice pot fi accesate de alte metode statice si de alte metode de instanta, insa metodele de instanta
    # pot fii accesate doar de cele de instanta

# # instatiere
tk = Ticket(100)

tk.stm()
Ticket.stm()

# tk = obiect = instanta
print(tk.get_price_w_taxes())

print(Ticket.get_tva_ratio())