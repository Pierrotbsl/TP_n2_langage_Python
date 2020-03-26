class Lien:
    """Class Test."""

    def __init__(self, noeud1, noeud2, distance):
        """Initialize the value."""
        self.__identifiant = 1
        self.__distance = 0
        self.__noeud1 = 0
        self.__noeud2 = 0

    def getIdentifiant(self):
        return self.__identifiant

    def getDistance(self):
        return self.__distance

    def getNoeud1(self):
        return self.__noeud1

    def getNoeud2(self):
        return self.__noeud2

    def setIdentifiant(self, identifiant):
        self.__identifiant = identifiant

    def __str__(self):
        print("L'identifiant est : " + str(self.getIdentifiant()))


Lien1 = Lien(1, 1, 10)
Lien1.__str__()
