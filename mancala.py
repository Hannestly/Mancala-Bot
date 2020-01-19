#!/usr/bin/python

def printNextMove(player, player1Mancala, player1Marbles, player2Mancala, player2Marbles):
    print ""

player = input()
mancala1 = input()
mancala1_marbles = [int(i) for i in raw_input().strip().split()]
mancala2 = input()
mancala2_marbles = [int(i) for i in raw_input().strip().split()]
print printNextMove(player, mancala1, mancala1_marbles, mancala2, mancala2_marbles)