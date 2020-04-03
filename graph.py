from node import Node

class Graph(Node):

    """ Graph Class """

    def __init__(self, id_):
        self._id = id_
        self._nbrNodes = 0
        self._nodeDictionary = {}
        self._linkDictionary = {}

    """ Getters and Setters """

    def setGraphId(self, GraphId):
        self._id = GraphId

    def getGraphId(self):
        return self._id

    def getNbNodes(self):
        return self._nbrNodes

    """ methods """

    def addNode(self, node):
        self._nodeDictionary.add(node)
        self._nbrNodes += 1

    def addLinkToGraph(self, link):
        self._linkDictionary.add(link)

    def getNextNode(self, idNode):
        return self._nodeDictionary.append(idNode)

    def __str__(self):
        print("Node Id is : " + str(self._id))
