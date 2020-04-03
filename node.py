from lien import Lien
from graph import Graph


class Node(Lien):
    """Class Noeud"""
    id = 1

    """Initialize the value."""
    def __init__(self):
        self.__NodeId = self.getId()
        self.__list = []

        Node.id += 1

    """Getters et Setters"""
    def getNodeId(self):
        return self.__NodeId

    def setNodeId(self, NodeId):
        self.__NodeId = NodeId

    def getList(self):
        for element in self.__list:
            print(element)
        """return self.__liste"""


    """Methods"""

    def __str__(self):
        print("Node Id is : "+ str(self.__NodeId))

    def displayLinkId(self):
        print("Links List : " + str(self.getList()))

    def addLinkId(self, _id):
        self.__list.append(_id)

    @classmethod
    def getId(cls):
        return Node.id


Node1 = Node()
Node1.__str__()
Node1.displayLinkId()

