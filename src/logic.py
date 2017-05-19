#
# CS1010FC --- Programming Methodology
#
# Mission N Solutions
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.
from random import *

#######
#Task 1a#
#######

DIMENSION = 2

# [Marking Scheme]
# Points to note:
# Matrix elements must be equal but not identical
# 1 mark for creating the correct matrix

def new_game(n):
    matrix = []

    for i in range(n):
        matrix.append([0] * n)
    return matrix

###########
# Task 1b #
###########

# [Marking Scheme]
# Points to note:
# Must ensure that it is created on a zero entry
# 1 mark for creating the correct loop

def add_two(mat):
    a=randint(0,DIMENSION-1)
    b=randint(0,DIMENSION-1)
    while(mat[a][b]!=0):
        a=randint(0,DIMENSION-1)
        b=randint(0,DIMENSION-1)
    mat[a][b]=2
    return mat

###########
# Task 1c #
###########

# [Marking Scheme]
# Points to note:
# Matrix elements must be equal but not identical
# 0 marks for completely wrong solutions
# 1 mark for getting only one condition correct
# 2 marks for getting two of the three conditions
# 3 marks for correct checking

def game_state(mat):
    for i in range(DIMENSION):
        for j in range(DIMENSION):
            if mat[i][j]==2048:
                return 'win'
    for i in range(DIMENSION-1): #intentionally reduced to check the row on the right and below
        for j in range(DIMENSION-1): #more elegant to use exceptions but most likely this will be their solution
            if mat[i][j]==mat[i+1][j] or mat[i][j+1]==mat[i][j]:
                return 'not over'
    for i in range(DIMENSION): #check for any zero entries
        for j in range(DIMENSION):
            if mat[i][j]==0:
                return 'not over'
    for k in range(DIMENSION-1): #to check the left/right entries on the last row
        if mat[DIMENSION-1][k]==mat[DIMENSION-1][k+1]:
            return 'not over'
    for j in range(DIMENSION-1): #check up/down entries on last column
        if mat[j][DIMENSION-1]==mat[j+1][DIMENSION-1]:
            return 'not over'
    return 'lose'

###########
# Task 2a #
###########

# [Marking Scheme]
# Points to note:
# 0 marks for completely incorrect solutions
# 1 mark for solutions that show general understanding
# 2 marks for correct solutions that work for all sizes of matrices

def reverse(mat):
    new=[]
    for i in range(DIMENSION):
        new.append([])
        for j in range(DIMENSION):
            new[i].append(mat[i][DIMENSION-j-1])
    return new

###########
# Task 2b #
###########

# [Marking Scheme]
# Points to note:
# 0 marks for completely incorrect solutions
# 1 mark for solutions that show general understanding
# 2 marks for correct solutions that work for all sizes of matrices

def transpose(mat):
    new=[]
    for i in range(DIMENSION):
        new.append([])
        for j in range(DIMENSION):
            new[i].append(mat[j][i])
    return new

##########
# Task 3 #
##########

# [Marking Scheme]
# Points to note:
# The way to do movement is compress -> merge -> compress again
# Basically if they can solve one side, and use transpose and reverse correctly they should
# be able to solve the entire thing just by flipping the matrix around
# No idea how to grade this one at the moment. I have it pegged to 8 (which gives you like,
# 2 per up/down/left/right?) But if you get one correct likely to get all correct so...
# Check the down one. Reverse/transpose if ordered wrongly will give you wrong result.

def cover_up(mat):
    new=[[0,0],[0,0]]
    done=False
    for i in range(2):
        count=0
        for j in range(2):
            if mat[i][j]!=0:
                new[i][count]=mat[i][j]
                if j!=count:
                    done=True
                count+=1
    return (new,done)

def merge(mat):
    done=False
    newscore=0
    for i in range(2):
         for j in range(1):
             if mat[i][j]==mat[i][j+1] and mat[i][j]!=0:
                 mat[i][j]*=2
                 mat[i][j+1]=0
                 newscore=mat[i][j]
                 done=True
    return (mat,done,newscore)


def up(game):
        #print("up")
        # return matrix after shifting up
        game=transpose(game)
        game,done=cover_up(game)
        temp=merge(game)
        game=temp[0]
        done=done or temp[1]
        newscore=temp[2]
        game=cover_up(game)[0]
        game=transpose(game)
        return (game,done,newscore)

def down(game):
        #print("down")
        game=reverse(transpose(game))
        game,done=cover_up(game)
        temp=merge(game)
        game=temp[0]
        done=done or temp[1]
        newscore=temp[2]
        game=cover_up(game)[0]
        game=transpose(reverse(game))
        return (game,done,newscore)

def left(game):
        #print("left")
        # return matrix after shifting left
        game,done=cover_up(game)
        temp=merge(game)
        game=temp[0]
        done=done or temp[1]
        newscore=temp[2]
        game=cover_up(game)[0]
        return (game,done,newscore)

def right(game):
        #print("right")
        # return matrix after shifting right
        game=reverse(game)
        game,done=cover_up(game)
        temp=merge(game)
        game=temp[0]
        done=done or temp[1]
        newscore=temp[2]
        game=cover_up(game)[0]
        game=reverse(game)
        return (game,done,newscore)
