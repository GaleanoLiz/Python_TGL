#Reversed string

def reverse_string(str:str):
    str_list = list(str)
    str_list.reverse()
    return print(f'The original string is {str}, the reversed string is {"".join(str_list)}')

reverse_string('Hello')