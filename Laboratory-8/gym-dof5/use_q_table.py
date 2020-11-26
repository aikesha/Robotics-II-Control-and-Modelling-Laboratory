import ast
import gym
import gym_dof5
import qlearn
import time
import matplotlib.pyplot as plt

def choose_action(qtable, state):
    q = [qtable.get((state, a), 0.0) for a in range(10)]
    return q.index(max(q))



if __name__ == '__main__':
    f = open("qtable.txt", "r")
    cont = f.read()
    qtable = ast.literal_eval(cont)
    env = gym.make('Planar5DoF-v0')
    highest_reward = 0
    for x in range(100):
        total_reward = 0
        if (x == 0):
            time.sleep(3) # to load all controllers first
        print("New episode #" + str(x))
        state = env.reset()
        for i in range(20):
            print("New step "+str(i))
            action = choose_action(qtable, state)
            new_state, reward, done, info = env.step(action)
            total_reward += reward


            if (done):
                break
            else:
                state = new_state
        print("Episode #"+str(x)+" has ended, total reward is "+str(total_reward))
    f.close()
