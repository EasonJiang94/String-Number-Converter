from str2num import solve
def number_to_string(num):
    '''
    For generating the test case
    '''
    ## fake output 555555531
    return "five hundred and fifty five million and five hundred fifty five thousand and five hundred thirty one"

if __name__ == "__main__":
    # for test_num in range(1000000000):
    for test_num in range(1):
        test_num = 555555531 # just use fake input 
        ans_num = solve(test_num)
        if test_num == ans_num:
            print("Pass")
        else:
            print("Fail")
