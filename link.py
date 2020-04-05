class Link:

    def __init__(self, tmp_node1, tmp_node2, distance):
        """Initialize the value."""
        self.__id = str(tmp_node1) + "." + str(tmp_node2)
        self.__distance = distance
        self.__node1 = tmp_node1
        self.__node2 = tmp_node2

    def getId(self):
        return self.__id

    def getDistance(self):
        return self.__distance

    def getNode1(self):
        return self.__node1

    def getNode2(self):
        return self.__node2

    def setId(self, tmp_id):
        self.__id = tmp_id

    def __str__(self):
        print("Link Id is : ")
        print(self.__id)
