def parse_int(a):
    word_dict = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
        'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10,
        'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15,
        'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19,
        'twenty': 20, 'thirty': 30, 'forty': 40, 'fifty': 50, 'sixty': 60,
        'seventy': 70, 'eighty': 80, 'ninety': 90,
    }

    def func(num):

        c = str(num).split()

        n = 0
        cn = 0



        for w in c:
            if w in word_dict:
                cn += word_dict[w]
            elif w == 'hundred':
                cn *= 100
            elif w == 'thousand':
                cn *= 1000
            elif w == 'million':
                cn *= 100000
            elif w == 'and':
                continue
            elif '-' in w:
                sw = w.split('-')
                cn += sum(word_dict[swd] for swd in sw)
            else:
                n += cn
                cn = 0 
                n += word_dict[w]

        return(n+cn)


    def thou(t):
        return(func(t))

    def mil(m):
        return(func(m))




    a = a.lower()
    c = a.lower().split()
    num = 0

    mi = a.split('million')
    if len(mi)>1:
        x = mil(mi[0].strip())*1000000
        num += x
        a = mi[1]


    th = a.split('thousand')
    if len(th)>1:
        x = thou(th[0].strip()) * 1000
        num += x
        a = th[1]
        
    num += func(a.strip())
    
    
    return num


t = input("Enter string: ")
print(parse_int(t))
