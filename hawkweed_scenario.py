""" File name:   hawkweed_scenario.py
    Author: Yixi Rao
    Date: 27/02/2021
    Description: This file represents a scenario simulating the spread of 
                hawkweed through Kosciuszko National Park and its
                surroundings. It should be implemented for Part 1 of 
                Exercise 4 of Assignment 0.

                See the lab notes for a description of its contents.
"""


class HawkweedScenario:
    def __init__(self):
        self.threshold = 0.0
        self.growth = 0.0
        self.spread = 0.0
        self.locations = []
        self.location = ""
        self.hawkweed = {}
        self.conn = {}

    def read_scenario_file(self, path_to_scenario_file):
        """ This function will take a file path to scenario file, and will retuen the execution result to let the user know whether the
            file loading is success or not.
        
            (self, str) -> bool
        """
        try:
            with open(path_to_scenario_file) as scenario_file:
                for line in scenario_file:
                    line = line[:-1]
                    cutting_line = line.split(" ")
                    name = cutting_line[0]
                    # initialization starts
                    if name == "threshold":
                        self.threshold = float(cutting_line[1])
                    elif name == "growth":
                        self.growth = float(cutting_line[1])
                    elif name == "spread":
                        self.spread = float(cutting_line[1])
                    elif name == "start":
                        self.location = cutting_line[1]
                    elif name == "hawkweed":
                        self.hawkweed[cutting_line[1]] = float(cutting_line[2])
                    elif name == "location":
                        self.locations.append(cutting_line[1])
                    else:
                        if cutting_line[1] not in self.conn:
                            self.conn[cutting_line[1]] = set()
                        self.conn[cutting_line[1]].add(cutting_line[2])

                        if cutting_line[2] not in self.conn:
                            self.conn[cutting_line[2]] = set()
                        self.conn[cutting_line[2]].add(cutting_line[1]) 
                    # leak filling
                    for loc in self.locations:
                        if loc not in self.hawkweed:
                            self.hawkweed[loc] = 0.0
                        if loc not in self.conn:
                            self.conn[loc] = set()
        except IOError: # catch an IO error
            return False
        else:
            return True



    def valid_moves(self):
        """ This function will retuen all the valid moves. a list of valid moves. Each
            valid move is either a neighbouring location or the current location of the
            agent (which indicates that the agent stays put).
        
            (self) -> list
        """
        ans = list(self.conn[self.location])
        ans.append(self.location)
        return ans

    def move(self, loc):
        """ This method should move the agent to the specified
            location and eradicate the hawkweed population there
            
            (self, str) -> none
        """
        if loc not in self.valid_moves():
            raise ValueError("{} is not a valid location".format(loc))
        self.location = loc
        self.hawkweed[loc] = 0.0

    def spread_hawkweed(self):
        """ This method should spread hawkweed according the
            threshold, growth, spread, and connections between locations.
            
            (self) -> none
        """
        const_threshold = self.threshold
        const_growth    = self.growth
        const_spread    = self.spread
        Agent_location  = self.location
        new_hawkweed    = {}
        # first grow
        for loc,num in self.hawkweed.items():
            if loc == Agent_location:
                new_hawkweed[loc] = 0.0
                continue

            new_hawkweed[loc] = num * (1.0 + const_growth)
        # collect others spread
            adj_locs = self.conn[loc]
            for adj_loc in adj_locs:
                adj_num = self.hawkweed[adj_loc]
                if adj_loc != Agent_location and adj_num >= const_threshold:
                    new_hawkweed[loc] = new_hawkweed[loc] + (adj_num * const_spread)
                
        self.hawkweed = new_hawkweed
                    

