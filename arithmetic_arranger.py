import re


def arithmetic_arranger(problems, solutions=False):
    '''
    Takes a list of string numbers (["32 + 8", "1 - 4"]).
    Loops through list of numbers and taks all first numbers,
    operands, and second numbers and appends to strings named
    tops, operands and bottoms repectively. Will return a string comprised
    of all tops, operands, and bottoms which will print 
    all numbers horizontally creating a table of math problems. 
    Ex:
      32        1     9999     523
    +  8   - 3801   + 9999   -  49
    ----   ------   ------   -----
    '''
    # Variables will be appended to then combined to return a single string with all data.
    if len(problems) > 5:
        return "Error: Too many problems."

    padding = 2
    tops = ""
    bottoms = ""
    lines = ""
    answer = ""
    string = ""

    for seq in problems:
        # handle error exception cases
        if(re.search("[^\s0-9.+-]", seq)):
            if(re.search("[/]", seq) or re.search("[*]", seq)):
                return "Error: Operator must be '+' or '-'."
            return "Error: Numbers must only contain digits."
        
        num_1 = int(re.search("([^\s]+)", seq).group())
        
        operand = re.search("[+,-]", seq).group()
        
        num_2 = int(seq.split(None, 2)[-1])
        
        #Capture len between two items to use as padding for both during printing
        num_1_str = str(num_1)
        num_2_str = str(num_2)

        if len(num_1_str) >= 5 or len(num_2_str) >= 5:
            return "Error: Numbers cannot be more than four digits."
 
        largest_len = max(len(num_1_str), len(num_2_str)) + padding

        ops = {"+": (lambda x,y: num_1+num_2), "-": (lambda x,y: num_1-num_2)}
        evaluate = ops[operand] (num_1, num_2)

        top = num_1_str.rjust(largest_len)
        bottom = operand + num_2_str.rjust(largest_len - 1)
        line = "-" * largest_len
        res = str(evaluate).rjust(largest_len)

        # Check for last problem to avoind adding unnecessary spacing
        if seq != problems[-1]:
            tops += top + '    '
            bottoms += bottom + '    '
            lines += line + '    '
            answer += res + '    '
        else:
            tops += top
            bottoms += bottom
            lines += line
            answer += res

    # Add answers if answers=True then return string  
    if solutions == True:
        string = tops + "\n" + bottoms + "\n" + lines + "\n" + answer
    else:
        string = tops + "\n" + bottoms + "\n" + lines
    print(string)
    return string
        
        
arithmetic_arranger(["3 + 855", "988 + 40"], True)