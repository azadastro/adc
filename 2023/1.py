
spelled_digits =["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
def find_first_digit(in_str: str, flag: bool):
    emp_str = ""
    for ch in in_str:
        emp_str += ch
        if ch.isdigit():
            min_index = 1000
            for i, s_digit in enumerate(spelled_digits):
                if flag:
                    s_digit = s_digit[::-1]
                if s_digit in emp_str:
                    if emp_str.find(s_digit) < min_index:
                        min_index =emp_str.find(s_digit)
                        ch = str(i+1)
            return ch
        

with open("1.txt" , "r") as f:
    input_param = f.readlines()

numbers = []
for line in input_param:
    fst_digit = find_first_digit(line, False)
    scn_digit = find_first_digit(line[::-1], True)
    numbers.append(int(fst_digit+scn_digit))
    
    
print(sum(numbers))