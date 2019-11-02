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
    from util import Stack

    pathAct = []
    path = Queue()
    exploredSet = set()
    frontier = Queue()
    frontier.push( (problem.getStartState(), Directions.STOP, 0))
    while 1:
        if frontier.isEmpty():
            return []
        
        currNode = frontier.pop()
        moveTo = currNode
        print "currNode:", currNode

        if problem.isGoalState(currNode[0]):
            indexes = []

            print "////////////////////////////"
            print "Start:", problem.getStartState()
            print "////////////////////////////"
            for i in path.list:
                print i
            print "////////////////////////////"
            return []
            print(" \-/ ".join(str(y) for y in path.list))
            print ""
            print ""
            backtraceNode = path.list[0][0]
            pathAct = path.list[0][1][1]
            print "1:", path.list[0][0]
            print "2:", path.list[0][1][1]
            while 1:
                break

            pathActAct = Queue()
            goTo = path.list[0][1]
            for index, item in enumerate(path.list):
                #print(index, item)
                #print "->", item[1], " | ", goTo
                if item[1] == goTo:
                    pathActAct.push(goTo[1])
                    goTo = item[0]
                    #print "  >goTo: ", goTo
                    continue
                else:
                    #print "  >else"
                    indexes.append(index)
                
            for ind in reversed(indexes):
                path.list.pop(ind)
            return pathActAct.list
            print(" - ".join(str(y) for y in pathActAct.list))
            print(" - ".join(str(y) for y in indexes))
            print(" \-/ ".join(str(y) for y in path.list))
            inp = raw_input()




            return []

            print ""
            print(" \\\-/// ".join(str(y) for y in path.list))
            print ""
            print ""
            while 1:
                inp = raw_input()
                print "node: ", currNode
                successorz = problem.getSuccessors(currNode[0])
                #find correct successor
                for i in successorz:
                    print "  sc:", i
                    print "  DR", Directions.REVERSE[currNode[1]]
                    if i[1] ==  Directions.REVERSE[currNode[1]]:
                        moveTo = i

                if moveTo[0] == problem.getStartState():
                    break
                
                #remove everyother node in the path till you find the successor
                print "  moveTo: ", moveTo
                enable = 0
                #for y in path.list[:]:
                #    print "  y: ", y
                #    if enable:
                #        if y[0] != moveTo[0]:
                #            print ">remove: ", y , "<"
                #            path.list.remove(y)
                #        else:
                #            currNode = y
                #            break
                #    if y == currNode:
                #        enable = 1
                #        print "    enabled"

                #print(' '.join(str(y) for y in path.list))
            print "broke free"
            print "finally it has happened to me"
            #print(' '.join(str(z) for z in frontier.list))
            #print(' '.join(str(y) for y in path.list))
            for i in reversed(path.list):
                pathAct.append(i[1])
            return pathAct

        exploredSet.add(currNode[0])
        for i in problem.getSuccessors(currNode[0]):
            print "  succ: ", i
            if i[0] not in exploredSet and i[0] not in [row[0] for row in frontier.list]:
                print "  gotin" 
                frontier.push(i)
                path.push(((currNode),i))

        #if checkDeadEnd:
        #    print "deadend on node: ", currNode
        #    for l in reversed(path.list):
        #       if l != frontier.list[-1]:
        #           path.pop();
        #        else:
        #            break

    util.raiseNotDefined()















def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
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
