print("welcome my bro, this is my crazy program")
x = (input("your list:")) # קלט של מחרוזת לדוגמא: "xxx,xxx,xxx"
list_markt = x.split(",") # המרה של המחרוזת לרשימה
num = input("choice your num:") 
while int(num) < 9:
    
    if num == "1": # מציג את הרשימה
        print(list_markt)
        num = input("choice your num:")
        
    elif num == "2": # מדפיס את מספר הפריטים ברשימה
        print(len(list_markt))
        num = input("choice your num:")
        
    elif num == "3": # חיפוש פריט בתוך הרשימה 
        find_item = input("input your item that you want to find in list:")
        if find_item in list_markt:
            print(True) # קיים
            num = input("choice your num:")
        else:
            print(False) # לא קיים
            num = input("choice your num:")

    elif num == "4": # מספר הפעמים שהפריט קיים
        find_count_item = input("input your iten that you want find his count in the list:")
        len_of_item_in_list = list_markt.count(find_count_item)
        print(len_of_item_in_list)
        num = input("choice your num:")
        
    elif num == "5": # הסרת פריט
        remove_item = input("input your item that you want remove from list:")
        list_markt.remove(remove_item)
        num = input("choice your num:")

    elif num == "6": # הוספת פריט
        up_item = input("input you item thaht you want to add:")
        list_markt.append(up_item)
        print(list_markt)
        num = input("choice your num:")


    elif num == "7": # הצגת פריטים שאינם תקינים
        import string

        list_em_numbers = []
        for numbers in list_markt:
            for ss in numbers:
                if ss in "0123456789":
                    list_em_numbers.append(numbers)

        list_em_len = []
        for len_of_words in list_markt:
            if len(len_of_words) < 3:
                list_em_len.append(len_of_words)
                
                
        print(list_em_len + list_em_numbers)
        num = input("choice your num:")




    elif num == "8": # מחיקת כפילויות ברשימה
        em_prev = []
        for replay_item in list_markt:
            if replay_item not in em_prev:
                em_prev.append(replay_item)
                list_markt = em_prev
        num = input("choice your num:")


    elif num == "9": # יציאה
        print("GoodBye")
        break


    
    
