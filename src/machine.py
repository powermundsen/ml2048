import puzzle

#ACCESS SCORE AS self.game.score
#ACCESS MATRIX AS self.game.matrix
#DECIDE ACTION TO TAKE IN act()
#POSSIBLE ACTIONS:
#	go up:		"'w'"
#	go left:	"'a'"
#	go right:	"'s'"
#	go down:	"'d'"
class Machine:
    game=puzzle.GameGrid() #Game object
    def run(self):
        while True:
            #self.game.key_down("'w'") #EXAMPLE UNCOMMENT TO RUN
            self.game.key_down(self.act()) #COMMENT TO RUN EXAMPLE
            self.game.update_idletasks
            self.game.update()
    def act(self):
        return ("'z'") #DOES NOTHING
        #PLACEHOLDER
