x = input("Enter three digits (each digit for one pig): ")

a = int(x[0:1]) + int(x[1:2]) + int(x[2:3]) # סך כל הבלוקים
b = a // 3 # חלוקת הבלוקים ללא שארית
c = (a / 3) - b # השארית במידה ויש 
d = (a % 3) # השארית כמספר שלם
print(a)
print(b)
print(c)
print(d)

print(c == 0.0) # במידה ויש שארית מתקבל פיילס במידה ואין שארית מתקבל טרו

