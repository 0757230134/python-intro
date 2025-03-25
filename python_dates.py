from datetime import date, timedelta, datetime

today=date.today()
print(today.month)

formated_dates=today.strftime('%m:%d:%Y')
print(formated_dates)

formated_dates=today.strftime('%m:%d:%y')
print(formated_dates)

expiry_dates=today+timedelta(days=30) #30 days after
print(expiry_dates)

expiry_dates=today-timedelta(days=30)  #30 days before
print(expiry_dates)


















