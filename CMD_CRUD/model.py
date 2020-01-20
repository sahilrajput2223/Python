class model:
    def __init__(self, id, name, number):
        self.__id = id
        self.__name = name
        self.__number = number

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def getNumber(self):
        return self.__number

    def setId(self, id):
        self.__id = id

    def setName(self, name):
        self.__name = name

    def setNumber(self, number):
        self.__number = number
