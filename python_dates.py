from datetime import date, timedelta

today = date.today()
print(today.month)

formated_dates = today.strftime('%m:%d:%Y')
print(formated_dates)

formated_dates = today.strftime('%m:%d:%y')
print(formated_dates)

expiry_dates = today + timedelta(days=30)  # 30 days after
print(expiry_dates)

expiry_dates = today - timedelta(days=30)  # 30 days before
print(expiry_dates)


def differ_days(date1: 1998 - 1 - 16, date2: 2005 - 12 - 25):
    a = date1
    b = date2
    return a - b


print(differ_days((date(2005,12,25)),date(1998,1,16)))

















