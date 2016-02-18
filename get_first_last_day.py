import datetime as dt
from datetime import date, timedelta

def get_first_day(dt, d_years=0, d_months=0):
    # d_years, d_months are "deltas" to apply to dt
    y, m = dt.year + d_years, dt.month + d_months
    a, m = divmod(m-1, 12)
    return date(y+a, m+1, 1)

def get_last_day(dt):
    return get_first_day(dt, 0, 1) + timedelta(-1)


#d = date.today()
d = str(input('put any date of that particular month in format yyyy-mm-dd:'))
print('type of input received:',type(d))
d = dt.datetime.strptime(d, '%Y-%m-%d').date()
print('after date conversion..',d,'type..',type(d))


q = get_first_day(d)
w = get_last_day(d)
