# Max number from a user defined list

def find_maximum():
    number_list = input('Enter the list of numbers ')
    number_list = number_list[1:-1]
    number_list = number_list.split(',')
    return print(f"The max number of the list is {max(number_list)}")

find_maximum()
    