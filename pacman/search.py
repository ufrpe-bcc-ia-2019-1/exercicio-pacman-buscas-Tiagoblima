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
from game import Directions
from pacman import PacmanRules


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
    # from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


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
    global node
    "*** YOUR CODE HERE ***"
    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())

    #guardar apenas nós do que deu certo
    cur_node = problem.getStartState()
    stack = util.Stack()

    moves = []
    visited = set()

    for el in problem.getSuccessors(cur_node):
        stack.push(el)

       while not problem.isGoalState(cur_node[0]) and not stack.isEmpty():

        cur_node = stack.pop()
        caminho =


        visited.add(cur_node[0])
        moves.append(cur_node[1])
        sucessors = problem.getSuccessors(cur_node[0])

        print '{0} -> {1}'.format(cur_node, sucessors)

        for node in sucessors:

            if node[0] not in visited:
                stack.push((node, caminho+node))

    print moves
    return moves
    # util.raiseNotDefined()


def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    DICA: Utilizar util.PriorityQueue
    *** YOUR CODE
    HERE ***
    """
    moves = []
    visited = set()
    queue = util.Queue()
    source = problem.getStartState()

    for node in problem.getSuccessors(source):
        queue.push(node)

    while not problem.isGoalState(source[0]) and not queue.isEmpty():

        source = queue.pop()
        visited.add(source)
        moves.append(source[1])
        frontier = problem.getSuccessors(source[0])

        print "{0} -> {1}".format(source, frontier)

        for node in frontier:

            if node not in visited:
                queue.push(node)

    print moves
    return moves


def uniformCostSearch(problem):
    """Search the node of least total cost first.
    *** YOUR CODE HERE ***
    """
    moves = []
    visited = set()
    queue = util.PriorityQueue()
    source = problem.getStartState()

    for node in problem.getSuccessors(source):
        queue.push(node, node[2])

    while not problem.isGoalState(source[0]) and not queue.isEmpty():

        source = queue.pop()
        visited.add(source)
        moves.append(source[1])
        frontier = problem.getSuccessors(source[0])

        print "{0} -> {1}".format(source, frontier)

        for node in frontier:

            if node not in visited:
                queue.push(node, node[2])

    print moves
    return moves

   # util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    moves = []
    visited = set()
    queue = util.PriorityQueue()
    source = problem.getStartState()

    for node in problem.getSuccessors(source):
        queue.push(node, node[2])

    while not problem.isGoalState(source[0]) and not queue.isEmpty():

        source = queue.pop()
        visited.add(source)
        moves.append(source[1])
        frontier = problem.getSuccessors(source[0])

        print "{0} -> {1}".format(source, frontier)

        for node in frontier:

            if node not in visited:
                queue.push(node, node[2])

    print moves
    return moves


#  util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
