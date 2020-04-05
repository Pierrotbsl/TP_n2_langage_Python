from graph import Graph


class OrientedGraph(Graph):
    def __init__(self, graphId):
        Graph.__init__(self, graphId)

    def getNextNodes(self, tmp_nodeId):
        nextNode = {}

        for LinkId in self._linkDictionary:
            LinkId1 = LinkId
            LinkId = LinkId.split(".")
            if LinkId[0] == str(tmp_nodeId):
                nextNode[LinkId[1]] = self._linkDictionary[LinkId1].getDistance()

        return nextNode
