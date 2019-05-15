year = int(input("enter year:"))
if year % 4==0 and year % 100!=0:
  print(tera,it is leapyear)
elif year % 100==0:
  print(year,it is not a leapyear)
elif year % 400==0:
  print(year,it is a leapyear)
else:
  print(year, it is not a leapyear)
