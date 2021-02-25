""" File name:   hawkweed_eradication_agents.py
    Author:      <your name goes here>
    Date:        <the date goes here>
    Description: This file contains agents which manage and eradicate hawkweed. 
                It is used in Exercise 4 of Assignment 0.
"""

import random


class HawkweedEradicationAgent:
    """ A simple hawkweed eradication agent. """

    def __init__(self, locations, conn):
        """ This contructor does nothing except save the locations and conn.
            Feel free to overwrite it when you extend this class if you want
            to do some initial computation.

            (HawkweedEradicationAgent, [str], { str : set([str]) }) -> None
        """
        self.locations = locations
        self.conn = conn

    def choose_move(self, location, valid_moves, hawkweed, threshold, growth, spread):
        """ Using given information, return a valid move from valid_moves.
            Returning an invalid move will cause the system to stop.

            Changing any of the mutable parameters will have no effect on the operation
            of the system.

            This agent will locally move to the highest hawkweed population, if there is
            is no nearby hawkweed, it will act randomly.

            (HawkweedEradicationAgent, str, [str], [str], { str : float }, float, float, float) -> str
        """
        max_hawkweed = None
        max_move = None
        for move in valid_moves:
            if max_hawkweed is None or hawkweed[move] > max_hawkweed:
                max_hawkweed = hawkweed[move]
                max_move = move

        if not max_hawkweed:
            return random.choice(valid_moves)

        return max_move


# Make a new agent here called SmartHawkweedEradicationAgent, which extends HawkweedEradicationAgent and
# acts a bit more sensibly. Feel free to add other helper functions if needed.

class SmartHawkweedEradicationAgent(HawkweedEradicationAgent):
    def __init__(self, locations, conn):
        """ YOUR CODE HERE. """

    def choose_move(self, location, valid_moves, hawkweed, threshold, growth, spread):
        """ YOUR CODE HERE. """
