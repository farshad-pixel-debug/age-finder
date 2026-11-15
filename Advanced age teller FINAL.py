from datetime import datetime
maindate = datetime.now()
year = input("Enter your birth year (YYYY): ")
month = input("Enter your birth month (MM): ")
day = input("Enter your birth day (DD): ")
month2 = maindate.month
year2 = maindate.year
day2 = maindate.day
diffmonth = int(month2) - int(month)
diffyear = int(year2) - int(year)
diffday = int(day2) - int(day)
print("You are ", str(diffyear), "years old", str(diffmonth), "months old and", str(diffday), "days old")