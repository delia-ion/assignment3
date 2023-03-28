import numpy as np


class MyEGreedy:
    def __init__(self):
        print("Made EGreedy")

    def get_random_action(self, agent, maze):
        valid_actions = maze.get_valid_actions(agent)
        return np.random.choice(valid_actions)

    def get_best_action(self, agent, maze, q_learning):
        valid_actions = maze.get_valid_actions(agent)
        state = agent.get_state(maze)
        best_action = valid_actions[0]
        max_q = q_learning.get_q(state, best_action)

        for action in valid_actions[1:]:
            q = q_learning.get_q(state, action)
            if q > max_q:
                max_q = q
                best_action = action

        return best_action

    def get_egreedy_action(self, agent, maze, q_learning, epsilon):
         if np.random.random() < epsilon:
             return self.get_random_action(agent, maze)
         else:
             return self.get_best_action(agent, maze, q_learning)

