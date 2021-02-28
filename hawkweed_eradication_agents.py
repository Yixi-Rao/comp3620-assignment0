""" File name:   hawkweed_eradication_agents.py
    Author:      Yixi Rao
    Date:        27/02/2021
    Description: This file contains agents which manage and eradicate hawkweed. 
                It is used in Exercise 4 of Assignment 0.
"""

import random
from queue import PriorityQueue

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
        super().__init__(locations ,conn)
        self.target = None
        self.path = None
        self.max_hawkweed = None

    def choose_move(self, location, valid_moves, hawkweed, threshold, growth, spread):
        if max(hawkweed.values()) == 0 and self.path == None:
            return location
        
        max_hawkweed_loc = max(hawkweed, key = hawkweed.get)
            
        if self.target == max_hawkweed_loc:
            next_loc = self.path[0]
            if next_loc == self.target:
                self.path = None
            else:
                self.path.remove(next_loc)
            return next_loc
        elif self.max_hawkweed == max(hawkweed.values()) and hawkweed.values().count(max(hawkweed.values())) > 1:
            next_loc = self.path[0]
            if next_loc == self.target:
                self.path = None
            else:
                self.path.remove(next_loc)
            return next_loc
        else:
            self.target = max_hawkweed_loc
            self.max_hawkweed = max(hawkweed.values())
            self.dijkstra(location, valid_moves, hawkweed, threshold, growth, spread, max_hawkweed_loc)
            
            next_loc = self.path[0]
            if next_loc == self.target:
                self.path = None
            else:
                self.path.remove(next_loc)
            return next_loc

            
            
            
            
        
        
    def dijkstra(self, location, valid_moves, hawkweed, threshold, growth, spread, destination):
        
        S                 = location
        visited_locations = dict([(x, False)        for x in self.locations])
        distance_table    = dict([(x, float("inf")) for x in self.locations])
        path_table        = dict([(x, None)         for x in self.locations])
        distance_table[S] = 0
        
        Q = PriorityQueue()
        Q.put((0, S))
        
        while (not Q.empty()):
            node_U = Q.get()[1]
            
            if visited_locations[node_U]:
                continue
            
            visited_locations[node_U] == True
            
            conn_edges = self.conn[node_U]
            
            for edge in conn_edges:
                if not visited_locations[edge] and 1 + distance_table[node_U] < distance_table[edge]:
                    distance_table[edge] = 1 + distance_table[node_U]
                    Q.put((distance_table[edge], edge))
                    path_table[edge] = node_U
        
        parent_path = path_table[destination]
        shortest_path = []
        shortest_path.append(destination)
        while (parent_path != S):
            shortest_path.append(parent_path)
            parent_path = path_table[parent_path]
        
        shortest_path.reverse()
        self.path = shortest_path
            
        
        
        
