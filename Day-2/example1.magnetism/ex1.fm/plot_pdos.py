#/usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np

from sys import argv

""" END IMPORTS """

# read data into numpy arrays

data_file = 'PDOS/Fe.pdos_atm#1(Fe)_wfc#3(d)'

data = np.loadtxt(data_file, skiprows=1)

# energy (eV)
column1 = data[:, 0]

# d_z**2 up
column3 = data[:, 3]
# d_z**2 down
column4 = data[:, 4]

# d_xz up
column5 = data[:, 5]
# d_xz down
column6 = data[:, 6]

# d_yz up
column7 = data[:, 7]
# d_yz down
column8 = data[:, 8]

# d_x**2-y**2 up
column9 = data[:, 9]
# d_x**2-y**2 down
column10 = data[:, 10]

# d_xy up
column11 = data[:, 11]
# d_xy down
column12 = data[:, 12]

# set Fermi energy (eV)

E_F = 18.0753

# set energy zero to Fermi energy

column1 -= E_F

# Plot labels, title, file name to which the plot will be saved...

xlabel = 'E (eV)'
ylabel = 'States/eV'

title = 'Fe PDOS'
filename = 'Fe_PDOS.png'

# Define some nice colors

color1 = 'maroon'
color2 = 'tomato'
color3 = 'midnightblue'
color4 = 'deepskyblue'
color5 = 'lime'

# Plot

fig, ax = plt.subplots()

ax.plot(column1, column3, lw=2.5, label=r'$d_{z^2}$', color=color1)
ax.plot(column1, -column4, lw=2.5, color=color1)

ax.plot(column1, column5, lw=5.5, label=r'$d_{xz}$', color=color2, ls='--')
ax.plot(column1, -column6, lw=5.5, color=color2, ls='--')

ax.plot(column1, column7, lw=2.5, label=r'$d_{yz}$', color=color3)
ax.plot(column1, -column8, lw=2.5, color=color3)

ax.plot(column1, column9, lw=5.5, label=r'$d_{x^2-y^2}$', color=color4, ls='--', zorder=1)
ax.plot(column1, -column10, lw=5.5, color=color4, ls='--', zorder=1)

ax.plot(column1, column11, lw=6.5, label=r'$d_{xy}$', color=color5, ls='--', zorder=1)
ax.plot(column1, -column12, lw=6.5, color=color5, ls='--', zorder=1)


ax.axhline(y=0.0, xmin=-10, xmax=10, ls='-', color='black', lw=0.5, alpha=0.7)
ax.axvline(ymax=10, ls='--', color='black', label=r'$E_{F}$')

# Set title/labels

ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)
ax.set_title(title)

# Legend

ax.legend()

# Make the plot a bit prettier...

ax.tick_params(direction='in', which='both')
ax.set_xlim(left=-5.0, right=5.0)
ax.set_ylim(bottom=-1.0, top=1.0)
plt.tight_layout()

# Save the plot

fig.savefig(fname=filename, format='png', bbox_inches='tight')
plt.show()
