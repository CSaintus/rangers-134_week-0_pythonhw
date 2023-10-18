def hello_name(user_name):
    print("hello_" + user_name + "!")

def first_odds():
    for num in range(1, 101, 2):
        print(num)

def max_num_in_list(a_list):
    if not a_list:
        return None

    max_num = a_list[0]

    for num in a_list[1:]:  
         if num > max_num:
            max_num = num

    return max_num

def is_leap_year(a_year):
    if (a_year % 4 == 0 and a_year % 100 != 0) or (a_year % 400 == 0):
        return True
    else:
        return False

def is_consecutive(a_list):
    if not a_list:
        return False  # Return False for an empty list

    for i in range(len(a_list) - 1):
        if a_list[i] + 1 != a_list[i + 1]:
            return False

    return True


