def numbers_letters_count(my_str):
    num = sum(bool(i.isdigit())
          for i in my_str)
    print(num)
    return [num] + [(len(my_str) - num)]



print(numbers_letters_count("Python 3.6.3"))
