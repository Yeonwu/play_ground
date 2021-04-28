import board
import numpy as np 
from os import system
import timeit
import datetime as dt
import random

env = board.Board()
Q = np.load('tictacto_model_2021-04-28-19-49-14.npy')

def step(action, turn):
    x = 0
    y = 0
    while 3 * (y + 1) <= action:
        y += 1
    x = action - 3 * y
    new_state = env.state()
    env.setXY(turn, x, y)
    return new_state

win_rate = 0
draw_rate = 0
defeat_rate = 0
play_time = 0

for _ in range(100):
    play_time += 1
    env.reset()
    done = False
    turn = False
    state = env.state()

    while not done:
       # env.render()

        if turn:
            #x, y = map(int, input("O TURN: ").split())
            #env.setXY(0, x, y)
            action = random.randint(0, 8)
            step(action, 0)
        else:
            action = np.argmax(Q[state, :])
            step(action, 1)

        turn = not turn
        state = env.state()
        done = env.checkWinner()
        
    # env.render()
    if done == 1:
        # print("WINNER: O")
        defeat_rate += 1
    elif done == -1:
        # print("WINNER: X")
        win_rate += 1
    else:
        # print("???")
        draw_rate += 1

print(f'Win rate: {win_rate / play_time * 100}%')
print(f'Draw rate: {draw_rate / play_time * 100}%')