import unittest
import eight_puzzle_rev0 as epr
import numpy as np
import pandas as pd

#Initialize start state
start_array = np.array([[1,2,3],[4,0,8],[7,6,5]])
df = pd.DataFrame(start_array, columns=['A', 'B', 'C'], index=['A', 'B', 'C'])

#Initialize end state
end_array = np.array([[1,2,3],[4,5,6],[7,8,0]])

#Number of loops
number_of_iter = 100

class SimpleTest(unittest.TestCase):

    # Returns True or False.
    def test(self):
        suggested_node = epr.dfs(start_array,end_array,df,number_of_iter)
        print(suggested_node)
        self.assertTrue(np.array_equal(suggested_node,end_array))

if __name__ == '__main__':
    unittest.main()
