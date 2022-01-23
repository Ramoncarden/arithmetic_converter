import re
def arithmetic_arranger(problems, answers=False):
    '''
    Takes a list of string numbers (["32 + 8", "1 - 4"]) and 
    converts to type int. Will print in table format.
    If answers parameter == True, anwers will be displayed. 

    '''
    padding = 2

    for seq in problems:
        nums = seq
        num_1 = int(re.search("([^\s]+)", nums).group())
        
        operand = re.search("[+,-]", nums).group()
        num_2 = int(nums.split(None, 2)[-1])
        
        num_1_len = len(str(num_1))
        num_2_len = len(str(num_2))
        largest_len = num_1_len + padding
        if num_2_len > num_1_len:
            largest_len = num_2_len + padding
        
        print(f"{num_1 : > {largest_len}}") 
        print(f"{operand : <}", end="")
        print(f"{num_2 : > {largest_len - 1}}")
        if answers == True:
            print('-' * largest_len)
            ops = {"+": (lambda x,y: num_1+num_2), "-": (lambda x,y: num_1-num_2)}
            print(f"{ops[operand] (num_1, num_2) : > {largest_len}} ")
        else:
            print('-' * largest_len, end="")


    
arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"])