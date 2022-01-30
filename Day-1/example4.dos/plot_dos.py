#/usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np

from sys import argv

""" END IMPORTS """

# set Fermi energy (eV)

E_F = 16.502

# read data into numpy arrays

data_file = argv[1]

data = np.loadtxt(data_file, skiprows=1)

column1 = data[:, 0]
column2 = data[:, 1]

# set energy zero to Fermi energy

column1 -= E_F

# Plot labels, title, file name to which the plot will be saved...

xlabel = 'E (eV)'
ylabel = 'States/eV'
title = 'Ag DOS'
filename = 'Ag_DOS.png'

# Plot

fig, ax = plt.subplots()

ax.plot(column1, column2, lw=2.5)
ax.axvline(ymax=10, ls='--', color='black', label=r'$E_{F}$')

# Set title/labels

ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)
ax.set_title(title)

# Legend

ax.legend()

# Make the plot a bit prettier...

ax.tick_params(direction='in', which='both')
ax.set_xlim(left=-7.5, right=5.0)
ax.set_ylim(bottom=0.0, top=7.0)
plt.tight_layout()

# Save the plot

fig.savefig(fname=filename, format='png', bbox_inches='tight')
plt.show()
