# scrieti o clasa Shape care are o metoda arie
# scrieti o clasa Circle care mosteneste Shape si suprascrie metoda arie
# scrieti o clasa Square care mosteneste Shape si suprascrie metoda arie

class Shape:

    def arie(self):
        pass

class Circle(Shape):
    
    def arie(self, r):
        return 3.14 * r ** 2 

class Square(Shape):

    def arie(self, l):
        return l ** 2

cerc = Circle()
patrat = Square()

print(cerc.arie(10))
print(patrat.arie(5))




