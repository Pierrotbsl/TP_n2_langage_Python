from queue import PriorityQueue
from node import Node
from lien import Lien
from graph import Graph

import csv


"Lire le fichier"
Graph = Graph(_id)

with open('file') as f:
    f_csv = csv.reader(f)
    header = next(f_csv)

    for _ in range(int(header[0])):
        node = Node()
        Graph.addNode(node)

    for ligne in f_csv:
        ligne = str(ligne[0])
        ligne = ligne.split("\t")
        Graph.addLinkToGraph(ligne[0], ligne[1], ligne[2])

return Graph

def dijkstra(self, f, t):
    nodeId = f.getId()
    dist = [None] * len(self.getDictNode())
    for i in range(len(dist)):
        dist[i] = sys.maxsize
        dist[i].append([self.getDictNode()[nodeId]])
    dist[nodeId][0] = 0
    nodeQueue = [i for i in range(len(self.getDictNode()))]
    nodesSeen = set()
    while len(nodeQueue):
        dist_min = sys.maxsize
        node_min = None
        for n in nodeQueue:
            if dist[n][0] < dist_min and n not in nodesSeen:
                dist_min = dist[n][0]
                node_min = n
        nodeQueue.remove(node_min)
        nodesSeen.add(nodesSeen)
        neighbours = self.obtenirProchainsNoeuds(node_min.getId())
        for (node, edge) in neighbours:
            dist_tot = edge.getl1() + dist_min
            if dist_tot < dist[node.getId()][0]:
                dist[node.getId()][0] = dist_tot
                dist[node.getId()][1] = list(dist[node_min][1])
                dist[node.getId()][1].append(node)
        return dist
