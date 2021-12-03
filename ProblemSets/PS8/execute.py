import numpy as np
import functions as fn
import matplotlib as plt

VFtol = 1e-8 
VFdist = 7.0 
VFmaxiter = 3000 
V = np.zeros(fn.size_q)
Vmat = np.zeros((fn.size_q, fn.size_q))
Vstore = np.zeros((fn.size_q, VFmaxiter))
VFiter = 1 
while VFdist > VFtol and VFiter < VFmaxiter:  
    for i in range(fn.size_q): # loop over q
        for j in range(fn.size_q): # loop over l
            Vmat[i, j] = fn.U[i, j] + fn.beta * V[j] 
      
    Vstore[:, VFiter] = V.reshape(fn.size_q,)
    TV = Vmat.max(1)
    PF = np.argmax(Vmat, axis=1)
    VFdist = (np.absolute(V - TV)).max()
    V = TV
    VFiter += 1 
    


if VFiter < VFmaxiter:
    print('Value function converged after this many iterations:', VFiter)
else:
    print('Value function did not converge')


VF = V # solution to the functional equation

optQ = fn.q_grid[PF] # tomorrow's optimal crop size (savings function)
optU = fn.q_grid - optQ # optimal sales - get sales through the transition eqn

# Plot value function 
plt.figure()
plt.scatter(fn.q_grid[1:], VF[1:])
plt.xlabel('Size of Crop')
plt.ylabel('Value Function')
plt.title('Value Function - deterministic csales of crop')
plt.show()