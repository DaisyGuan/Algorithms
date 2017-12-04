class Space(object):
    __isCarParked = False
    __spaceId = 0

    def __init__(self, spaceId):
        self.__isCarParked = False
        self.__spaceId = spaceId

    def getSpaceId(self):
        return self.__spaceId

    def parkCar(self):
        self.__isCarParked = True

    def leaveCar(self):
        self.__isCarParked = False

    def checkIfCarParked(self):
        return self.__isCarParked
