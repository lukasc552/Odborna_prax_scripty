# -*- coding: utf-8 -*-

from misc.figFcns_TeX import *

# %% ---------------------------------------------------------------------------
"""
    zavolanie scriptu prikazom: 'exec(open('misc/fig_reg.py', encoding='utf-8').read())'

    Musia byt zadefinovane parametre:   figNameNum - cislo figure(okno grafu)
                                        t_log - casovy vektor
                                        sig_setpoint - vektor ziadanych hodnot prisluchajucich cas. vektoru
                                        u_log
                                        y
                                        e_log
                                        der_e_log
                                        int_e_log
"""
# %% ---------------------------------------------------------------------------

# figNameNum = 1
figPlotParam = fcnDefaultFigSize(18.0, 0.15, 0.96, 0.1, 0.45, 13)
fig = plt.figure(figNameNum, figsize=figPlotParam[0:2])

subPlots = gridspec.GridSpec(4, 1,
                             height_ratios=[40, 20, 20, 20]
                             )
# subPlots = gridspec.GridSpec(2, 1,
#                              height_ratios=[40, 40]
#                              )

# ------------------
ax0 = plt.subplot(subPlots[0])

ax0.plot(t_log, sig_setpoint,
         '-', lw=0.5, color='blue', dashes=[5, 2],
         label='$w(t)$',
         )

# ax0.plot(t_log, u_log,
#          '-', lw=0.5, color='k', ds='steps-post',
#          label='u(t)',
#          )

ax0.plot(t_log, y_log,
         '-', lw=1.0, color='r',
         label='$y(t)$',
         )

# ------------------
# ax0.set_title('Regulačný dej', x=0.01, y=1.02, ha='left')

# ------------------
ax1 = plt.subplot(subPlots[1])

ax1.plot(t_log, e_log,
         '-', lw=1.0, color='k', ds='steps-post',
         label='$e$(t)',
         )

# ------------------

ax2 = plt.subplot(subPlots[2])

ax2.plot(t_log, der_e_log,
         '-', lw=1.0, color='k', ds='steps-post',
         label='$\dot e$(t)',
         )

# ------------------
ax3 = plt.subplot(subPlots[3])

ax3.plot(t_log, int_e_log,
         '-', lw=1.0, color='k', ds='steps-post',
         label='$\int\, e(t)\, dt$',
         )
# ------------------
# ------------------
# ax4 = plt.subplot(subPlots[1])
#
#
# ax4.plot(t_log, u_log,
#          '-', lw=1.0, color='k', ds='steps-post',
#          label='$u$(t)',
#          )


fcnDefaultLayoutAdj(fig, figPlotParam[2], figPlotParam[3], figPlotParam[4], figPlotParam[5])

for ax in fig.get_axes():

    if ax in [ax0, ax1, ax2, ax3]:
        # if ax in [ax0, ax4]:

        fcnDefaultAxisStyle(ax)

        ax.xaxis.set_minor_locator(AutoMinorLocator())
        ax.yaxis.set_minor_locator(AutoMinorLocator())

        ax.xaxis.set_label_coords(1.01, -0.08)
        # ax.yaxis.set_label_coords(-0.02, 1.05)
        ax.yaxis.set_label_coords(-0.1, 0.4)

        ax.set_xlabel(u'čas [s]', ha='left', va='top')
        # if ax == ax0:
        #     ax.set_ylabel(u'$\\Delta{\\varphi}$ [rad]', ha='left', va='top')
        #
        # if ax == ax4:
        #     ax.set_ylabel(u'M [Nm]', ha='left', va='top')

    # -----------------------------

    handles_ax, labels_ax = ax.get_legend_handles_labels()

    if ax in [ax0, ax1, ax2, ax3]:
        # if ax in [ax0, ax4]:
        ax.legend(handles_ax, labels_ax, ncol=1, handlelength=1.2, loc=2, bbox_to_anchor=(1.01, 1.00))

# ------------------


# ------------------

plt.savefig('Figures/' + figName + '_{}'.format(figNameNum) + '.png', dpi=200)
plt.savefig('Figures/' + figName + '_{}'.format(figNameNum) + '.pdf')
