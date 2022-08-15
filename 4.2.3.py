#c = float((5*f - 160) / 9)
#f = float((9*c + 160) / 5)


x = str(input("temp': "))

if "f" in x or "F" in x:

    
    f = (float(x[0:-1]))
    print((5*f - 160) / 9 )
    
else:
    c = float(x[0:-1])
    print((9*c + 160) / 5)
