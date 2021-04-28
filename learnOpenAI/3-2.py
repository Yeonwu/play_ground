import tensorflow
import gym
import numpy as np
from gym.envs.registration import register

print("register...")
register(
    id="FrozenLake-v3",
    entry_point='gym.envs.toy_text:FrozenLakeEnv',
    kwargs={
        'map_name': '4x4',
        'is_slippery': False
    }
)

print("making gym...")
env = gym.make("FrozenLake-v3")

print("initiating Q-table...")
Q = np.zeros([env.observation_space.n, env.action_space.n])

print("initiating Other Values...")
dis = 0.99
num_episodes = 2000

rList = []

print("Started Learning")
for i in range(num_episodes):
    if not i % 100:
        print(f"Episode {i}")

    state = env.reset()
    rAll = 0
    done = False

    while not done:
        action = np.argmax(Q[state, :] + np.random.randn(1, env.action_space.n) / (i + 1))
        new_state, reward, done, _ = env.step(action)
        Q[state, action] = (reward + (dis * np.max(Q[new_state, :])))
        rAll += reward
        state = new_state

    rList.append(rAll)

print(f"Success Rate: {str(sum(rList)/num_episodes)}")
print("Q-Table")
print(Q) 