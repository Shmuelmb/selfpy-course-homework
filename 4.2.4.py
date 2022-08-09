
import calendar

# 0 = monday - שני
# 1 = tuesday - שלישי
# 2 = Wednesday - רביעי
# 3 = Thursday - חמישי
# 4 = Friday - שישי
# 5 = Saturday - שבת
# 6 = Sunday - ראשון

#dd/mm/yyyy

z = input("Input date in foramt dd/mm/yyyy: " )

#DAY
a = int(z[0:2])

#MONTH
b = int(z[3:5])

#YEAR
c = int(z[6:10])


x = calendar.weekday(c, b, a)

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


