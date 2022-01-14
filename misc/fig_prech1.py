# -*- coding: utf-8 -*-

from misc.figFcns_TeX import *


figPlotParam = fcnDefaultFigSize(11.0, 0.15, 0.96, 0.15, 0.5, 13)
fig = plt.figure(figNameNum, figsize=figPlotParam[0:2])

subPlots = gridspec.GridSpec(1, 1,
                             height_ratios=[40]
                             )
# ------------------
ax = plt.subplot(subPlots[0])

# ax.plot(t, y, lw=1.2, color='r', label='ODE solver')
ax.plot(t, y, lw=1.2, color='b')
# ax.plot(t, dy)
ax.plot(time, yi, lw=1.2,color='r', linestyle = '-.')
# ax.plot(t2, y2, lw=1.2, color='r', label='$w_0 = 0.5$')
# ax.plot(t3, y3, lw=1.2, color='g', label='$w_0 = 1$')
# ax.plot(t4, y4, lw=1.2, color='k', label='$w_0 = 2$')
# plt.axhline(y = 3, color = 'r', linestyle = '-.', label='K')
# ax.plot(t2, y2, lw=1.2, color='b')
# ax.plot(t2, y3, lw=1.2, color='b')
# plt.axhline(y = y63, color = 'r', linestyle = '-.', label='$y(T_{0.63})$')
# plt.axvline(x = t63, color = 'g', linestyle = '-.', label='$T_1=0.5$')
# plt.axvline(x = t263, color = 'g', linestyle = '-.', label='$T_2=1$')
# plt.axvline(x = t363, color = 'g', linestyle = '-.', label='$T_3=2$')
# ax.plot(t1, y1, '-', lw=1.2, color='r', label='step()')

# ax.plot(t_log, y_log_lti + y_pb_log, '-', lw=0.3, color='C0', label='y(t) + $y\_PB$(t)')
# ax.plot(t_log, y[:, 0], '-', lw=0.3, color='C1', label='$\\varphi$')

# ------------------

fcnDefaultLayoutAdj(fig, figPlotParam[2], figPlotParam[3], figPlotParam[4], figPlotParam[5])

fcnDefaultAxisStyle(ax)

ax.xaxis.set_minor_locator(AutoMinorLocator())
ax.yaxis.set_minor_locator(AutoMinorLocator())

# ax.xaxis.set_label_coords(1.01, -0.08)
# ax.yaxis.set_label_coords(-0.02, 1.05)

ax.set_xlabel(u'čas [s]', ha='center', va='center')
ax.set_ylabel(u'y(t)', ha='center', va='center')

# -----------------------------

handles_ax, labels_ax = ax.get_legend_handles_labels()

# -----------------------------
ax.legend(handles_ax, labels_ax, ncol=1, handlelength=1.2, loc=2, bbox_to_anchor=(1.01, 1.00))
plt.savefig('Figures/' + figName + '_{}'.format(figNameNum) +'.png', dpi=200)
plt.savefig('Figures/' + figName + '_{}'.format(figNameNum) +'.pdf')