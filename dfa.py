""" File name:   dfa.py
    Author:      Yixi Rao
    Date:        25/02/2021
    Description: This file defines a function which reads in
                a DFA described in a file and builds an appropriate datastructure.

                There is also another function which takes this DFA and a word
                and returns if the word is accepted by the DFA.

                It should be implemented for Exercise 3 of Assignment 0.

                See the assignment notes for a description of its contents.
"""


def load_dfa(path_to_dfa_file):
    """ This function reads the DFA in the specified file and returns a
        data structure representing it. It is up to you to choose an appropriate
        data structure. The returned DFA will be used by your accepts_word
        function. Consider using a tuple to hold the parts of your DFA, one of which
        might be a dictionary containing the edges.

        We suggest that you return a tuple containing the names of the start
        and accepting states, and a dictionary which represents the edges in
        the DFA.

        (str) -> Object
    """
    initial_states = []
    accepting_states = []
    transitions = {}
    with open(path_to_dfa_file) as dfa_file:
        for line in dfa_file:
            line = line[:-1]
            cutting_line = line.split(" ")
            name = cutting_line[0]
            if name == "initial":
                initial_states = cutting_line[1:]
            elif name == "accepting":
                accepting_states = cutting_line[1:]
            else:
                transitions[cutting_line[1] + " " + cutting_line[2]] = cutting_line[3]
    return (initial_states, accepting_states, transitions)
            


def accepts_word(dfa, word):
    """ This function takes in a DFA (that is produced by your load_dfa function)
        and then returns True if the DFA accepts the given word, and False
        otherwise.

        (Object, str) -> bool
    """

    initial_states = dfa[0][0]
    accepting_states = dfa[1]
    transitions = dfa[2]

    current_state = initial_states

    for index in range(len(word) + 1):
        if index == len(word):
            if current_state in accepting_states:
                return True
            else:
                return False
        else:
            current_char = word[index]
            have_transition = False
            for transition,label in transitions.items():
                two_states = transition.split(" ")
                if two_states[0] == current_state and label == current_char:
                    current_state = two_states[1]
                    have_transition = True
                    break
            if not have_transition:
                return False       


