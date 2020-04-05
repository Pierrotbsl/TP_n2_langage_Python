class Node:
    """Initialize the value."""

    def __init__(self, NodeId):
        self.__nodeId = NodeId
        self.__connectLink = []

    """Getters et Setters"""

    def getNodeId(self):
        return self.__nodeId

    def setNodeId(self, NodeId):
        self.__nodeId = NodeId

    def getList(self):
        for element in self.__connectLink:
            print(element)
        return self.__connectLink

    """Methods"""

    def __str__(self):
        print("Node Id is : ")
        print(self.__nodeId)

    def displayLinkId(self):
        print("Links List : ")
        print(self.__connectLink)

    def addLinkId(self, tmp_id):
        self.__connectLink.append(tmp_id)
