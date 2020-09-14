import numpy as np
import pandas as pd
import random, copy
import helper_heu as hh
from helper_heu import log_time

"""
This scripts solves an 8-Puzzle Game using Depth-First-Algo
with Heuristics, it solves few dis-ordered start states efficiently,
work is in progress to solve more complex start states.
"""

#Solves only two puzzles for now
#start_array = np.array([[1,2,3],[4,0,5],[7,8,6]]) and
#start_array = np.array([[1,2,3],[4,0,8],[7,6,5]])

#Initialize the start state
start_array_ = np.array([[1,2,3],[4,0,8],[7,6,5]])
df_ = pd.DataFrame(start_array_, columns=['A', 'B', 'C'], index=['A', 'B', 'C'])
#Initialize end state
end_array_ = np.array([[1,2,3],[4,5,6],[7,8,0]])
#Initialize loop lenght
number_of_iter_ = 100

#call logginh decorator
@log_time
#wrap code in function
def dfs(start_array,end_array,df,number_of_iter):
    #Inititialize variables used in iteration
    while_stopper = 0
    node =[]
    interupt = 0

    while while_stopper<number_of_iter:
        #Main loop code below
        if while_stopper <1:
            starter = start_array
            if __name__ == '__main__':
                print("first loop with start array shown below: ")
                print(df.head())
                print("***********************************************")
            pass
        else:
            #Initalize starter as result of last loop
            starter = next_loop
        #Get the first layer of the node from start state
        current_level = hh.tree_switch(starter)
        heur_list_layer1 = []
        lopper = 0
        for state in current_level:
            #Appends into empty list the Heuristic value for each node
            heur_list_layer1.append(hh.heur(state,end_array))
    #Checks if any of the nodes in the first layer solves the puzzle, if this is yes,end loop
            if np.array_equal(state,end_array):
                df_s = pd.DataFrame(state, columns=['A', 'B', 'C'], index=['A', 'B', 'C'])
                if __name__ == '__main__':
                    print("Solved:")
                    print(df_s.head())
                break
        if interupt >=1:
            if __name__ == '__main__':
                print("***********************************************")
                print("Step of solution shown below: ")
            node.append(state)
            for i in node:
                df_sn = pd.DataFrame(i, columns=['A', 'B', 'C'], index=['A', 'B', 'C'])
                if __name__ == '__main__':
                    print(df_sn.head())
                    print("**********")
            return df_s
            #break #Break will be used if we remove the function wraper
        #Get the index of the minimum heuristic value and select corresponding nodes
        #as first chosen state
        index_minimum = heur_list_layer1.index(min(heur_list_layer1))
        first_chosen_state = current_level[index_minimum]
        #Get the index of the next minimum heuristic value and select corresponding nodes
        #as second chosen state
        heur_list_layer_temp = copy.deepcopy(heur_list_layer1)
        heur_list_layer_temp[index_minimum]=10000
        next_index_minimum = heur_list_layer_temp.index(min(heur_list_layer_temp))
        second_chosen_state = current_level[next_index_minimum]
        #Get a list of np.arrays with children of firt and second chosen states
        next_levelA = hh.tree_switch(first_chosen_state)
        next_levelB = hh.tree_switch(second_chosen_state)
        #Initialize empty list to keep the heuristic values of the first and second chosen states
        heur_list_layer2A = []
        heur_list_layer2B = []
        #Loop through the first ad second chosen states and store the heuristic value in empty list
        for optionA,optionB in zip(next_levelA, next_levelB):
            heur_list_layer2A.append(hh.heur(optionA,end_array))
            heur_list_layer2B.append(hh.heur(optionB,end_array))
    #Checks if any of the nodes in the first layer solves the puzzle, if this is yes, end loop
            if np.array_equal(optionA,end_array):
                df_s = pd.DataFrame(optionA, columns=['A', 'B', 'C'], index=['A', 'B', 'C'])
                if __name__ == '__main__':
                    print("Solved:")
                    print(df_s.head())
                    print("***********************************************")
                node.append(first_chosen_state)
                node.append(optionA)
                interupt +=1
                break
            if np.array_equal(optionB,end_array):
                df_s = pd.DataFrame(optionB, columns=['A', 'B', 'C'], index=['A', 'B', 'C'])
                if __name__ == '__main__':
                    print("Solved:")
                    print(df_s.head())
                    print("***********************************************")
                node.append(second_chosen_state)
                node.append(optionB)
                interupt +=1
                break
        if interupt >=1:
            if __name__ == '__main__':
                print("Step of solution shown below: ")
            # print(node)
            for i in node:
                df_sn = pd.DataFrame(i, columns=['A', 'B', 'C'], index=['A', 'B', 'C'])
                if __name__ == '__main__':
                    print(df_sn.head())
                    print("**********")
            return df_s
            #break #Break will be used if we remove the function wraper
        #Get the nodes with minimum heuristic value in the sub-nodes of te first_chosen_state
        #and second_chosen_state
        min_index_branchA = min(heur_list_layer2A)
        min_index_branchB = min(heur_list_layer2B)
        #If minimum heuristic in sub branchA is greater that minimum heuristic in parent
        #branch, sort through the sub-branch to select a node from smallest heuristic to
        #the largest heuristic and select the node that is not in not sames as it first
        #chosen state and is not same as the last selected state.
        if min_index_branchA>min(heur_list_layer1):
            test_sort_A = []
            test_sort_A.extend(heur_list_layer2B)
            test_sort_A.sort()
            for i in test_sort_A:
                next_loopA = next_levelA[heur_list_layer2A.index(min_index_branchA)]
                if not np.array_equal(next_loopA, first_chosen_state):
                    if node is None:
                        break
                    else:
                        for i in node:
                            if not np.array_equal(next_loopA, i):
                                break
        #If minimum heuristic in sub branchA is smaller that minimum heuristic in parent
        #branch, select this node and check that it is not equal to parant node or
        #any of the previously selected nodes
        else:
            next_loopA = next_levelA[heur_list_layer2A.index(min_index_branchA)]
            if not np.array_equal(next_loopA, first_chosen_state):
                if node != None:
                    for i in node:
                        if np.array_equal(next_loopA, i):
                            lopper += 1
                    if lopper >= 1:
                        next_loopA = next_levelA[random.randint(0,len(next_levelA)-1)]
            else:
                next_loopB = next_levelB[random.randint(0,len(next_levelB)-1)]

        #If minimum heuristic in sub branchB is greater that minimum heuristic in parent
        #branch, sort through the sub-branch to select a node from smallest heuristic to
        #the largest heuristic and select the node that is not in not sames as it first
        #chosen state and is not same as the last selected state.
        if min_index_branchB>min(heur_list_layer1):
            test_sort_B = []
            test_sort_B.extend(heur_list_layer2B)
            test_sort_B.sort()
            for i in test_sort_B:
                next_loopB = next_levelB[heur_list_layer2B.index(min_index_branchB)]
                if not np.array_equal(next_loopB, second_chosen_state):
                    if node is None:
                        break
                    else:
                        for i in node:
                            if not np.array_equal(next_loopB, i):
                                break
        #If minimum heuristic in sub branchB is smaller that minimum heuristic in parent
        #branch, select this node and check that it is not equal to parant node or
        #any of the previously selected nodes
        else:
            next_loopB = next_levelB[heur_list_layer2B.index(min_index_branchB)]
            if not np.array_equal(next_loopB, second_chosen_state):
                if node != None:
                    for i in node:
                        if np.array_equal(next_loopB, i):
                            lopper += 1
                    if lopper >= 1:
                        next_loopB = next_levelB[random.randint(0,len(next_levelB)-1)]
            else:
                next_loopB = next_levelB[random.randint(0,len(next_levelB)-1)]
        #For loop checks the node with the smallest heursitics between the sub-nodes of
        #the first and second chosen states and saves its for next iterations, alsosaves it for
        #in an array of all slected nodes.
        if hh.heur(next_loopA, end_array)>=hh.heur(next_loopA, end_array):
            next_loop = next_loopA
            node.append(first_chosen_state)
            node.append(next_loopA)
            node.append(next_loop)
        else:
            next_loop = next_loopB
            node.append(second_chosen_state)
            node.append(next_loopB)
            node.append(next_loop)
        #Prevents infinite loop
        if while_stopper==(number_of_iter-1):
            if __name__ == '__main__':
                print("Loop ending, no solution. Suggest increasing loop lenght")
                print("Steps to current state: ")
                print(node)
        while_stopper +=1


#Call DFS function
if __name__ == '__main__':
    dfs(start_array_,end_array_,df_,number_of_iter_)
