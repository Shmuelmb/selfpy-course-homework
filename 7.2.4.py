def seven_boom(end_number):
    import string
    end_number = end_number + 1
    e_list = []
    for num in range(end_number):
        (e_list.append(num))
        if "7" in str(num):
            e_list[num] = "BOOM"
        elif num/7 == num//7:
            e_list[num] = "BOOM"

    return e_list
    

print(seven_boom(57))



