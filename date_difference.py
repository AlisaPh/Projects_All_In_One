from datetime import datetime
date= datetime.now()
month_now=date.strftime("%m")
year_now=datetime.today().year
from random import randint
rnd_year=randint(1980,year_now)
rnd_month=randint(1,12)