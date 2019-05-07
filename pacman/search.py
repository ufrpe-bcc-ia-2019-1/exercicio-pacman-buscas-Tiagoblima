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

    # guardar apenas nos do que deu certo
    cur_node = problem.getStartState()
    stack = util.Stack()

    parent = {problem.getStartState(): None}
    moves = []
    visited = set()

    successors = problem.getSuccessors(cur_node)

    for node in successors:
        stack.push(node)

    parent[successors.pop()[0]] = None

    while not stack.isEmpty():

        cur_node = stack.pop()
        visited.add(cur_node[0])

        if problem.isGoalState(cur_node[0]):

            move = cur_node[1]
            position = cur_node[0]
            moves.append(move)

            while parent[position] is not None:
                node = parent[position]
                print(node)
                move = node[1]
                position = node[0]
                moves.append(move)

            moves.reverse()

            print(moves)

            return moves

        successors = problem.getSuccessors(cur_node[0])

        print '{0} -> {1}'.format(cur_node, successors)

        for node in successors:

            if node[0] not in visited:
                stack.push(node)
                parent[node[0]] = cur_node
    # util.raiseNotDefined()


def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    DICA: Utilizar util.PriorityQueue
    *** YOUR CODE
    HERE ***
    """
    # guardar apenas nos do que deu certo
    cur_node = problem.getStartState()
    queue = util.Queue()

    parent = {problem.getStartState(): None}
    moves = []
    visited = set()

    successors = problem.getSuccessors(cur_node)

    for node in successors:
        queue.push(node)

    parent[successors.pop(0)[0]] = None

    while not queue.isEmpty():

        cur_node = queue.pop()
        visited.add(cur_node[0])

        if problem.isGoalState(cur_node[0]):

            move = cur_node[1]
            position = cur_node[0]
            moves.append(move)

            while parent[position] is not None:
                node = parent[position]
                print(node)
                move = node[1]
                position = node[0]
                moves.append(move)

            moves.reverse()

            print(moves)

            return moves

        successors = problem.getSuccessors(cur_node[0])

        print '{0} -> {1}'.format(cur_node, successors)

        for node in successors:

            if node[0] not in visited:
                queue.push(node)
                parent[node[0]] = cur_node


def uniformCostSearch(problem):
    """Search the node of least total cost first.
    *** YOUR CODE HERE ***
    """
    cur_node = problem.getStartState()
    queue = util.PriorityQueue()

    parent = {problem.getStartState(): None}
    moves = []
    visited = set()

    successors = problem.getSuccessors(cur_node)

    for node in successors:
        queue.push(node, node[2])

    first = queue.pop()
    queue.push(first, first[2])

    parent[first[0]] = None

    while not queue.isEmpty():

        cur_node = queue.pop()
        visited.add(cur_node[0])

        if problem.isGoalState(cur_node[0]):

            move = cur_node[1]
            position = cur_node[0]
            moves.append(move)

            while parent[position] is not None:
                node = parent[position]
                print(node)
                move = node[1]
                position = node[0]
                moves.append(move)

            moves.reverse()

            print(moves)

            return moves

        successors = problem.getSuccessors(cur_node[0])

        print '{0} -> {1}'.format(cur_node, successors)

        for node in successors:

            if node[0] not in visited:
                queue.push(node, node[2])
                parent[node[0]] = cur_node


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
    cur_node = problem.getStartState()
    queue = util.PriorityQueue()

    parent = {problem.getStartState(): None}
    moves = []
    visited = set()

    successors = problem.getSuccessors(cur_node)

    for node in successors:
        queue.push(node, node[2] + heuristic(node[0], problem))

    first = queue.pop()
    queue.push(first, first[2] + heuristic(first[0], problem))

    parent[first[0]] = None

    while not queue.isEmpty():

        cur_node = queue.pop()
        visited.add(cur_node[0])

        if problem.isGoalState(cur_node[0]):

            move = cur_node[1]
            position = cur_node[0]
            moves.append(move)

            while parent[position] is not None:
                node = parent[position]
                print(node)
                move = node[1]
                position = node[0]
                moves.append(move)

            moves.reverse()

            print(moves)

            return moves

        successors = problem.getSuccessors(cur_node[0])

        print '{0} -> {1}'.format(cur_node, successors)

        for node in successors:

            if node[0] not in visited:
                queue.push(node, node[2] + heuristic(node[0], problem))
                parent[node[0]] = cur_node


#  util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
