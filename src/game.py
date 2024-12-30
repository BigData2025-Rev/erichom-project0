from ships import Ships
import json
import random

class Game:

    def __init__(self):
        #last hit successful bool (on true, next turn is free)
        self.enemyShips = set()
        self.successfulHits = set()
        self.allGuesses = set()
        self.gameGrid = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        self.gameState = ''
        self.x = 0
        self.y = 0
        self.turns = 10
        self.shipsRemaining = 0
        self.splash = False

    def drawUI(self, status):
        print('')
        print('Welcome to Battleship.')
        print('You will have 10 tries to guess the enemy ship positions.')
        print('There are 3 ship types: Destroyer(2), Cruiser(3), Battleship(4)')
        print('Every correct guess will provide you a free turn.')
        print('Good luck!')
        print('')

        self.printGrid()

        # initialPos, direction = self.generateShipPosition(2)

        #print(f'Initial position: {initialPos}, direction: {direction}')
        if(status == 'newGame'):
            destroyer = Ships('Destroyer', 2)
            x = random.randint(0,1)
            destroyer.addCoords((x,1))
            destroyer.addCoords((x,2))
            self.shipsRemaining += 1
            self.enemyShips.add((x,1))
            self.enemyShips.add((x,2))

            cruiser = Ships('Cruiser', 3)
            x = random.randint(2,4)
            cruiser.addCoords((x,0))
            cruiser.addCoords((x,1))
            cruiser.addCoords((x,2))
            self.shipsRemaining += 1
            self.enemyShips.add((x,0))
            self.enemyShips.add((x,1))
            self.enemyShips.add((x,2))

            battleship = Ships('Battleship', 4)
            y = random.randint(3,4)
            battleship.addCoords((1,y))
            battleship.addCoords((2,y))
            battleship.addCoords((3,y))
            battleship.addCoords((4,y))
            self.shipsRemaining += 1
            self.enemyShips.add((1,y))
            self.enemyShips.add((2,y))
            self.enemyShips.add((3,y))
            self.enemyShips.add((4,y))
        

        # print(f'Hits remaining on creation: {destroyer.hitsRemaining}')


        self.gameState = 'playing'
        # x = input('Ship x: ')
        # y = input('Ship y: ')
        # x = int(x)
        # y = int(y)

        # self.enemyShips.add((x,y))

        # x = input('Ship x: ')
        # y = input('Ship y: ')
        # x = int(x)
        # y = int(y)

        # self.enemyShips.add((x,y))


        while(self.gameState == 'playing'):
            if (self.shipsRemaining == 0):
                self.gameState = 'won'
                print(f'Game over! You {self.gameState}!')
                continue

            if (self.turns == 0):
                self.gameState = 'lost'
                print(f'Game over! You {self.gameState}!')
                continue

            print('')
            print('Enter menu codes (load, save, newGame, viewShips, viewData, viewSave) OR')
            print('')
            print('Enter coordinates of target (x, y):')
            x = input('x: ')
            
            if(x == 'viewShips'):
                self.revealGrid()
            elif(x == 'save'):
                self.writeSave(destroyer, cruiser, battleship)
                continue
            elif(x == 'load'):
                d,c,b = self.loadSave()
                if d != None:
                    destroyer.hitsRemaining = d
                    cruiser.hitsRemaining = c
                    battleship.hitsRemaining = b
                continue
            elif(x == 'viewData'):
                self.viewData(destroyer, cruiser, battleship)
                continue
            elif(x == 'viewSave'):
                self.viewSave()
                continue
            elif(x == 'newGame'):
                self.newGame()

            else: 
                
                try:
                    int(x)
                except ValueError:
                    print('Invalid input, input must be an integer or menu code.')
                    continue

                y = input('y: ')
                print('')

                if(y == 'viewShips'):
                    self.revealGrid()

                elif(y == 'save'):
                    self.writeSave(destroyer, cruiser, battleship)
                    continue

                elif(y == 'load'):
                    d,c,b = self.loadSave()
                    if d != None:
                        destroyer.hitsRemaining = d
                        cruiser.hitsRemaining = c
                        battleship.hitsRemaining = b
                        continue
                elif(x == 'viewData'):
                    self.viewData(destroyer, cruiser, battleship)
                    continue
                elif(y == 'viewSave'):
                    self.viewSave()
                    continue

                elif(x == 'newGame'):
                    self.newGame()
                
                else:

                    try:
                        int(y)
                    except ValueError:
                        print('Invalid input, input must be an integer or menu code.')
                        continue

                    x = int(x)
                    y = int(y)
                    if x < 0 or x > 4 or y < 0 or y > 4:
                        print('Target coordinates are out of bounds!')
                        continue

                    print('')
                    currentTuple = (x,y)


                    # print(f'Is ({x},{y}) in enemyShips?: ')
                    # print(bool(((x,y)) in self.enemyShips))
                    # print(type((1,1)a))

                    if currentTuple in self.allGuesses:
                        print('Invalid guess, location already attempted.')
                        continue

                    if currentTuple in self.enemyShips:
                        print(f'{currentTuple} -----> Hit!')
                        print('')
                        self.gameGrid[x][y] = 1
                        self.Splash = True
                        self.successfulHits.add((x,y))
                        self.allGuesses.add((x,y))
                        if destroyer.findHit((x,y)) == 'sunk': 
                            self.shipsRemaining -= 1
                        elif cruiser.findHit((x,y)) == 'sunk':
                            self.shipsRemaining -= 1
                        elif battleship.findHit((x,y)) == 'sunk':
                            self.shipsRemaining -= 1
                        print(f'Turns remaining: {self.turns}')
                        print(f'Ships remaining: {self.shipsRemaining}')
                        print('')

                    
                    else:
                        print(f'{currentTuple} -----> Miss.')
                        print('')
                        self.gameGrid[x][y] = 2
                        self.splash = False
                        self.allGuesses.add((x,y))
                        #print(self.allGuesses)
                        #print(self.enemyShips)
                        self.turns -= 1
                        print(f'Turns remaining: {self.turns}')
                        print(f'Ships remaining: {self.shipsRemaining}')
                        print('')
                        #print(type(list(self.enemyShips)[1]))

                    self.printGrid()

    def run(self):
        self.drawUI('newGame')

    def printGrid(self):
        # print('Current board:')
        # print(self.gameGrid)
        # print(len(self.gameGrid))
        print('Current board:')
        print('------------------')
        print('')
        for i in range(0,5):
            for j in range(0,5):
                if self.gameGrid[i][j] == 0:
                    print('*   ', end ='')
                elif self.gameGrid[i][j] == 1:
                    print('X   ', end = '')
                elif self.gameGrid[i][j] == 2:
                    print('O   ', end = '')
            print(' ')
            print(' ')
        print('------------------')

    def revealGrid(self):
        
        revealGrid = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]         

        for x,y in self.enemyShips:
            revealGrid[x][y] = 1

        print('------------------')
        print('')
        for i in range(0,5):
            for j in range(0,5):
                if revealGrid[i][j] == 0:
                    print('*   ', end ='')
                elif revealGrid[i][j] == 1:
                    print('X   ', end = '')
                elif revealGrid[i][j] == 2:
                    print('O   ', end = '')
            print(' ')
            print(' ')
        print('------------------')

    def generateShipPosition(self, len):
        blocked = False
        valid = False
        initialX = random.randint(0,4)
        initialY = random.randint(0,4)
        direction = 0

        newTuple = (initialX, initialY)

        while valid == False:

            while newTuple in self.enemyShips:
                initialX = random.randint(0,4)
                initialY = random.randint(0,4)
                newTuple = (initialX, initialY)

            direction = random.randint(1,2)
            print(f'Direction: {direction}')
            #direction = 1

            for i in range(1, len):
                # try vertical first
                if direction == 1:
                    if (initialX + i, initialY) in self.enemyShips or initialX + i < 0 or initialX + i > 4:
                        blocked = True
                        print('blocked tuple detected, trying north direction')
                        direction = 3
                        i = 0
                    if i == len - 1 and blocked == False:
                        valid = True
                                
                if direction == 3:
                    if (initialX - i, initialY) in self.enemyShips or initialX - i < 0 or initialX - i > 4:
                        blocked = True
                        print('blocked tuple detected, retrying new initial')
                    if i == len - 1 and blocked == False:
                        valid = True
            
                #try horizontal
                if direction == 2:
                    if (initialX, initialY + i) in self.enemyShips or initialY + i < 0 or initialY + i > 4:
                        blocked = True
                        print('blocked tuple detected, trying south direction')
                        direction = 4
                        i = 0
                    if i == len - 1 and blocked == False:
                        valid = True

                if direction == 4:
                    if (initialX, initialY - i) in self.enemyShips or initialY - i < 0 or initialY - i > 4:
                        blocked = True
                        print('blocked tuple detected, retrying new initial')
                    if i == len - 1 and blocked == False:
                        valid = True

        return newTuple, direction

    def loadSave(self):
        name = input('Enter save file name:')

        try:
            with open(name, 'r') as f:
            # Load the JSON data into a Python dictionary
                data = json.load(f)
        except Exception as e:
            print(f'Error opening JSON file: {e}')

            return None, None, None

        self.gameGrid = set()
        self.gameGrid = data[0].get("gameGrid")

        self.allGuesses = set()

        guessList = data[1].get("allGuesses")

        for item in guessList:
            
            x = item[0]
            y = item[1]

            self.allGuesses.add((x,y))
        
        self.turns = data[5].get("turns")
        self.shipsRemaining = data[6].get("shipsRemaining")

        self.enemyShips = set()

        destroyer = Ships('Destroyer', 2)
        destroyerCoords = data[2].get("destroyer")
        for item in destroyerCoords:
            x = item[0]
            y = item[1]

            destroyer.addCoords((x,y))
            self.enemyShips.add((x,y))

        cruiser = Ships('Cruiser', 3)
        cruiserCoords = data[3].get("cruiser")
        for item in cruiserCoords:
            x = item[0]
            y = item[1]

            cruiser.addCoords((x,y))
            self.enemyShips.add((x,y))

        battleship = Ships('Battleship', 4)
        battleshipCoords = data[4].get("battleship")
        for item in battleshipCoords:
            x = item[0]
            y = item[1]

            battleship.addCoords((x,y))
            self.enemyShips.add((x,y))
        
        # for item in self.allGuesses:
        #     destroyer.findHit(item)
        #     cruiser.findHit(item)
        #     battleship.findHit(item)

        # 8 DD, 9 CL, 10 BB

        dHits = data[8].get("dHits")
        cHits = data[9].get("cHits")
        bHits = data[10].get("bHits")


        # destroyer.addCoords((1,1))
        # destroyer.addCoords((1,2))
        # self.shipsRemaining += 1
        # self.enemyShips.add((1,1))
        # self.enemyShips.add((1,2))

        print('')
        print('Loaded game successfully!')
        print('')

        print(f'Turns remaining: {self.turns}')
        print(f'Ships remaining: {self.shipsRemaining}')

        self.printGrid()

        return dHits, cHits, bHits
        
        # print('Loaded grid:')
        # print(newGameGrid)
        # print('Actual Grid in Memory:')
        # print(self.gameGrid)
    
    def viewSave(self):
        name = input('Enter save file name: ')
        try:
            with open(name, 'r') as f:
            # Load the JSON data into a Python dictionary
                data = json.load(f)
        except Exception as e:
            print(f'Error opening JSON file: {e}')
            return

        for item in data:
            print(item)
        
        # print(type(data[0].get("gameGrid")))
        # print(data[0].get("gameGrid"))

        # print('all guesses:')
        # print(data[1].get("allGuesses")[0][1])

    def viewData(self, destroyer, cruiser, battleship):
        print(f'gameGrid: {self.gameGrid}')
        print(f'allGuesses: {self.allGuesses}')
        print(f'turns: {self.turns}')
        print(f'shipsRemaining: {self.shipsRemaining}')
        print(f'Destroyer hits remaining:  {destroyer.hitsRemaining}')
        print(f'Cruiser hits remaining:  {cruiser.hitsRemaining}')
        print(f'Battleship hits remaining:  {battleship.hitsRemaining}')

    def writeSave(self, destroyer, cruiser, battleship):
        name = input('Enter save file name: ')
        gameData = [{'gameGrid': self.gameGrid}, {'allGuesses': list(self.allGuesses)}, {'destroyer': list(destroyer.coordinates)}, {'cruiser': list(cruiser.coordinates)}, {'battleship': list(battleship.coordinates)},{'turns': self.turns}, {'shipsRemaining': self.shipsRemaining}, {'splash': self.splash},{'dHits': destroyer.hitsRemaining}, {'cHits': cruiser.hitsRemaining}, {'bHits': battleship.hitsRemaining}]
        try:
            with open(name, 'w') as f:
                # Dump the variables to the file as JSON
                json.dump(gameData, f, indent=4)  # indent for pretty formatting
        except Exception as e:
            print(f'Error writing JSON to file: {e}')
            return

        print('')
        print('Game saved, game data written to file.')
        print('')
        self.gameState = 'saved'

    def newGame(self):
        self.enemyShips = set()
        self.successfulHits = set()
        self.allGuesses = set()
        self.gameGrid = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        self.gameState = ''
        self.x = 0
        self.y = 0
        self.turns = 10
        self.shipsRemaining = 0
        self.splash = False       

        self.drawUI('newGame')      
                


            

        


    
    


