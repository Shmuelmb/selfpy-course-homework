def numbers_letters_count(my_str):
    num = 0
    for i in my_str:
            if i.isdigit():
                num +=1
    return [num] + [(len(my_str) - num)]



print(numbers_letters_count("Python 3.6.3"))
