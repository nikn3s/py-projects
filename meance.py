from random import randint

class Meance:
    def __init__(bob, fields) -> None:
        bob.__fields = fields
        
        # {board_state: { (row, column): rating} }
        bob.__states = {
            '_____O___': {
                (2, 3): 3,
                (1, 3): 4,
                (1,2): 4
                }
        }
        
        
    def makeMove(bob, positions:str, state:str, bead: list):
        highest_rating = ()
        for i, value in enumerate(positions):
            if value == '_':
                random_index = value
                break
        
        # list of states
        states = list(bob.__states.keys())
        # list of corresponding (row, column) if any
        beads = list(bob.__states[state].keys())
        
        if state in states and bead in beads:
            values = bob.__states[state]
            highest_rating = max(values, key=values.get)
            return highest_rating
        else: 
            random_pos = bob.__fields[random_index]
            return random_pos
        
    # evaluates game results and 'rewards' the RLA
    def evaluateGame(bob, result, beads, states):
        saved_states = list(bob.__states.keys())
        # iterates through each state in states of its moves
        for state in states:
            if state in saved_states:
                saved_beads = list(bob.__states[state].keys())
                if result == 'w':
                    for bead in beads:
                        if bead in saved_beads:
                            bob.__states[state][bead] += 1
                        else:
                            bob.__states[state][bead] = 1
                elif result == 'l':
                    for bead in beads:
                        if bead in saved_beads:
                            bob.__states[state][bead] -= 1
                        else:
                            bob.__states[state][bead] = 0
                else:
                    for bead in beads:
                        if bead not in saved_beads:
                            bob.__states[state][bead] = 1
                            
            else:
                # bob.__states[state][bead] = bead
                saved_beads = list(bob.__states[state].keys())
                if result == 'w':
                    for bead in beads:
                        bob.__states[state][bead] = 1
                elif result == 'l':
                    for bead in beads:
                        bob.__states[state][bead] = 0
                else:
                    for bead in beads:
                        bob.__states[state][bead] = 1
                    
            
    
    def modifyState(bob):
        pass
                    
    
    def getState(bob):
        return bob.__states
    
    def getBeads(bob):
        return bob.__bead_config
    
        
class TicTacToe:
    def __init__(bob) -> None:
        bob.__meance = Meance()
        bob.__moves = []
        bob.__board =list('''
                    1   2   3
                     
              1     _ | _ | _
              2     _ | _ | _
              3     _ | _ | _''')
        
        bob.__fields = {
            (1, 1): 1,
            (1,2): 2,
            (1,3): 3,
            (2, 1): 4,
            (2,2): 5,
            (2,3): 6,
            (3, 1): 7,
            (3,2): 8,
            (3,3): 9,
        }
        bob.__position = list('_________')
        bob.__board_position = [73, 77, 81, 103, 107, 111, 133, 137, 141]
        
    def play(bob):
        print('Welcome to 𝖬𝖾𝖺𝗇𝖼𝖾')
        print('Type START to play')
        start = input('> ')
        
        if start not in ['start', 'START', 's', 'S']:
            exit()
        
              
        print(''.join(bob.__board))
        
        bob.userMove()

    def userMove(bob):
        # records the move position
        row_move = int(input('Row > '))
        column_move = int(input('Column > '))
        move = (row_move, column_move)
        # appends the position into a list variable
        bob.__moves.append(move)
        # findex of the posiiton in a flat rep
        position_index = bob.__fields[move] - 1
        # findex of the corresponding cell
        board_pos_index = bob.__board_position[position_index]
        # replaces the given indexes with X
        bob.__position[position_index] = 'X'
        bob.__board[board_pos_index] = 'X'
        # converts to a readable format
        position = ''.join(bob.__position)
        board = ''.join(bob.__board)
        # prints the board
        print(board)
        # for debugging
        print(position)
        print(bob.__moves)
        
    def evaluateMove():
        pass
            
    
if __name__ == '__main__':
    game = TicTacToe()
    game.play()