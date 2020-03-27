class Graphe:

    def __init__(self, id_, nbrNodes, dictionaryLink):
        self._id = id_
        self._nbrNodes = nbrNodes
        self._nodeDictionary = 0
        self._DictionaryLink = dictionaryLink

    def getNbNodes(self):
        return self._nodeDictionary

    def addNode(self, node):
        self._nbrNodes += 1
        #self._dictionnaireNoeuds.append(node)


    def getNextNode(self, idNode):
        return

    def __str__(self):
        print("Liste des noeuds & liens du graphe")
