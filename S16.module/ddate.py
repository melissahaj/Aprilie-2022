from datetime import datetime

# formatare data/ora
# print(datetime.now().strftime("%H:%M:%S"))

# formatare data
# print(datetime.now().strftime("%d/%b/%y"))

b_day = datetime(1991, 12, 18)
print(b_day.strftime("%m/%d/%Y"))