
# states
from unittest import TestResult


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

# string
string_to_be_checked = input()


# print("States: ", states)
# print("Initial state: ", initial_state)
# print("Alphabet: ", alphabet)
# print("Final state: ", final_state)
# print("Transition count: ", transition_count)
# print("Transitions: ", transitions)
# print("String: ", string_to_be_checked)


# main logic
list_of_states = [initial_state]
for char in string_to_be_checked:
    temp = []
    for state in list_of_states:
        for transition in transitions:
            if transition[0] == state and (transition[1] == char or transition[1] == '$'):
                temp.append(transition[2])
            if transition[0] == state and transition[1] == '$':
                t = transition[2]
                for trans in transitions:
                    if trans[0] == t and trans[1] == char:
                        temp.append(trans[2])

    list_of_states = temp


# check if we have reached a final state
is_accepted = False
for f_state in final_state:
    if f_state in list_of_states:
        is_accepted = True


# print the result
if is_accepted:
    print('Accepted')
else:
    print('Rejected')