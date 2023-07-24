import math

try:
    inp_str_list_final = input()

    inp_str_list = inp_str_list_final.split(' ')

    inp_str_list_2 = []
    for item in inp_str_list:
        item = item.replace('(', ' ( ')
        item = item.replace(')', ' ) ')
        item = item.replace('  ', ' ')
        inp_str_list_2.append(item)

    inp_str_list_3 = []
    for item in inp_str_list_2:
        inp_str_list_3 += item.split(' ')

    inp_str_list_final = []
    for item in inp_str_list_3:
        if item != '':
            inp_str_list_final.append(item)


    non_operands = ['+', '-', '*', '/', '^', 'sqrt', 'sin', 'cos', 'tan', 'abs', 'exp', 'ln', '(', ')']
    info_dict = {'stack' : [], 'postfix_result' : [], 'operator_priority' : {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, 'sqrt': 4, 'sin': 4, 'cos': 4, 'tan': 4, 'abs': 4, 'exp': 4, 'ln': 4}}


    # operations for stack
    # check is the stack is empty
    def is_empty():
        if len(info_dict['stack']) == 0:
            return True
        return False

    # push method
    def push(i):
        info_dict['stack'].append(i)

    # pop method
    def pop():
        if not is_empty():
            return info_dict['stack'].pop()

    # top of stack
    def peek():
        return info_dict['stack'][-1]

    # check i
    # check if i is operand
    def is_operand(i):
        if i not in non_operands:
            return True
        return False

    # check if i's priority is less that top of the stack
    def is_not_greater(i):
        try:
            if info_dict['operator_priority'][i] <= info_dict['operator_priority'][peek()]:
                return True
            return False
        except KeyError:
            return False

    # main function for conversion
    def convert_infix_to_postfix(infix_element):
        for i in infix_element:
            # operand
            if is_operand(i):
                info_dict['postfix_result'].append(i)

            # '('
            elif i == '(':
                push(i)

            # ')'
            elif i == ')':
                while ((not is_empty()) and peek() != '('):
                    a = pop()
                    info_dict['postfix_result'].append(a)
                pop()

            # operator
            else:
                while (not is_empty() and is_not_greater(i)):
                    info_dict['postfix_result'].append(pop())
                push(i)

        # pop everything from the stack
        while not is_empty():
            info_dict['postfix_result'].append(pop())

        return info_dict['postfix_result']



    postfix_version_of_input = convert_infix_to_postfix(inp_str_list_final)


    def temp_eval(i):
        if i == '+':
            op1 = float(final_stack.pop())
            op2 = float(final_stack.pop())
            return op1 + op2
        elif i == '-':
            op1 = float(final_stack.pop())
            op2 = float(final_stack.pop())
            return op2 - op1
        elif i == '*':
            op1 = float(final_stack.pop())
            op2 = float(final_stack.pop())
            return op1 * op2
        elif i == '/':
            op1 = float(final_stack.pop())
            op2 = float(final_stack.pop())
            return op2 / op1
        elif i == '^':
            op1 = float(final_stack.pop())
            op2 = float(final_stack.pop())
            return math.pow(op2, op1)
        elif i == 'sin':
            op = float(final_stack.pop())
            return math.sin(op)
        elif i == 'cos':
            op = float(final_stack.pop())
            return math.cos(op)
        elif i == 'tan':
            op = float(final_stack.pop())
            return math.tan(op)
        elif i == 'abs':
            op = float(final_stack.pop())
            return abs(op)
        elif i == 'exp':
            op = float(final_stack.pop())
            return math.exp(op)
        elif i == 'ln':
            op = float(final_stack.pop())
            return math.log(op)


    # final stack
    final_stack = []

    # check if the stack is empty
    def final_stack_is_empty():
        if len(final_stack) == 0:
            return True
        return False

    # pop from stack
    def final_stack_pop():
        if not final_stack_is_empty():
            return final_stack.pop()

    # push to stack
    def final_stack_push(i):
        final_stack.append(i)

    # postfix evaluator
    def final_evaluation(postfix_version_of_input):
        for i in postfix_version_of_input:
            # check if i is operand
            if i not in non_operands:
                final_stack_push(i)
            # check if i is operator
            else:
                final_stack_push(str(temp_eval(i)))
        return "{:.2f}".format(float(final_stack_pop()))


    count_of_open = 0
    count_of_close = 0
    for item in inp_str_list_final:
        if item == '(':
            count_of_open += 1
        elif item == ')':
            count_of_close += 1
    
    if count_of_open == count_of_close:
        print(final_evaluation(postfix_version_of_input))
    else:
        print('INVALID')


except:
    print('INVALID')
