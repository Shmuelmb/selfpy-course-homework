import calendar

# 0 = monday - שני
# 1 = tuesday - שלישי
# 2 = Wednesday - רביעי
# 3 = Thursday - חמישי
# 4 = Friday - שישי
# 5 = Saturday - שבת
# 6 = Sunday - ראשון


year = int(input("year: "))
month = int(input("month: "))
day = int(input("day: "))


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


