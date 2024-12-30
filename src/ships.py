class Ships:
    def __init__(self, type: str, lives: int):
        self.type = type
        self.coordinates = set()
        self.hitsRemaining = lives
    
    def addCoords(self, newTuple):
        self.coordinates.add(newTuple)
    
    def findHit(self, myTuple):
        # print(self.coordinates)
        # print(myTuple)
        # print(f'Is {myTuple} in self.coordinates?')
        # print(bool(myTuple in self.coordinates))
        if(self.hitsRemaining > 0):
            if myTuple in self.coordinates:
                self.hitsRemaining-= 1;
                # print(f'Hits remaining on {self.type}: {self.hitsRemaining}')
            if self.hitsRemaining == 0:
                print(f'YOU SUNK THE ENEMY {self.type}!')
                return 'sunk'

            


    
