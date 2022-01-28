#/usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np

from sys import argv

""" END IMPORTS """

# read data into numpy arrays

data_file = argv[1]

data = np.loadtxt(data_file)

column1 = data[:, 0]
column2 = data[:, 1]

# Plot labels, title, file name to which the plot will be saved...

xlabel = 'ecutwfc (Ry)'
ylabel = 'Total energy (Ry)'
title = 'Plane wave energy convergence test'
filename = 'ecut_vs_energy.png'

# Plot

fig, ax = plt.subplots()

ax.plot(column1, column2)
ax.scatter(column1, column2)

# Set title/labels

ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)
ax.set_title(title)

# Make the plot a bit prettier...

ax.tick_params(direction='in', which='both')
plt.tight_layout()

# Save the plot

fig.savefig(fname=filename, format='png', bbox_inches='tight')
plt.show()
