import time

# timestamp -  secunde trecute de la 01.01.1970

print(time.time())

b_day = time.strptime("12/18/1991", "%m/%d/%Y")

wday = {
    0: "Luni",
    1: "Marti",
    2: "Miercuri",
    3: "Joi",
    4: "Vineri",
    5: "Sambata",
    6: "Duminica"
}

b_day_ts = time.mktime(b_day)
print(time.strftime("%Y", b_day))