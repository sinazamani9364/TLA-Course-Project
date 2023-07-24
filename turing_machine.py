
def get_char(num):
    str = '#abcdefghijklmnopqrstuvwxyz'
    return str[len(num) - 1]

states = ['q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10']
directions = ['L', 'R']


# getting and processing input
encoded_turing_split = input().split('00')
transitions = {}

finding_final_state = []
for trans in encoded_turing_split:
    trans = trans.split('0')
    transitions[(states[len(trans[0]) - 1], get_char(trans[1]))] = (states[len(trans[2]) - 1], get_char(trans[3]), directions[len(trans[4]) - 1])
    finding_final_state.append(len(trans[0]) - 1)
    finding_final_state.append(len(trans[2]) - 1)


# final state
final_state = states[max(finding_final_state)]


number_of_strings = int(input())
inp_strings = []

for _ in range(number_of_strings):
    inp = input()
    if inp == '':
        inp_strings.append('##########')
    else:
        inp = inp.split('0')
        
        res = '#####'
        for item in inp:
            res += get_char(item)
        res += '#####'

        inp_strings.append(res)
        res = ''


# reading strings
for s in inp_strings:
    current_index = 5
    current_state = states[min(finding_final_state)]
    
    s = list(s)
    for _ in range(100):
        if (current_state, s[current_index]) in transitions:

            ch = s[current_index]
            st = current_state

            current_state = transitions[(st, ch)][0]
            s[current_index] = transitions[(st, ch)][1]

            if transitions[(st, ch)][2] == 'L':
                current_index -= 1
            else:
                current_index += 1
        else:
            if current_state == final_state:
                print('Accepted')
                break
            else:
                print('Rejected')
                break

