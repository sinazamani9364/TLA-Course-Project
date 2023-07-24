
# states
states = input()[1: -1].split(',')
initial_state = states[0]

# alphabet
alphabet = input()[1: -1].split(',')

# states
final_state = input()[1: -1].split(',')

# transitions
transition_count = int(input())
transitions = []
for _ in range(transition_count):
    temp = input().split(',')
    transitions.append((temp[0], temp[1], temp[2])) # temp[0] => source, temp[1] => transition, temp[2] => destination


# expanding lambda transitions
for i in range(len(transitions)):
    if (transitions[i])[1] == '$':
        t_source = transitions[i][0]
        t_dest = transitions[i][2]
        for t in transitions:
            if t[2] == t_source:
                transitions.append((t[0], t[1], t_dest))

        for t in transitions:
            if t[0] == t_dest:
                transitions.append((t_source, t[1], t[2]))


transitions_dict = {}
for i in range(len(states)):
    transitions_dict[states[i]] = []

for t in transitions:
    if t[1] != '$':
        transitions_dict[t[0]].append((t[1], t[2]))


# making my state_list
ultimate_states = [[initial_state]]

for s_list in ultimate_states:
    if s_list != 'Trap':
        s_transitions = []
        for s in s_list:
            s_transitions += transitions_dict[s]

        temp_t = []
        for a in alphabet:
            for t in s_transitions:
                if t[0] == a:
                    if t[1] not in temp_t:
                        temp_t.append(t[1])
            if temp_t != []:
                if temp_t not in ultimate_states:
                    ultimate_states.append(temp_t)
                temp_t = []
        
        a_count = 0
        for a in alphabet:
            for t in s_transitions:
                if t[0] == a:
                    a_count += 1
            if a_count == 0:
                if 'Trap' not in ultimate_states:
                    ultimate_states.append('Trap')
            a_count = 0



# ultimate_states_final = []

# if 'Trap' in ultimate_states:
#     ultimate_states_final.append('Trap')
# temp_list = []
# for l in ultimate_states:
#     for i in range(100):
#         if f'q{i}' in l:
#             temp_list.append(f'q{i}')

#     if temp_list not in ultimate_states_final and temp_list != []:
#         ultimate_states_final.append(temp_list)
#     temp_list = []



# print(len(ultimate_states_final))





ultimate_states_final = []
for l in ultimate_states:
    temp = ''
    for item in l:
        temp += item
    ultimate_states_final.append(temp)

ultimate_states_final_2 = []
for s in ultimate_states_final:
    s = ''.join(sorted(s))
    if s not in ultimate_states_final_2:
        ultimate_states_final_2.append(s)




print(len(ultimate_states_final_2))



