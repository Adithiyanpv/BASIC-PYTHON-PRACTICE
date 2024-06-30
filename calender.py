import calendar

month = int(input("Enter the month in number: "))
year = int(input("Enter the year in number: "))
result = calendar.month(year,month)
print(f"Hence the calender is displayed below: {result}")