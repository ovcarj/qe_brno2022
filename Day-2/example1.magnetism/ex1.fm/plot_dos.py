#/usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np

from sys import argv

""" END IMPORTS """

# read data into numpy arrays

data_file = argv[1]

data = np.loadtxt(data_file, skiprows=1)

column1 = data[:, 0]
column2 = data[:, 1]
column3 = data[:, 2]

# set Fermi energy (eV)

if 'nfm' in data_file:
    E_F = 18.191

else:
    E_F = 18.074

# set energy zero to Fermi energy

column1 -= E_F

# Plot labels, title, file name to which the plot will be saved...

xlabel = 'E (eV)'
ylabel = 'States/eV'

if 'nfm' in data_file:
    title = 'Fe (nonmagnetic) DOS'
    filename = 'Fe_nfm_DOS.png'

else:
    title = 'Fe DOS'
    filename = 'Fe_DOS.png'

# Plot

fig, ax = plt.subplots()

ax.plot(column1, column2, lw=2.5, color='darkred', label='Spin up')
ax.plot(column1, -column3, lw=2.5, color='midnightblue', label='Spin down')
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
ax.set_ylim(bottom=-7.0, top=7.0)
plt.tight_layout()

# Save the plot

fig.savefig(fname=filename, format='png', bbox_inches='tight')
plt.show()
