import datetime as dt

y = dt.datetime.now()

p = dt.date(2026, 5, 24)
print(p)

q = dt.datetime(year=2026, month=11, day=5, hour=5, minute=15, second=20)

m = dt.date.today()
n = m + dt.timedelta(days=5)
print(m)
print(n)

print(y.hour)
print(y.day)

print("\n\n- - - - - - - - - - - -\n")

a = dt.datetime.now()
print(a.strftime("%B"))
print(a.strftime("%d/%m/%y"))
print(a.strftime("%d-%m-%Y"))

print(a.strftime("%I:%M:%S %p"))