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
        self.target       = None # This is the target location which has the maximum Hawkweed
        self.path         = None # This is the path to the target location 
        self.max_hawkweed = None # This is the maximum of the Hawkweed at the target location 
        self.map          = None # This is the dijkstra map

    def choose_move(self, location, valid_moves, hawkweed, threshold, growth, spread):
        """ Using given information, return a valid move from valid_moves.
            Returning an invalid move will cause the system to stop.

            This agent will find to locate the spot which has the maximum number of Hawkeed and then using the dijkstra to find
            the shortest path to it, and it will also generate a path(which will be stored in self.path) which can help the agent
            to go straight through the destination without calculating the dijkstra algorithm again and again when the location of the 
            the maximum number of Hawkeed is not changed.
            
            When there are multiple locations with the same maximum number of Hawkeed, the agent will choose a path according this two 
            criterion 1. the number of connections of the target location -- if this location have more connections, the agent will more tempting to 
                                                                             to select 
                      2. total number of Hawweed in the path to the target -- if this path have more Hawkeed, then it is very danger to let it grow freely,
                                                                              so the agent should choose the path which contains more Hawkweed

            (HawkweedEradicationAgent, str, [str], [str], { str : float }, float, float, float) -> str
        """
        max_hawkweed_now = max(hawkweed.values())                          # the maximum number of hawkweed detected now
        max_hawkweed_loc = max(hawkweed, key = hawkweed.get)               # the location of the maximum number of hawkweed detected now
        num_same_MAX     = list(hawkweed.values()).count(max_hawkweed_now) # the number of locations where have the same maximum number of hawkweed detected now
        # all the Hawkweed are Eradicated
        if max_hawkweed_now == 0:  
            return location
        # if the agent only find one location which has the maximum number of hawkweed
        if num_same_MAX == 1: 
            if self.target is None or max_hawkweed_loc != self.target: # 1.There is no target so create one 2. or there is one but the agent find another one
                self.target       = max_hawkweed_loc
                self.max_hawkweed = max_hawkweed_now
                self.dijkstra(location, self.locations, self.conn)  
                self.path         = self.create_path(location, max_hawkweed_loc, self.map)
        # if the agent only find lots of locations which has the same maximum number of hawkweed        
        else:
            max_hawkweeds_Group = [key for (key,value) in hawkweed.items() if value == max_hawkweed_now] # list of all the hawkweed locations with maximum number
            if self.target is None or self.target not in max_hawkweeds_Group: # 1.There is no target so create one 2. or there is one but the agent find another one not in the group
                self.dijkstra(location, self.locations, self.conn)
                minimal_step        = None # the number of the step of the temporary choosen path
                temp_choose         = None # temporary choosen location which may be used
                temp_path           = None # temporary choosen path which may be used
                # for every potential destination, find the best one 
                for des in max_hawkweeds_Group:
                    des_path = self.create_path(location, des, self.map)
                    if temp_choose is None or minimal_step >= len(des_path):
                        if minimal_step == len(des_path) and (len(self.conn[temp_choose]) > len(self.conn[des])): # use the number of connections to find the path
                            continue 
                        if minimal_step == len(des_path) and (len(self.conn[temp_choose]) == len(self.conn[des])): # use the total number of Hawweed in the path to find the path
                            temp_path     = self.create_path(location, temp_choose, self.map)
                            tmp_total_Hak = sum(list([value for key,value in hawkweed.items() if key in temp_path]))
                            des_total_Hal = sum(list([value for key,value in hawkweed.items() if key in des_path]))
                            if tmp_total_Hak > des_total_Hal:
                                continue
                        minimal_step = len(des_path)
                        temp_choose  = des
                self.path = self.create_path(location, temp_choose, self.map)
        # generate the next step    
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
        """ This function will use the dijkstra algorithm of finding the shortest path of weighted graph, since the distance of the edge in the graph of this assignment is 
            the same, so we can assumed that the distance between two vertice is 1.0 and we also know the source point and the destination point, the connections
            is also stored in the dictionary, so it is suitable to use dijkstra to generate the path

            (self, str, [str], {str:[str]}) -> None
        """
        S                 = location                                         # source location
        visited_locations = dict([(x, False)        for x in all_locations]) # locations that are visited
        distance_table    = dict([(x, float("inf")) for x in all_locations]) # distance to the source point
        path_table        = dict([(x, None)         for x in all_locations]) # store the parent location of each location
        Q                 = PriorityQueue()                                  # the queue that stores all the selected loctions
        
        distance_table[S] = 0
        Q.put((0, S))
        # relaxing the graph
        while (not Q.empty()):
            node_U = Q.get()[1]
            
            if visited_locations[node_U]:
                continue
            
            visited_locations[node_U] == True
            
            conn_edges = conn_dict[node_U]
            
            for edge in conn_edges:
                if not visited_locations[edge] and 1 + distance_table[node_U] < distance_table[edge]: # if the distance can be updated
                    distance_table[edge] = 1 + distance_table[node_U]
                    Q.put((distance_table[edge], edge))
                    path_table[edge] = node_U
        self.map = path_table
        
        
    def create_path(self, S, destination, path_table):
        """ This function will create the shortest path by using the result of the dijkstra algorithm, the path is a list which starts from
            the next proper step, end at the destination location e.g ["next step location",......, Destination]

            (self, str, str, {str:str}) -> [str]
        """
        parent_path   = path_table[destination] # the next step location
        shortest_path = []                      # path
        shortest_path.append(destination)
        while (parent_path != S):
            shortest_path.append(parent_path)
            parent_path = path_table[parent_path]
        # reverse it so that it can end at destination
        shortest_path.reverse()
        
        return shortest_path
        
        
               
        
        
        
