from .text_def import *
def convert_3_digit_str_to_num(input_str)->int:
    hundred_texts = input_str.split("hundred")
    if len(hundred_texts) > 2:
        print("the input format is wrong")
        raise ValueError
    elif len(hundred_texts) == 2:
        ## process 3 digit numbers here
        hundred_digit_str, other_digit_str = hundred_texts
        hundred_digit_str = hundred_digit_str.replace(" ", "")
        hundred_digit_num = text_num_table.get(hundred_digit_str, None)
        if hundred_digit_num is None:
            print("the input format is wrong")
            raise ValueError
        ans_num = hundred_digit_num * 100 + convert_3_digit_str_to_num(other_digit_str)
    if len(hundred_texts) == 1:
        ## process two-digit numbers here
        other_digit_str = hundred_texts[0]
        other_digit_str = other_digit_str.replace(" ", "")
        num_strs = other_digit_str.split("-")
        sum_num = 0
        for num_str in num_strs:
            if len(num_str) == 0:
                continue
            sum_num += convert_3_digit_str_to_num(num_str)
        return sum_num
        

def solve(input_str)->int:
    '''
    Convert string to int number
    '''
    million_texts = input_str.split("million")
    # if
    million_digits = million_texts[0]
    # thousand_texts
    return 0

