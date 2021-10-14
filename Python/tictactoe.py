#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 16:28:29 2021

@author: wolschlag
"""

possible_moves = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']

ttt = {'A1': "-",'A2': "-",'A3': "-",
       'B1': "-",'B2': "-",'B3': "-",
       'C1': "-",'C2': "-",'C3': "-"}

game_continue = True
winner = None
current_player = "X"


def display_board():
    print("---------------")
    print(" " + ttt['A1'] + "  |  " + ttt['B1'] + "  | " + ttt['C1'])
    print("_______________")
    print(" " + ttt['A2'] + "  |  " + ttt['B2'] + "  | " + ttt['C2'])
    print("_______________")
    print(" " + ttt['A3'] + "  |  " + ttt['B3'] + "  | " + ttt['C3'])
    

def play():
    display_board()
    
    while game_continue:
            move_piece(current_player)
            
            game_over_check()
            
            swap_turn()
           
    #game ends
    if winner == "X" or winner == "O":
        print(winner + "  is the winner! Congrats!")
    elif winner == None:
        print("Tie! (Cat's Game!)")
    

def move_piece(current_player):
    global possible_moves
    print("________________")
    print(" ")
    print(current_player + "'s turn!")
    position = input( "Choose a position starting A-C and ending with 1-3: " )
    
    valid = False
    while not valid:
        while position not in ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']:
            position = input( "Invalid Placement ... Try again (A-C) + (1-3):  " )
            
        if ttt[position] == "-":
            valid = True
        else:
            print("You can't go here, Try Again")
            position = input( "Invalid Placement ... Try again (A-C) + (1-3):  " )
            
            
        
    ttt[position] = current_player
    display_board()
    game_over_check() 

def game_over_check():
    win_check()
    
    tie_check()
    

def check_rows():
    #set up global 
    global game_continue
    row_1 = ttt['A1'] == ttt['B1'] == ttt['C1'] != "-"
    row_2 = ttt['A2'] == ttt['B2'] == ttt['C2'] != "-"
    row_3 = ttt['A3'] == ttt['B3'] == ttt['C3'] != "-"
    if row_1 or row_2 or row_3:
        game_continue = False
    if row_1:
        return ttt['A1']
    elif row_2:
        return ttt['A2']
    elif row_3:
        return ttt['A3']
    return

def check_cols():
    global game_continue
    col_A = ttt['A1'] == ttt['A2'] == ttt['A3'] != "-"
    col_B = ttt['B1'] == ttt['B2'] == ttt['B3'] != "-"
    col_C = ttt['C1'] == ttt['C2'] == ttt['C3'] != "-"
    if col_A or col_B or col_C:
        game_continue = False
    if col_A:
        return ttt['A1']
    elif col_B:
        return ttt['B1']
    elif col_C:
        return ttt['C1']
    return

def check_diags(): 
    global game_continue
    diag_1 = ttt['A1'] == ttt['B2'] == ttt['C3'] != "-"
    diag_2 = ttt['C1'] == ttt['B2'] == ttt['A3'] != "-"
    if diag_1 or diag_2:
        game_continue = False
    if diag_1:
        return ttt['A1']
    elif diag_2:
        return ttt['C1']
    return
    
def win_check():
    global winner
    #check rows
    row_winner = check_rows()
    #check columns
    col_winner = check_cols()
    #check diags
    diag_winner = check_diags()
    if row_winner:
        winner = row_winner
    elif col_winner:
        winner = col_winner
    elif diag_winner:
        winner = diag_winner
    else:
        winner = None   
    return

def tie_check():
    global game_continue
    if "-" not in ttt.values():
        game_continue = False
    return

def swap_turn():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
        return

play()    
