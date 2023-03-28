from QLearning import QLearning

class MyQLearning(QLearning):
    def update_q(self, state, action, r, state_next, possible_actions, alfa, gamma):
        current_q = self.get_q(state, action)
        max_q_next = max([self.get_q(state_next, a) for a in possible_actions])
        new_q = current_q + alfa * (r + gamma * max_q_next - current_q)
        self.set_q(state, action, new_q)
