# Project Smart_Calculator
import re

help_command = """The program calculates the sum, subtraction, multiplication, integer division, power of numbers
The program supports variables, parentheses.
Rules for variables:
    - Name of a variable (identifier) can contain only Latin letters;
    - A variable can have a name consisting of more than one letter;
    - The case is also important; for example, n is not the same as N;
    - The value can be an integer number or a value of another variable;
    - It is possible to set a new value to an existing variable;
    - To print the value of a variable you should just type its name;
Example (the greater-than symbol followed by space (>) represents the user input):
> -2 + 4 - 5 + 6
3
> 9 +++ 10 -- 8
27
> 3 --- 5
-2
> 3 + 8 * ((4 + 3) * 2 + 1) - 6 / (2 + 1)
121
> 2*2^3
16
"""

def normalise(expstr):  # function to normalise expression removing the extra '-' or '+'
    norm_str = ''
    sign = -1
    ln = len(expstr)
    for i in range(ln):
        if expstr[i] == '-':
            if expstr[i+1] == '-':
                sign *= -1
                continue
            elif sign > 0:
                norm_str += '+'
            else:
                norm_str += expstr[i]
        elif expstr[i] == '+':
            if expstr[i+1] == '+':
                continue
            else:
                norm_str += expstr[i]
        else:
            norm_str += expstr[i]
    return norm_str


def infix_postfix(infix_exp):   # function to convert infix expression to postfix
    temp_stk = []
    post_stk = []
    prefix = ''
    prd = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    if infix_exp[0] == '-':
        prefix = '-'
        infix_exp = infix_exp.lstrip('-')
    if infix_exp[0] == '+':
        infix_exp = infix_exp.lstrip('+')
    if '--' in infix_exp or '++' in infix_exp:
        infix_exp = normalise(infix_exp)
    for idx, tk in enumerate(infix_exp):
        if tk == ' ':
            continue
        if tk.isnumeric():
            num = ''
            if idx != 0 and infix_exp[idx - 1].lstrip('-').isnumeric():
                num = post_stk.pop()
                num += tk
            elif idx == 0 and prefix:
                post_stk.append(prefix+tk)
            else:
                post_stk.append(tk)
            if num:
                post_stk.append(num)
        elif tk.isalpha():
            if tk in num_dic.keys():
                post_stk.append(num_dic[tk])
            else:
                print('Unknown variable')
                return
        elif tk == '(':
            temp_stk.append(tk)
        elif tk in ('+', '-', '*', '/', '^'):
            if tk == infix_exp[idx+1] and tk in ('*', '/'):
                print('Invalid expression')
                return
            while len(temp_stk) >= 1 and temp_stk[-1] in ('+', '-', '*', '/', '^') and prd[temp_stk[-1]] >= prd[tk]:
                opr = temp_stk.pop()
                post_stk.append(opr)
            else:
                temp_stk.append(tk)
        elif tk == ')':
            temp = temp_stk.pop()
            while temp != '(':
                post_stk.append(temp)
                try:
                    temp = temp_stk.pop()
                except IndexError:
                    print('Invalid expression')
                    return
    while len(temp_stk) != 0:
        opr = temp_stk.pop()
        post_stk.append(opr)
    return post_stk


def postfix_evaluation(pf_stk):  # function to evaluate the postfix expression
    eval_stk = []
    for tk in pf_stk:
        if tk in ('+', '-', '*', '/'):
            oprd1 = eval_stk.pop()
            oprd2 = eval_stk.pop()
            strg = str(oprd2) + tk + str(oprd1)
            try:
                result = eval(strg)
                eval_stk.append(result)
            except SyntaxError:
                print("Invalid expression")
                return
        elif tk == '^':
            oprd1 = int(eval_stk.pop())
            oprd2 = int(eval_stk.pop())
            result = pow(oprd2, oprd1)
            eval_stk.append(result)
        else:
            eval_stk.append(tk)
    print(round(eval_stk.pop()))


def command(com_expr):  # function handling command expression
    if "/exit" in com_expr:
        print("Bye!")
        return True
    elif "/help" in com_expr:
        print(help_command)
    else:
        print('Unknown command')
    return False


def assignment(expstr):  # function handling assignment expression
    regex = re.compile('[-+^*()/=]')
    if '=' in expstr and len(expstr) > 1:
        leftstr = expstr.split('=')[0].strip()
        rgtstr = expstr.split('=')[1].strip()
        if bool(re.match('^(?=.*[0-9])(?=.*[a-zA-Z])', leftstr)):
            print('Invalid identifier')
            return
        elif len(rgtstr) > 1 and rgtstr.isalnum() and not rgtstr.isnumeric() and rgtstr not in num_dic.keys():
            print('Invalid assignment')
            return
    if expstr.count('=') > 1:
        print('Invalid assignment')
        return
    if not regex.search(expstr):
        for item in expstr.split():
            if item in num_dic.keys():
                print(num_dic[item])
                return
            else:
                print('Unknown variable')
                return
    if '=' in expstr:
        lst_exp = expstr.split('=')
        assign = lst_exp[1].strip()
        if not assign.isnumeric():
            if assign in num_dic.keys():
                num_dic[lst_exp[0].strip()] = num_dic[assign]
            else:
                print('Unknown variable')
                return
        else:
            num_dic[lst_exp[0].strip()] = lst_exp[1].strip()
    else:
        pfix_stk = infix_postfix(expstr)
        if pfix_stk:
            postfix_evaluation(pfix_stk)

# Main Body
num_dic = {}
while True:
    expr = input("Expression: > ").strip()
    if not expr:
        continue
    if expr.startswith('/'):
        flag = command(expr)
        if flag:
            break
    elif expr.lstrip('-+')[0].isnumeric():
        postfix_stk = infix_postfix(expr)
        if postfix_stk:
            postfix_evaluation(postfix_stk)
    elif expr[0].isalpha():
        assignment(expr)
    else:
        print('Invalid expression')

