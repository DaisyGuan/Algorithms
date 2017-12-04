class Card(object):
    __cardId = [0,0]
    __levelId = 0
    __spaceId = 0

    def __init__(self, cardId, levelId, spaceId):
        self.__cardId = [levelId, spaceId]
        self.levelId = levelId
        self.__spaceId = spaceId

    def getCardId(self):
        return self.__cardId

    def getLevelId(self):
        return self.__levelId

    def getSpaceId(self):
        return self.__spaceId
