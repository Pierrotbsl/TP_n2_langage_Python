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


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

link1 = Link(1, 2, 5)
link2 = Link(2, 2, 6)

graph = OrientedGraph(5)

graph.addNode(node1)
graph.addNode(node2)
graph.addNode(node3)
graph.addLinkToGraph(link1)
graph.addLinkToGraph(link2)

#graph.dijkstra(1, 5) => commenté car erreur KeyError : 1 non résolue

print("get Next Node : ")
print(graph.getNextNodes(2))
graph = makeGraph(1, "fileGraph2.csv")
print("List of Nodes : ")
print(graph.getNextNodes(1))
graph.__str__()
