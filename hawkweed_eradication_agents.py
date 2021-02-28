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
        self.target       = None
        self.path         = None
        self.max_hawkweed = None
        self.map          = None

    def choose_move(self, location, valid_moves, hawkweed, threshold, growth, spread):
        max_hawkweed_now = max(hawkweed.values()) # the maximum number of hawkweed detected now
        max_hawkweed_loc = max(hawkweed, key = hawkweed.get)  # the location of the maximum number of hawkweed detected now
        num_same_MAX     = list(hawkweed.values()).count(max_hawkweed_now) # the number of locations where have the same maximum number of hawkweed detected now
        
        if max_hawkweed_now == 0:  
            return location

        # if second max_num is near by:
        #     return the second one
        
        if num_same_MAX == 1: # 1.没有找到目标 2.有一个目标但又找到个比现在目标大的目标 3.目标相同
            if self.target is None or max_hawkweed_loc != self.target:
                self.target       = max_hawkweed_loc
                self.max_hawkweed = max_hawkweed_now
                self.dijkstra(location, self.locations, self.conn)  
                self.path         = self.create_path(location, max_hawkweed_loc, self.map)
        else: # 1.没有找到目标，同时找到多个max 2.有一个目标但是又找到多个比现在目标大的目标 3.目标相同
            max_hawkweeds_Group = [key for (key,value) in hawkweed.items() if value == max_hawkweed_now]
            if self.target is None or self.target not in max_hawkweeds_Group:
                self.dijkstra(location, self.locations, self.conn)
                minimal_step        = None
                temp_choose         = None
                temp_path           = None
                
                for des in max_hawkweeds_Group:
                    des_path = self.create_path(location, des, self.map)
                    if temp_choose is None or minimal_step >= len(des_path):
                        if minimal_step == len(des_path) and (len(self.conn[temp_choose]) > len(self.conn[des])):
                            continue
                        if minimal_step == len(des_path) and (len(self.conn[temp_choose]) == len(self.conn[des])):
                            temp_path     = self.create_path(location, temp_choose, self.map)
                            tmp_total_Hak = sum(list([value for key,value in hawkweed.items() if key in temp_path]))
                            des_total_Hal = sum(list([value for key,value in hawkweed.items() if key in des_path]))
                            if tmp_total_Hak > des_total_Hal:
                                continue
                        minimal_step = len(des_path)
                        temp_choose  = des
                self.path = self.create_path(location, temp_choose, self.map)
            
        next_loc = self.path[0]
        if next_loc == self.target:
            self.path         = None
            self.target       = None
            self.max_hawkweed = None
            self.map          = None
        else:
            self.path.remove(next_loc)
        return next_loc

    def dijkstra(self, location, all_locations, conn_dict):
        
        S                 = location
        visited_locations = dict([(x, False)        for x in all_locations])
        distance_table    = dict([(x, float("inf")) for x in all_locations])
        path_table        = dict([(x, None)         for x in all_locations])
        Q                 = PriorityQueue()
        
        distance_table[S] = 0
        Q.put((0, S))
        
        while (not Q.empty()):
            node_U = Q.get()[1]
            
            if visited_locations[node_U]:
                continue
            
            visited_locations[node_U] == True
            
            conn_edges = conn_dict[node_U]
            
            for edge in conn_edges:
                if not visited_locations[edge] and 1 + distance_table[node_U] < distance_table[edge]:
                    distance_table[edge] = 1 + distance_table[node_U]
                    Q.put((distance_table[edge], edge))
                    path_table[edge] = node_U
        self.map = path_table
        
        
    def create_path(self, S, destination, path_table):
        parent_path = path_table[destination]
        shortest_path = []
        shortest_path.append(destination)
        while (parent_path != S):
            shortest_path.append(parent_path)
            parent_path = path_table[parent_path]
        
        shortest_path.reverse()
        
        return shortest_path
        # self.path = shortest_path
        
               
        
        
        
