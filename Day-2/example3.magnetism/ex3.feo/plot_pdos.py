#/usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np

from sys import argv

""" END IMPORTS """

# read data into numpy arrays

hubbard = argv[1]

if hubbard == 'hubbard':
     data_file1 = 'PDOS/feo_hub.pdos_atm#1(Fe1)_wfc#5(d)'
     data_file2 = 'PDOS/feo_hub.pdos_atm#2(Fe2)_wfc#5(d)'
     data_file3 = 'PDOS/feo_hub.pdos_atm#3(O)_wfc#2(p)'

else:
     data_file1 = 'PDOS/feo.pdos_atm#1(Fe1)_wfc#5(d)'
     data_file2 = 'PDOS/feo.pdos_atm#2(Fe2)_wfc#5(d)'
     data_file3 = 'PDOS/feo.pdos_atm#3(O)_wfc#2(p)'

data1 = np.loadtxt(data_file1, skiprows=1)
data2 = np.loadtxt(data_file2, skiprows=1)
data3 = np.loadtxt(data_file3, skiprows=1)

# energy (eV)
column1 = data1[:, 0]

# Fe 3d majority spin
column2 = data1[:, 2]
# Fe 3d minority spin
column3 = data2[:, 2]
# O 2p
column4 = data3[:, 2]

# set Fermi energy (eV)

if hubbard == 'hubbard':
     E_F = 13.6125

else:
    E_F = 13.7043

# set energy zero to Fermi energy

column1 -= E_F

# Plot labels, title, file name to which the plot will be saved...

xlabel = 'E (eV)'
ylabel = 'States/eV'

if hubbard == 'hubbard':
    title = 'FeO PDOS (Hubbard correction)'
    filename = 'FeO_PDOS_hubbard.png'

else:
    title = 'FeO PDOS (no correction)'
    filename = 'FeO_PDOS_noCorr.png'

# Define some nice colors

color1 = 'maroon'
color2 = 'tomato'
color3 = 'midnightblue'
color4 = 'deepskyblue'
color5 = 'lime'

# Plot

fig, ax = plt.subplots()

ax.plot(column1, column2, lw=2.5, label='Fe-3d (majority spin)', color=color1)
ax.plot(column1, column3, lw=2.5, label='Fe-3d (minority spin)', color=color2)
ax.plot(column1, column4, lw=2.5, label='O-2p', color=color3)

ax.axvline(ymax=10, ls='--', color='black', label=r'$E_{F}$')

# Set title/labels

ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)
ax.set_title(title)

# Legend

ax.legend()

# Make the plot a bit prettier...

ax.tick_params(direction='in', which='both')
ax.set_xlim(left=-4.0, right=2.4)
ax.set_ylim(bottom=0.0, top=8.0)
plt.tight_layout()

# Save the plot

fig.savefig(fname=filename, format='png', bbox_inches='tight')
plt.show()
