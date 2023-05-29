kh = {'first_name':  'Mariah', 'last_name': 'Carey', 'birth_date': '27.03.1970', 'hobbies': ['Sing', 'Compose', 'Act']}

x = input("enter number between 1-7: ")
x = int(x)

match x:
    case 1:
        print(kh['last_name'])
        
    case 2:
        print(kh['birth_date'][3:5])
        
    case 3:
        print(len(kh['hobbies']))
    
    case 4:
        print(kh['hobbies'][2])   
            
    case 5:
        kh['hobbies'] += ['Cooking']
        print(kh['hobbies'])
    
    case 6:
        kh['birth_date'] = kh['birth_date'].split('.')
        print(tuple(kh['birth_date']))
    
    case 7:
        kh['age'] = 52
        print(kh['age'])
    

   
