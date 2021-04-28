import board
import numpy as np 
from os import system
import timeit
import datetime as dt

env = board.Board()
Q = np.zeros([2 ** 18, 9])
P = np.zeros([2 ** 18, 9])

dis = 0.99
num_episodes = 0

def step(action, turn):
    x = 0
    y = 0
    while 3 * (y + 1) <= action:
        y += 1
    x = action - 3 * y
    result = env.setXY(turn, x, y)
    new_state = env.state()
    reward = env.checkWinner()

    done = False if reward == 0 else True

    if not turn:
        reward = reward * -1
    if not result:
        reward -= 10

    return new_state, reward, done

rList = []
start_time = timeit.default_timer()
num_episodes = -1
while True:
    num_episodes += 1
    env.reset()
    state = env.state()
    rAll = 0
    done = False
    turn = True
    cnt = 0

    if not (num_episodes+1) % 100000:
        print(f'Episode {num_episodes} ')
        terminate_time = timeit.default_timer()
        if terminate_time - start_time > 100:
            break


    while not done:
        if cnt > 100:
            print('Infinite Loop')
            quit()
        cnt += 1
        if turn:
            action = np.argmax(Q[state, :] + np.random.randn(1, 9) / (num_episodes + 1))
            new_state, reward, done = step(action, turn)
            Q[state, action] = (reward + (dis * np.max(Q[new_state, :])))
            rAll += reward
            state = new_state
        else:
            action = np.argmax(P[state, :] + np.random.randn(1, 9) / (num_episodes + 1))
            new_state, reward, done = step(action, turn)
            P[state, action] = (reward + (dis * np.max(P[new_state, :])))
            rAll += reward
            state = new_state

        turn = not turn
terminate_time = timeit.default_timer()

print(f'{num_episodes} times learing takes {terminate_time - start_time} sec')

env.reset()
done = False
turn = True
while not done:
    env.render()

    if turn:
        x, y = map(int, input("O TURN: ").split())
        env.setXY(0, x, y)
    else:
        action = np.argmax(Q[state, :])
        step(action, 1)

    turn = not turn
    done = env.checkWinner()
    
env.render()
if done == 1:
    print("WINNER: O")
elif done == -1:
    print("WINNER: X")
else:
    print("???")

S = (Q + P) / 2

np.save(f'C:/old_codes/play_ground/tictacto_model_{dt.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}', S)
