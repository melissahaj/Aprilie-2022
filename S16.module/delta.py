from datetime import datetime

this_year = datetime(2022, 1, 1)
delta = datetime.now() - this_year

print(delta.total_seconds() / 3600)