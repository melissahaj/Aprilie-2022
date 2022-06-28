try:
    f_out = open("output.txt", "a")
except OSError:
    print("Nu pot deschide fisierul.")

for i in range(100):
    f_out.write(f"NO: {i}\n")

f_out.close()