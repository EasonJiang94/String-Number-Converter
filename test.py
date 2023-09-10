from str2num import solve

def number_to_string_3digit(number)->str:
    if number >= 1000:
        raise ValueError
    ten_text = {
        1: "ten", 
        2: "twenty", 
        3: "thirty", 
        4: "forty", 
        5: "fifty", 
        6: "sixty", 
        7: "seventy",  
        8: "eighty", 
        9: "ninety"        
    }
    teen_text = {
        1: "eleven", 
        2: "twelve", 
        3: "thirteen",  
        4: "fourteen", 
        5: "fifteen", 
        6: "sixteen", 
        7: "seventeen", 
        8: "eighteen", 
        9: "nineteen"
    }
    single_digit_text = {
        0: "zero", 
        1: "one", 
        2: "two", 
        3: "three",  
        4: "four", 
        5: "five", 
        6: "six", 
        7: "seven", 
        8: "eight", 
        9: "nine"
    }
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
    else :
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
    # fake output 555555531
    return "five hundred fifty-five million five hundred fifty-five thousand five hundred thirty-one"
   



if __name__ == "__main__":
    # for test_num in range(1000000000):
    for test_num in range(1000):
        print(number_to_string_3digit(test_num))
    for test_num in range(1):
        test_num = 555555531 # just use fake input 
        ans_num = solve(test_num)
        if test_num == ans_num:
            print("Pass")
        else:
            print("Fail")
