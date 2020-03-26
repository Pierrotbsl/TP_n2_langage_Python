class Lien:
    """Class Test."""
    __id = 1
    __nodes = 1
    __distance = 1

    def __init__(self, node1, node2):
        """Initialize the value."""
        self.__value = 1
        Lien.__id += 1
        Lien.__nodes += 1
        Lien.__distance += 1

    def __str__(self, id):
        print()


    def getValue(self):
            return self.__value

    def setValue(self, value):
            self.__value = value
