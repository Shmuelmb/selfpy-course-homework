kh = {'first_name':  'Mariah', 'last_name': 'Carey', 'birth_date': '27.03.1970', 'hobbies': ['Sing', 'Compose', 'Act']}

x = input("enter number between 1-7: ")
x = int(x)
if x == 1:
    print(kh['last_name'])
    

if x == 2:
    print(kh['birth_date'][3:5])
    

if x == 3:
    print(len(kh['hobbies']))
   

if x == 4:
    print(kh['hobbies'][2])
   
        
if x == 5:
    kh['hobbies'] += ['Cooking']
    print(kh['hobbies'])
   

if x == 6:
    kh['birth_date'] = kh['birth_date'].split('.')
    kh['birth_date'] = tuple(kh['birth_date'])
    print(kh['birth_date'])
   

if x == 7:
    kh['age'] = 52
    print(kh['age'])
   

   
