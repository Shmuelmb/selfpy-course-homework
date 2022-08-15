x = input('enter a file patch: ')
file = open(x)
text = file.read()
y = input('enter a task: ')

l = list(text)
line_number = (text.count('\n'))
s = []

for i in range(len(l)):
    if l[i] == '\n':
      s.append(i)     

      
if y == 'sort':
    strr = (text.split())
    t = []
    for y in strr:
        if y not in t:
            t.append(y)
    print(sorted(t))

if y == 'rev':
    w = []   
    k = ''.join(l[::])
    w = list(k[::-1].split("\n"))
    w.reverse()
    for i in w:
        print(i)     
    
    


if y == 'last':
    num = int(input('enter a number: '))
    k = ''.join(l[s[-num]::])
    print(k)
            
   
                   


        
        
            
            
        
        

        
    
