
import calendar

# 0 = monday - שני
# 1 = tuesday - שלישי
# 2 = Wednesday - רביעי
# 3 = Thursday - חמישי
# 4 = Friday - שישי
# 5 = Saturday - שבת
# 6 = Sunday - ראשון

#dd/mm/yyyy

input_date = input("Input date in foramt dd/mm/yyyy: ").split("/")

#DAY
day = int(input_date[0])

#MONTH
month = int(input_date[1])

#YEAR
year = int(input_date[2])


x = calendar.weekday(year, month, day)

if x == 0:
    print("Monday")

elif x == 1:
    print("Tuesday")

elif x == 2:
    print("Wednesday")

elif x == 3:
    print("Thursday")

elif x == 4:
    print("Friday")

elif x == 5:
    print("Saturday")

elif x == 6:
    print("Sunday")

else:
    print("none")


