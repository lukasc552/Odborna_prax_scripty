import numpy as np
from scipy.signal import *
from scipy.integrate import odeint

import sys
import os
sys.path.append(os.getcwd())

# =========== Config grafov =========
save_fig = True
folder = ''
figName = folder + 'third'
figNameNum = 2
exec_file = 'misc/fig_prech1.py'
# ===================================

def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
#     return array[idx]
    return idx

# =============== Prenosova funkcia ================
num = [1]
den = [1, 3, 4, 2]

timevector = np.linspace(0, 10, 1001)

system1 = TransferFunction(num, den)
# state = StateSpace(system1)
t, y = step(system1, T=timevector)

# ziskanie rovnicu priamky - dotycnice v inflexnom bode
# y = slope*t + q
dyy = np.gradient(y, t)
dy = dyy.tolist()
max_value = max(dy)
max_idx = dy.index(max_value)
slope = dy[max_idx]
q = y[max_idx] - slope*t[max_idx]

time = np.linspace(0.5, 3.5)
yi = slope*time + q


if save_fig:
    exec(open(exec_file, encoding='utf-8').read())