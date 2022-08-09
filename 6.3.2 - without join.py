
def format_list(my_list):
    if len(my_list) == 1:
        return (my_list[0])+","
    elif len(my_list) == 2:
        return my_list[0] +"," " ""and " +  my_list[1] 
    elif len(my_list) == 4:
        return my_list[0] +","" "+ my_list[2] +","" ""and " + my_list[3]
    elif len(my_list) == 6:
        return my_list[0]+ ","" "+ my_list[2] + ","" " + my_list[4]+ "," " ""and " + my_list[5]
    elif len(my_list) == 8:
        return my_list[0] +","" "+ my_list[2] +","" "+ my_list[4] +","" "+ my_list[6] +","" ""and " + my_list[8] 
    else:
        return False

my_list = ["hydrogen", "helium", "lithium", "beryllium", "boron", "magnesium"]
print(format_list(my_list))




