# Scrieti o functie care returneaza daca unu nr. (reprezentan un an) este
# considerat an bisect.

def is_leap_year(year):
    """Check if it is leap year"""
    if year % 4 == 0: #formula ca este an bisect
        return True

    else:
        return False

is_leap_year(1956)
print(is_leap_year(1956))

