from link import Link
from node import Node
from graph import Graph
from orientedgraph import OrientedGraph

import csv

def makeGraph(graphId, file):
    with open(file, newline='') as csv_file:
        reader = csv.reader(csv_file, delimiter='\t')

        graphe1 = OrientedGraph(graphId)

        nbrNodes = next(reader)

        for i in range(1, int(nbrNodes[0]) + 1):
            graphe1.addNode(Node(i))

        for row in reader:
            graphe1.addLinkToGraph(Link(int(row[0]), int(row[1]), float(row[2])))

        return graphe1


node1 = Node(11)
node2 = Node(22)
node3 = Node(33)
node4 = Node(4444)

link1 = Link(11, 22, 10)
link2 = Link(22, 33, 11)
link4 = Link(11, 4444, 11)

graph1 = OrientedGraph(10)
graph1.addNode(node1)

graph1.addNode(node2)
graph1.addNode(node3)
graph1.addNode(node4)
graph1.addLinkToGraph(link1)
graph1.addLinkToGraph(link2)
graph1.addLinkToGraph(link4)

graph1.dijkstraAlgo(1, 8)

print("Next Node")
print(graph1.getNextNodes(22))
print("===========================================================")
graph = makeGraph(1, "fileGraph2.csv")
print("Liste prochaine Noeuds : " + str(graph.getNextNodes(1)))

graph.__str__()  # affichage liste
