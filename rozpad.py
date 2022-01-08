import numpy as np
import matplotlib.pyplot as plt


import sys
import os
sys.path.append(os.getcwd())

# =========== Config grafov =========
save_fig = True
folder = ''  # 'Kyvadlo/URO/prve/'
figName = folder + 'rozpad'
figNameNum = 1
exec_file = 'fig_system.py'
# ===================================


def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
#     return array[idx]
    return idx


Q0 = 4
tau = 6.7*365*24*60*60 # polcas rozpadu 228Ra 6.7rokov
k = np.log(2)/tau
timevector = np.linspace(0, tau*4, 1001)

y = Q0 * np.exp(-k*timevector)

# plt.plot(timevector/(365*24*60*60), Q)
# plt.grid()
# plt.xlabel('t [s]')
# plt.ylabel('Q(t)')
# plt.show()

t = timevector/(365*24*60*60)

if save_fig:
    exec(open('misc/' + exec_file, encoding='utf-8').read())

