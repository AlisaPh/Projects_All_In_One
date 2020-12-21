from math import fabs
from datetime import datetime
date= datetime.now()
month_now=int(date.strftime("%m"))
year_now=datetime.today().year
from random import randint
rnd_year=randint(1980,year_now)
rnd_month=randint(1,12)
sum_years=year_now-rnd_year
sum_months=int(fabs(month_now-rnd_month))
print(sum_months, "/", sum_years)
