# 8 Puzzle Solver (Depth-First Algorithm)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

This scripts solves an 8-Puzzle Game using Depth-First-Algo with Heuristics, it solves few dis-ordered start states efficiently, work is in progress to solve more complex start states.

Current solvable Start states, code is ongoing upgrade to be able to solve more complex start states:
```
start_array = np.array([[1,2,3],[4,0,5],[7,8,6]])
start_array = np.array([[1,2,3],[4,0,8],[7,6,5]])
```

### Contributing

To contribute to the project, you need to fork the repo and initiate a pull request to the branch below:

* Pull Reception
```sh
git push -u origin PullReception
```

### Tech

Some of the libraries used in the project to work properly:

* Pandas - Data manipulation library
* Numpy - Data manipulation library

### Installation
```sh
$ env2/bin/pip install -r requirements.txt
```

### Testing

You can contribute to this code "Open Source" by initiating a pull request modifying and merging your code to this GitHub repo. Note that ContinuousIntergration (CI) is enabled using CircleCI for this repo. Thus, all merge request will be testing before mergin
#### Running the test
```sh
$ env2/bin/python 8Puzzle.text.py
```
This test is enabled using Python's **unittesting** library, code snippet below:
```
#Main body of the unit test function, checking if suggested node is sames as end node
def test(self):
    suggested_node = epr.dfs(start_array,end_array,df,number_of_iter)
    print(suggested_node)
    self.assertTrue(np.array_equal(suggested_node,end_array))
```


License
----

MIT
