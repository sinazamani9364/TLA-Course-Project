

# states
from operator import truediv
from pickle import TRUE


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


transition_table = {}
for i in range(len(states)):
    transition_table[states[i]] = []

for s in states:
    for a in alphabet:
        for t in transitions:
            if t[0] == s and t[1] == a:
                transition_table[s].append(t[2])


equivalence_list = [[], final_state]
for s in states:
    if s not in final_state:
        equivalence_list[0].append(s)




alphabet_accepted_count = 0


while (True):
    new_equivalence_list = []
    index_ignored = []
    for l in equivalence_list:
        if len(l) >= 2:
            for i in range(len(l) - 1):
                if i not in index_ignored:
                    new_equivalence_list.append([l[i]])
                    index_ignored.append(i)
                    for j in range(i + 1, len(l)):
                        if j not in index_ignored:
                            for k in range(len(alphabet)):
                                for temp_list in equivalence_list:
                                    if transition_table[l[i]][k] in temp_list and transition_table[l[j]][k] in temp_list:
                                        alphabet_accepted_count += 1

                                if alphabet_accepted_count == len(alphabet):
                                    for p in range(len(new_equivalence_list)):
                                        if l[i] in new_equivalence_list[p]:
                                            new_equivalence_list[p].append(l[j])
                                            index_ignored.append(j)

                            alphabet_accepted_count = 0

        else:
            new_equivalence_list.append(l)

        index_ignored = []

    if len(equivalence_list) == len(new_equivalence_list):
        break
    equivalence_list = new_equivalence_list



print(len(equivalence_list))
