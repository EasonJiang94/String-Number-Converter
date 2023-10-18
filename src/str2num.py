from .text_def import *
def convert_3_digit_str_to_num(input_str)->int:
    # print(input_str)
    hundred_texts = input_str.split("hundred")
    if len(hundred_texts) > 2:
        print("the input format is wrong :", hundred_texts)
        raise ValueError
    elif len(hundred_texts) == 2:
        ## process 3 digit numbers here
        hundred_digit_str, other_digit_str = hundred_texts
        hundred_digit_str = hundred_digit_str.replace(" ", "")
        hundred_digit_num = text_num_table.get(hundred_digit_str, None)
        if hundred_digit_num is None:
            print("the input format is wrong")
            raise ValueError
        return hundred_digit_num * 100 + convert_3_digit_str_to_num(other_digit_str)
    
    ## process two-digit numbers here
    other_digit_str = hundred_texts[0]
    other_digit_str = other_digit_str.replace(" ", "")
    num_strs = other_digit_str.split("-")
    sum_num = 0
    for num_str in num_strs:
        # print(num_str)
        if len(num_str) == 0:
            continue
        get_num = text_num_table.get(num_str, None)
        if get_num is None:
            print("the input format is wrong")
            raise ValueError
        sum_num += get_num
    # print(sum_num)
    return sum_num
        
        
def solve(input_str)->int:
    '''
    Convert string to int number
    '''
    million_texts = input_str.split("million")
    if len(million_texts) > 2:
        print("the input format is wrong :", million_texts)
        raise ValueError
    elif len(million_texts) == 2:
        ## multi-million numbers cases
        million_digit_str, other_digit_str = million_texts
        return int(convert_3_digit_str_to_num(million_digit_str) * 1e6 + solve(other_digit_str))
    
    ## only for muli-thousand number cases
    thousand_texts = input_str.split("thousand")
    if len(thousand_texts) > 2:
        print("the input format is wrong :", thousand_texts)
        raise ValueError
    elif len(thousand_texts) == 2:
        ## multi-million numbers cases
        thousand_digit_str, other_digit_str = thousand_texts
        return int(convert_3_digit_str_to_num(thousand_digit_str) * 1e3 + solve(other_digit_str))
    return int(convert_3_digit_str_to_num(input_str))

