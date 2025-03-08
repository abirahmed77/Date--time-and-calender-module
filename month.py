import calendar

year = int(input("Enter the Year : "))
month = int(input("Enter the Month as Integer : "))

month = calendar.month(year, month)

print(month)