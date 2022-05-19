# scrieti un script care citeste de la tst 3 nr (a, b si c) si afiseaza toti multipli comuni intr-un interval.
# primul nr (a) reprezinta limita superioara a intervalului in care se opereaza, limita inferioara este 1
# celelalte 2 (b, c) sunt numerele pentru care se vor cauta multipli comuni

# extra: sa se verifice daca b si c sunt mai mari decat 1 si mai mici decat lim. sup. (a)
# daca nu sunt in intervalul respectiv sa se afiseze eroare



# a = input("a = ")
# b = input("b = ")
# c = input("c = ")

# multipli_b = list(range(1 * b, a + 1, b))
# multipli_c = list(range(1 * c, a + 1, c))

# set1 = set(multipli_b)
# set2 = set(multipli_c)

# intersection = set1,intersection(set2)
# for i in intersection:
#     print(i)



a = int (input("Introduceti capatul intervalului: "))
b= int(input("Introduceti primul numar: "))
c = int (input("Introduceti al doilea numar: "))

multiplii_b = list (range(1*b,a+1,b))
multimplii_c = list (range(1*c,a+1,c ))


set1 = set(multiplii_b)
set2 = set(multimplii_c)


intersec = set1.intersection(set2)
for i in intersec:
    print (i)



