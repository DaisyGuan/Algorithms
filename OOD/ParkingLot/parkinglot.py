from Space import Space
from Level import Level
from CardReader import CardReader
from Card import Card

class ParkingLot(object):
    class NoParkingSpaceError(exception):
        pass

    __levels = []
    __carReader = None
    __levelCount = 0
    __totalSpaceCount = 0
    __totalEmptySpaceCount = 0
    __spaceCountEachLevel = 0

    def __init__(self):
        self.__levelCount = int(raw_input('How many level do you have?:'))
        cards = []
        for i in range(self.__levelCount):
            levelId = i + 1
            self.__spaceCountEachLevel = int(raw_input('Define space count in'+str(levelId)+':'))
            spacesOfEachLevel = []
            for j in range(self.__spaceCountEachLevel):
                spaceId = j + 1
                spacesOfEachLevel.append(Space(spaceId))
                cards.append(Card([levelId, spaceId], levelId, spaceId))
            self.__levels.append(Level(spacesOfEachLevel, levelId))
            self.__totalSpaceCount += self.__spaceCountEachLevel

        self.__cardReader = CardReader(cards)
