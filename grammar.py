
# getting input
number_of_non_terminals = int(input())
grammar = {}
for _ in range(number_of_non_terminals):
    raw_inp = input().split(' -> ')
    raw_inp[0] = raw_inp[0].replace('<', '')
    raw_inp[0] = raw_inp[0].replace('>', '')

    grammar[raw_inp[0]] = []
    raw_inp[1] = raw_inp[1].split(' | ')
    for item in raw_inp[1]:
        item = item.replace('<', '')
        item = item.replace('>', '')
        grammar[raw_inp[0]].append(item)

inp_str = input()

non_terminals_list = grammar.keys()


for k in grammar.keys():
    temp = grammar[k].copy()
    for item in temp:
        for i in item:
            if i not in non_terminals_list:
                if i not in inp_str and i != '#':
                    grammar[k].remove(item)
                    break


# generating strings
current_strings = [list(grammar.keys())[0]]
current_strings_2 = []
garbage = current_strings


def check_beginning(s):
    s = list(s)
    new_s = []
    for item in s:
        if item not in non_terminals_list:
            new_s.append(item)
        else:
            break
    
    new_s = ''.join([i for i in new_s])

    return inp_str.startswith(new_s)


def check_end(s):
    indexes = []
    for i in range(len(s)):
        if s[i] in non_terminals_list:
            indexes.append(i)
        
    sub_s = s[max(indexes) + 1:]

    return inp_str.endswith(sub_s)


def check_str(s):
    for i in s:
        if i in non_terminals_list:
            if '#' in grammar[i]:
                s = s.replace(i, '')
            else:
                return False
    return s


def main_func(current_strings, current_strings_2, garbage, grammar, non_terminals_list):
    for _ in range(7):
        for string in current_strings:
            for non_terminal in non_terminals_list:
                if non_terminal in string:
                    right_of_production = grammar[non_terminal]

                    if right_of_production != []:
                        for single_right in right_of_production:
                            if single_right != '#':
                                copy_of_string = string

                                copy_of_string = copy_of_string.replace(non_terminal, single_right)

                                if check_str(copy_of_string) != False:
                                    if check_str(copy_of_string) == inp_str:
                                        print('Accepted')
                                        return

                                for non_terminal_2 in non_terminals_list:
                                    if non_terminal_2 in copy_of_string:
                                        if copy_of_string not in garbage and len(copy_of_string) < len(inp_str) + 1 and check_beginning(copy_of_string) and check_end(copy_of_string):
                                            current_strings_2.append(copy_of_string)
                                        break

        garbage += current_strings_2
        current_strings = current_strings_2
        current_strings_2 = []

    print('Rejected')


main_func(current_strings, current_strings_2, garbage, grammar, non_terminals_list)



