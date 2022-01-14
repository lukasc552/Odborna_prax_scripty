import numpy as np
from scipy.signal import *

import sys
import os
sys.path.append(os.getcwd())

# =========== Config grafov =========
save_fig = True
folder = ''
figName = folder + 'prik4'
figNameNum = 1
exec_file = 'misc/fcns.py'
# ===================================

def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
#     return array[idx]
    return idx

# k_p = 3
# a = [0.5, 1]
# =============== Prenosova funkcia ================


timevector = np.linspace(0, 10, 1001)

# y = 2*np.exp(-3*timevector)*np.cos(timevector) + 2*np.exp(-3*timevector)*np.sin(1.867*timevector) + 2*timevector +1
y = np.exp(timevector) + np.exp(2*timevector) - 3*np.exp(timevector*2)








if save_fig:
    exec(open(exec_file, encoding='utf-8').read())