#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 14:33:06 2022
TFT Project
@author: wolschlag
"""
import random
from numpy.random import choice
import numpy as np
import pandas as pd

possible_moves = ['BS1', 'BS2', 'BS3', 'BS4', 'BS5', 'R', 'L',
                  'SA1', 'SA2', 'SA3','SA4', 'SA5', 'SA6', 'SA7', 'SA8', 'SA9',
                  'SB1', 'SB2', 'SB3', 'SB4', 'SB5', 'SB6', 'SB7', 'SB8', 'SB9',
                  'End']

all_slots = {'A1': "-",'A2': "-",'A3': "-",
            'A4': "-",'A5': "-",'A6': "-",
            'A7': "-",'A8': "-",'A9': "-",
            'B1': "-",'B2': "-",'B3': "-",
            'B4': "-",'B5': "-",'B6': "-",
            'B7': "-",'B8': "-",'B9': "-"}

game_continue = True
winner = None           
# Define Number of players
# players
current_player = "Player_1"

def display_board():
    print(" ")
    print("---S-T-A-R-T-I-N-G-----R-O-S-T-E-R----------------")
    print(" ")
    print("           " + all_slots['A1'] + "     |    " + all_slots['A2'] + "     |    " + all_slots['A3'])
    print("           _____________________")
    print("           " + all_slots['A4'] + "     |    " + all_slots['A5'] + "     |    " + all_slots['A6'])
    print("           _____________________")
    print("           " + all_slots['A7'] + "     |    " + all_slots['A8'] + "     |    " + all_slots['A9'])
    print(" ")
    print(" ")
    
    
    print("---B-E-N-C-H---------------------------------------------------")
    print(" " + all_slots['B1'] + "  |  " + all_slots['B2'] + "  | " + all_slots['B3'] + "  |  " + all_slots['B4'] + "  | " + all_slots['B5']+ "  |  " + all_slots['B6'] + "  | " + all_slots['B7']+ "  |  " + all_slots['B8'] + "  | " + all_slots['B9'])
    print("_______________________________________________________________")

display_board()

Cost1 = ["Brand", "Caitlyn", "Camille", "Darius", "Ezreal", "Illaoi", "Jarvan", "Kassadin", "Nocturne", "Poppy", "Singed", "Twitch", "Ziggs"]
Cost1_qty = 29 * Cost1
L1 = set(Cost1_qty)
# 377 total

Cost2 = ["Ashe", "Blitz", "Corki", "Lulu", "Quinn", "Rek_Sai", "Sejuani", "Swain", "Syndra", "Talon", "Warwick", "Zilean", "Zyra"]
Cost2_qty= 22 * Cost2
L2 = set(Cost2_qty)

Cost3 = ["ChoGath", "Ekko", "Gangplank", "Gnar", "Leona", "Lucian", "Malzahar", "MissFortune", "Morgana", "Senna", "Tryndamere", "Vex", "Zac"]
Cost3_qty = Cost3 * 18
L3 = set(Cost3_qty)

Cost4 = ["Ahri", "Alistar", "Braum", "Draven", "Irelia", "Jhin", "Kha'Zix", "Orianna", "RenataGlasc", "Seraphine", "Sivir", "Vi"]
Cost4_qty = Cost4 * 12
L4 = set(Cost4_qty)

Cost5 = ["Galio", "Jayce", "Jinx", "Kai_sa", "Silco", "TahmKench", "Viktor", "Zeri"]
Cost5_qty = Cost5 * 10
L5 = set(Cost5_qty)

All_Champs = Cost1_qty + Cost2_qty + Cost3_qty + Cost4_qty + Cost5_qty



# First 2 Shops
random.choice(Cost1_qty, k = 5)


#draw = random.uniform(low=0.0, high=1.0, size=None)
#if draw <= 0.4:
    #sample(Cost1_qty)



# Shop Odds by Level
# 1:100 2:0 3:0 4:0 5:0
# 1:100 2:0 3:0 4:0 5:0
# 1:75 2:25 3:0 4:0 5:0
# 1:55 2:30 3:15 4:0 5:0
# 1:45 2:33 3:20 4:2 5:0
# 1:25 2:40 3:30 4:5 5:0
# 1:19 2:30 3:35 4:15 5:1
# 1:16 2:20 3:35 4:25 5:4
# 1:9 2:15 3:30 4:30 5:16

# random.choices(population, weights=None, *, cum_weights=None, k=1)

# Choose elements with different probabilities

#L1.pop() for i in range (5)


def move_piece(current_player):
    global possible_moves
    print("________________")
    print(" ")
    print(current_player + "'s turn!")
    position = input( "Choose a position starting A-C and ending with 1-3: " )
# Game Process
    
# Change Player    
def change_player():
    global current_player
    if current_player == "Player_1":
        current_player = "Player_2"
    elif current_player == "Player_2":
        current_player = "Player_1"
        return

# Output [300 200 300 300]