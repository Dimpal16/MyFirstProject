# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 12:57:02 2019

@author: Dimpoo
"""

import numpy
board = numpy.array([['_','_','_'],['_','_','_'],['_','_','_']])
p1s = 'X'
p2s = 'O'

def place(symbol):
    print(numpy.matrix(board))
    while True:
        row = int(input("Enter row number(1, 2 or 3): "))
        column = int(input("Enter column number(1, 2 or 3): "))
        if (row>0  and row<4) and (column>0  and column <4) and board[row-1][column-1]=='_':
            break
        else:
            print("Enter valid row and column ")
    board[row -1 ][column -1] = symbol
    
def check_rows(symbol):
    for r in range(3):
        count = 0
        for c in range(3):
            if board[r][c] == symbol:
                count+=1
        if count==3:
            print(symbol, ", Won")
            return True
    return False
        
def check_col(symbol):
    for r in range(3):
        count = 0
        for c in range(3):
            if board[c][r] == symbol:
                count+=1
        if count==3:
            print(symbol, ", won")
            return True
    return False
    
def check_diag(symbol):
    diag = numpy.diag(board)
    count=0
    for i in diag:
        if i==symbol:
            count+=1
    if count==3:
        print(symbol, ", won")
        return True
    if board[0][2]==board[1][1] and board[1][1]==board[2][0] and board[1][1]==symbol:
        print(symbol, ", won")
        return True
    return False

def won(symbol):
    return check_rows(symbol) or check_col(symbol) or check_diag(symbol)

def play():
    for turn in range(9):
        if turn%2 == 0:
            print("Player X turn! ")
            place(p1s)
            if won(p1s):
                break
        else:
            print("Player O turn! ")
            place(p2s)
            if won(p2s):
                break
        turn+=1
    if not(won(p1s)) and not(won(p2s)):
        print("Draw")
            
play()