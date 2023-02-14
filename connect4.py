import numpy as np
import pygame
import sys
import math

ROWS = 6
COLS = 7

def create_board():
  board = np.zeros((ROWS, COLS))
  return board

board = create_board()
game_over = False
turn = 0


while not game_over:
  #Player 1 move
  if turn == 0:
    selection = input()
  #PLayer 2 Move

