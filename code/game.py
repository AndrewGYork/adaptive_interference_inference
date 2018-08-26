#!/usr/bin/python3
# Dependencies from the Scipy stack https://www.scipy.org/stackspec.html :
import numpy as np

class Oracle:
    def __init__(self, budget):
        assert budget > 0
        self.budget = budget
        self.total_cost = 0
        self.round = 0
        self.a_history = []
        self.b_history = []
        self.R_history = []
        self.game_over = False
        
        # Generate some secret numbers.
        # Don't peek!
        self._magnitude = np.random.random(1)
        self._phase = 2*np.pi*np.random.random(1)
        self._x = self._magnitude * np.exp(1j*self._phase)
        return None

    def ask(self, a, b):
        if self.game_over:
            return None
        self.total_cost += np.abs(a)**2
        if self.total_cost > self.budget:
            self.game_over = True
            return None
        y = np.abs(a*self._x + b)**2
        R = np.random.poisson(y)
        self.round += 1
        self.a_history.append(a)
        self.b_history.append(b)
        self.R_history.append(R)
        return R

if __name__ == '__main__':
    print("An example game")
    oracle = Oracle(budget=1000)
    print("Budget:", oracle.budget, '\n')
    while not oracle.game_over:
        print('Round', oracle.round)
        print('Total cost so far: %0.2f / %0.2f'%(oracle.total_cost, oracle.budget))
        a = 40*np.random.random(1)*np.exp(1j*2*np.pi*np.random.random(1))
        b = 40*np.random.random(1)*np.exp(1j*2*np.pi*np.random.random(1))
        print(' a: %07s    (intensity)\n'%('%0.2f'%(np.abs(a)**2)),
               '   %07s*pi (phase)'%('%0.2f'%(np.angle(a)/np.pi)))
        print(' b: %07s    (intensity)\n'%('%0.2f'%(np.abs(b)**2)),
               '   %07s*pi (phase)'%('%0.2f'%(np.angle(b)/np.pi)))
        response = oracle.ask(a, b)
        print('oracle.ask(a, b):', response, '\n')
    print("Budget exceeded; game over.")
    print("\nFrom these responses, how well can you infer 'x'?")
    print("\nIf you'd made smarter choices of 'a' and 'b' on each round,\n",
          "could you do a better job inferring 'x'?", sep='')
