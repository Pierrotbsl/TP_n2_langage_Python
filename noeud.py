from lien import Lien

class Noeud:
    """Class Noeud"""
    id = 1

    """Initialize the value."""
    def __init__(self):
        self.__identifiantNoeud=self.getId()
        self.__liste=[]

        Noeud.id+=1

    """Getters et Setterse"""
    def getIdentifiantNoeud(self):
        return self.__identifiantNoeud

    def setIdentifiantNoeud(self, identifiantNoeud):
        self.__identifiantNoeud=identifiantNoeud

    def getListe(self):
        for element in self.__liste:
            print(element)
        """return self.__liste"""


    """Les méthode"""
    def __str__(self):
        print("L'identifiant du Noeud est : "+ str(self.__identifiantNoeud))

    def affichageIdentifiantLien(self):
        print("Liste des liens : " + str(self.getListe()))

    def ajoutIdentifiantLien(self, identifiant):
        self.__liste.append(identifiant)




    @classmethod
    def getId(cls):
        return Noeud.id


noeud1= Noeud()
noeud1.__str__()
noeud1.affichageIdentifiantLien()

