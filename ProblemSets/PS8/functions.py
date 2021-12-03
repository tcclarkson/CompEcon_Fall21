import numpy as np

def profit(pi, q, l, beta):
    '''
    Bellman equation for maximizing farmer value
    '''
    profit = pi * (q - l) + beta * pi * l
    return profit

'''
Defining parameters
------------------------------------------------------------------------
beta  = discount rate to sell all goods in period 2
pi    = profit in period
q     = quantity sold
l     = goods leftover from period 1
sigma = RRA
------------------------------------------------------------------------
'''

beta = 0.9
sigma = 1
R = 1


'''
------------------------------------------------------------------------
Create Grid for State Space    
------------------------------------------------------------------------
lb_q      = scalar, lower bound of crops grid
ub_q      = scalar, upper bound of crops grid 
size_q    = integer, number of grid points in crops state space
q_grid    = vector, size_q x 1 vector of crops grid points 
------------------------------------------------------------------------
'''
lb_q = 0.4 
ub_q = 2.0 
size_q = 1500  # Number of grid points
q_grid = np.linspace(lb_q, ub_q, size_q)

'''
------------------------------------------------------------------------
Create grid of current utility values    
------------------------------------------------------------------------
Q        = matrix, current period sales (Q = q - l)
V        = matrix, current period value for all possible
           choices of q and l (rows are q, columns l)
------------------------------------------------------------------------
'''
Q = np.zeros((size_q, size_q)) 
for i in range(size_q): # loop over q
    for j in range(size_q): # loop over l
        Q[i, j] = q_grid[i] - q_grid[j] / R # note that if l > q, consumption negative
# replace 0 and negative consumption with a tiny value 
# This is a way to impose non-negativity on cons
Q[Q<=0] = 1e-15
if sigma == 1:
    U = np.log(Q)
else:
    U = (Q ** (1 - sigma)) / (1 - sigma)
U[Q < 0] = -9999999

