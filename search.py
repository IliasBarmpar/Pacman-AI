# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    from game import Directions
    from util import Stack
 
    
    pathAct = []
    path = Stack()
    exploredSet = set()
    frontier = Stack()
    frontier.push( (problem.getStartState(), Directions.STOP, 0))
    while 1:
        if frontier.isEmpty():
            return []
        currNode = frontier.pop()
        if problem.isGoalState(currNode[0]):
            for i in path.list:
                if i not in frontier.list:
                    pathAct.append(i[1])
            return pathAct
        exploredSet.add(currNode[0])

        checkDeadEnd = 1
        for i in problem.getSuccessors(currNode[0]):
            if i[0] not in exploredSet and i[0] not in frontier.list:
                frontier.push(i)
                path.push(i)
                checkDeadEnd = 0

        if checkDeadEnd:
            for l in reversed(path.list):
                if l != frontier.list[-1]:
                    path.pop();
                else:
                    break
    util.raiseNotDefined()




def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    from game import Directions
    from util import Queue

    pathAct = Queue()
    path = Queue()
    exploredSet = set()
    frontier = Queue()
    frontier.push( (problem.getStartState(), Directions.STOP, 0))
    while 1:
        if frontier.isEmpty():
            return []
        
        currNode = frontier.pop()
        if problem.isGoalState(currNode[0]):
            goTo = currNode
            for item in path.list:
                if item[1] == goTo:
                    pathAct.push(goTo[1])
                    goTo = item[0]
                    continue
            return pathAct.list

        exploredSet.add(currNode[0])
        for i in problem.getSuccessors(currNode[0]):
            if i[0] not in exploredSet and i[0] not in [row[0] for row in frontier.list]:
                frontier.push(i)
                path.push(((currNode),i))

    util.raiseNotDefined()












def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    from game import Directions
    from util import Queue
    from util import PriorityQueue

    pathAct = Queue()
    path = Queue()
    exploredSet = set()
    frontier = PriorityQueue()
    frontier.push( (problem.getStartState(), Directions.STOP, 0), 0 )
    
    while 1:
        if frontier.isEmpty():
            print "OOOOOOPS"
            return []
        #print [row in frontier.heap[]]
        print(' '.join(str(y) for y in frontier.heap))
        costOfCurrNode = frontier.heap[0][0]
        currNode = frontier.pop()
        print "currNode: ", currNode
       
        if problem.isGoalState(currNode[0]):
            #print "isGoalState"
            goTo = currNode
            print "goTo: ", goTo
            for item in path.list:
                print "item: ", item
                if item[1] == goTo:
                    pathAct.push(goTo[1])
                    goTo = item[0]
                    continue
            return pathAct.list
        
        exploredSet.add(currNode[0])
        #print(' '.join(str(y) for y in exploredSet))

        
        for i in problem.getSuccessors(currNode[0]):
            print "i[0]: ", i[0]
            if i[0] not in exploredSet and i[0] not in [row[2][0] for row in frontier.heap]:
                print "  got in."
                frontier.push(i, costOfCurrNode + i[2])
                path.push(((currNode),i))
            #elif i[0] in [row[2][0] for index, row in enumerate(frontier.heap)]:
            elif i[0] in [row[2][0] for row in frontier.heap]:
                for index, row in enumerate(frontier.heap):
                    print "i[0]: ", i[0], " 'vs' ", row[2][0]
                    if i[0] == row[2][0]:
                        if row[0] > costOfCurrNode +i[2]:
                            del frontier.heap[index]
                            frontier.heap.append((costOfCurrNode, row[1], i))
                            path.push(((currNode),i))
                    print index, " ", row
                #TODO check if frontier had more options what happenss
                #frontier.update(i, costOfCurrNode + i)
                print(' '.join(str(y) for y in frontier.heap))
                
                #if row[0] > costOfCurrNode + i[2]:
                    #print "wow"


        print ""
        #print [row[2][0] for row in frontier.heap]
        #print "l: ", l
        #inp = raw_input()
    util.raiseNotDefined()





















def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
