from collections import deque

from link import Link
from node import Node


import copy


class Graph:
    """ Graph Class """

    def __init__(self, tmp_id):
        self._nbrNodes = 0
        self._id = tmp_id
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
        self._nodeDictionary[node.getNodeId()] = node
        self._nbrNodes += 1

    def addLinkToGraph(self, link):
        self._linkDictionary[link.getId()] = link
        self._nodeDictionary[link.getNode1()].addLinkId(link.getId())
        self._nodeDictionary[link.getNode2()].addLinkId(link.getId())

    def getNextNode(self, tmp_nodeId):
        nextNode = {}

        for LinkId in self._linkDictionary:
            LinkId1 = LinkId
            LinkId = LinkId.split(".")
            if LinkId[0] == str(tmp_nodeId):
                nextNode[LinkId[1]] = self._linkDictionary[LinkId1].get_distance()
            if LinkId[1] == str(tmp_nodeId):
                nextNode[LinkId[0]] = self._linkDictionary[LinkId1].get_distance()

        return nextNode

    def __str__(self):
        print("Node Id is : ")
        print(self._id)
        print("Link : ")
        print(self._linkDictionary)
        print("\n")

    def dijkstra(self, Source, Destination):
        P = list()
        d = {}
        minKey = 0
        for i in range(1, self._nbrNodes + 1):
            d[i] = float('inf')
        d[Source] = 0

        while not len(P) == self._nbrNodes:
            D = copy.deepcopy(d)
            for j in range(1, len(d) + 1):
                if self._nodeDictionary[j].getNodeId() in P:
                    del D[j]
            dMin = min(D.values())
            find = 0
            for k in D:
                if dMin == D[k] and not find:
                    minKey = k
                    find = 1
            P.append(self._nodeDictionary[minKey].getNodeId())
            if not self._nodeDictionary[minKey].getNodeId() == Destination:
                tmpNode = self.getNextNode(self._nodeDictionary[minKey].getNodeId())
                for l in tmpNode:
                    if not self._nodeDictionary[l] in P:
                        dLink = tmpNode[l]
                        d[l] = min(d[l], (d[minKey] + dLink))
            else:
                return P, d[minKey]
        return P, d
