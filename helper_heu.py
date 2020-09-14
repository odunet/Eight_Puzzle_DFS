import numpy as np
import pandas as pd
import random as rd
import copy, math, time
from functools import wraps
from datetime import datetime

"""
Function hue(a,b);
This function takes in two auguments with must be s
same shape np arrays, the first is the start state,
and the second the goal state. It calculates the
heuristic cost and returns this value as an int type
"""
def heur(a,b):
    empty_List = []
    weight = 0
    for outerL in range(a.shape[0]):
        for innerL in range(a.shape[1]):
            if b[outerL][innerL] == 0:
                continue;
            #get the actual indexes of numbs(1-8) in the start-array
            x,y = (np.where(a==b[outerL][innerL]))[0][0],\
            (np.where(a==b[outerL][innerL]))[1][0]
            #get the abosulte sum difference in indexes between start and end array
            local_heuristic = (math.fabs(x-outerL)+math.fabs(y-innerL))/2
            if local_heuristic != 0:
                weight +=1
            # print(x,y," ",local_heuristic)
            empty_List.append(local_heuristic)
    return sum(empty_List)+weight


"""
Functon tree_switch(a);
This function takes in one augument with must be an
np array. This array is the current state of the tree.
The function returns a python list of n np_arrays with The
various children production state.
"""
def tree_switch(a):
    #Copy the index of the 0 element
    x,y = (np.where(a==0))[0][0],(np.where(a==0))[1][0]

    #Perform a deep copy of 5 element this will utilized for The
    #loop to build a list of possible childreen states
    copy_stateA = [copy.deepcopy(a),copy.deepcopy(a)\
                    ,copy.deepcopy(a),copy.deepcopy(a)\
                    ,copy.deepcopy(a)]

    #Initialize empty list for the possible states
    copy_stateB = []
    for j,i in enumerate(copy_stateA):
        if y != 0 and j==0:
            i[x][y], i[x][y-1] = i[x][y-1], i[x][y]
            copy_stateB.append(i)
        if y != 2 and j==1:
            i[x][y], i[x][y+1] = i[x][y+1], i[x][y]
            copy_stateB.append(i)
        if x != 0 and j==2:
            i[x][y], i[x-1][y] = i[x-1][y], i[x][y]
            copy_stateB.append(i)
        if x != 2 and j==3:
            i[x][y], i[x+1][y] = i[x+1][y], i[x][y]
            copy_stateB.append(i)
    return copy_stateB

"""
Functon log_time();
This decorator function takes in nill augument It logs the time taken to
run the function and the result
"""
def log_time(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        """Function that loggs time"""
        start = time.time()
        res = f(*args, **kwargs)
        stop = time.time()
        with open("func_call_log.txt", "a") as logger:
            logger.write(f'Date: {datetime.now()}, function ran in {stop-start:.3f}seconds, the reached state is \n{res}\n')
        return res
    return wrap
