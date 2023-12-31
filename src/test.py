from .str2num import solve
from .text_def import *
def number_to_string_3digit(number)->str:
    '''
    Process 3-digit numbers cases seperately
    '''
    if number >= 1000:
        raise ValueError
    if number < 10:
        return single_digit_text[number]
    elif number < 100:
        ten_digit_number = int(number / 10)
        single_digit_number = int(number % 10)
        if ten_digit_number == 0:
            return ""
        elif ten_digit_number == 1:
            if single_digit_number == 0:
                return ten_text[ten_digit_number]
            else: 
                return teen_text[single_digit_number]
        else: 
            # ten_digit_number in the range of [2,9]
            if single_digit_number == 0:
                return "{}".format(ten_text[ten_digit_number])
            else:
                return "{}-{}".format(ten_text[ten_digit_number], 
                                        single_digit_text[single_digit_number])
    else:
        hundred_digit = int(number / 100)
        the_rest = number % 100
        hundred_text = "{} hundred".format(single_digit_text[hundred_digit])
        if the_rest == 0:
            return hundred_text
        return "{} {}".format(hundred_text,number_to_string_3digit(the_rest))

def number_to_string(num):
    '''
    For generating the test case
    '''
    if num > 1e9:
        print("Out of range, the input number should be less than 1e9")
        raise ValueError
    if num >= 1e6: # one million        
        remainder = int(num % 1e6)
        quotient = int(num / 1e6)
        if remainder == 0:
            return "{} million".format(number_to_string_3digit(quotient))
        else:
            return "{} million {}".format(number_to_string_3digit(quotient), 
                                          number_to_string(remainder))
    elif num >= 1e3:
        remainder = int(num % 1e3)
        quotient = int(num / 1e3)
        if remainder == 0:
            return "{} thousand".format(number_to_string_3digit(quotient))
        else:
            return "{} thousand {}".format(number_to_string_3digit(quotient), 
                                          number_to_string(remainder))
    else:
        return number_to_string_3digit(num)




def main():
    import random
    random.seed(5001)
    test_case_amount = int(1e9)
    for cnt, test_num in enumerate(range(test_case_amount)):
        test_str = number_to_string(test_num)
        ans_num = solve(test_str)
        if random.randint(0, 4999) == 0:
            print("Test Case Running : {:08d}/{}\t{}              "
                  .format(cnt, test_case_amount, test_str), end='\r')
        if test_num == ans_num:
            # print("Pass")
            pass
        else:
            print("Fail")
            print("-- str : {}".format(test_str))
            print("-- ans : {}".format(ans_num))
            break
    
    print("                                        ",end="\r")
    print("Congratulation! Pass!")

if __name__ == "__main__":
    main()