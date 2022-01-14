import numpy as np
from scipy.signal import *

import sys
import os
sys.path.append(os.getcwd())

# =========== Config grafov =========
save_fig = True
folder = ''
figName = folder + 'prech'
figNameNum = 2
exec_file = 'misc/fig_prech1.py'
# ===================================

def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
#     return array[idx]
    return idx

k_p = 3
a = [0.5, 1]
# =============== Prenosova funkcia ================
num = [k_p]
den = [a[0], a[1]]

timevector = np.linspace(0, 10, 101)

system1 = TransferFunction(num, den)
# state = StateSpace(system1)
t, y = step(system1,T=timevector)

y63_idx = find_nearest(y, 3*0.63)
y63 = y[y63_idx]
t63 = t[y63_idx]


den[0] = 1


system2 = TransferFunction(num, den)
# state = StateSpace(system1)
t2, y2 = step(system2, T=timevector)

y263_idx = find_nearest(y2, 3*0.63)
y263 = y2[y263_idx]
t263 = t2[y263_idx]

den[0] = 2

system3 = TransferFunction(num, den)
# state = StateSpace(system1)
t3, y3 = step(system3, T=timevector)

y363_idx = find_nearest(y3, 3*0.63)
y363 = y3[y363_idx]
t363 = t3[y363_idx]

if save_fig:
    exec(open(exec_file, encoding='utf-8').read())