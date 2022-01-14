import numpy as np
from scipy.signal import *

import sys
import os
sys.path.append(os.getcwd())

# =========== Config grafov =========
save_fig = True
folder = ''
figName = folder + 'kmitava'
figNameNum = 3
exec_file = 'misc/fig_prech1.py'
# ===================================

def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
#     return array[idx]
    return idx

# =============== Prenosova funkcia ================
K = 1
xi = 0.2
w = 0.2
num = [K*(w**2)]
den = [1, 2*xi*w, (w**2)]

timevector = np.linspace(0, 30, 3001)

system1 = TransferFunction(num, den)
# state = StateSpace(system1)
t, y = step(system1, T=timevector)

# xi = 0.5
# den[1] = 2*xi*w
# system1 = TransferFunction(num, den)
# t2, y2 = step(system1, T=timevector)
#
# xi = 1
# den[1] = 2*xi*w
# system1 = TransferFunction(num, den)
# t3, y3 = step(system1, T=timevector)
#
# xi = 2
# den[1] = 2*xi*w
# system1 = TransferFunction(num, den)
# t4, y4 = step(system1, T=timevector)

w = 0.5
num = [K*(w**2)]
den = [1, 2*xi*w, (w**2)]
system1 = TransferFunction(num, den)
t2, y2 = step(system1, T=timevector)

w = 1
num = [K*(w**2)]
den = [1, 2*xi*w, (w**2)]
system1 = TransferFunction(num, den)
t3, y3 = step(system1, T=timevector)

xi = 2
num = [K*(w**2)]
den = [1, 2*xi*w, (w**2)]
system1 = TransferFunction(num, den)
t4, y4 = step(system1, T=timevector)



if save_fig:
    exec(open(exec_file, encoding='utf-8').read())