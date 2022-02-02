#!/usr/bin/python

import sys, getopt, string
import re
import numpy as np
import matplotlib.pyplot as plt

#

# ---------------------------------------
#               help
# ---------------------------------------


usage = """ \
        Usage: %s [OPTION...]
Options:
  -dat    <data file> 
  -img    <write image file>
  -h      <this help>
""" % sys.argv[0]

# ---------------------------------------
#       Default parameters
# ---------------------------------------

img = 0
ffile = 'NaCl-phdos.dat'

# ---------------------------------------
#       command line parameters
# ---------------------------------------

i = len(sys.argv)
j = 1
while (i > j):
        if sys.argv[j] == '-dat' :
                j = j+1
                ffile = sys.argv[j]
        elif sys.argv[j] == '-img' :
                img = 1
        elif sys.argv[j] == '-h' :
                print >>sys.stderr, usage
                sys.exit(1)
        else:
                print >>sys.stderr, usage
                sys.exit(1)
        j = j+1

# ---------------------------------------

if (ffile == ''):
        print >>sys.stderr, usage
        sys.exit(1)

# ---------------------------------------

try:
        ff = open(ffile)
except:
        print('no dos file:'), ffile
        sys.exit(1)

fq = []
dos = []
dmx = 0.0
line  = ff.readline().strip()

while(ff):
	line  = ff.readline().strip()
	dd = line.split()
	if (len(dd) <= 0): break
	f = float(dd[0].strip())
	d = float(dd[1].strip())
	fq.append( f  )
	dos.append( d )
	dmx = max(dmx,d)

ff.close()

# ---------------------------------------

plt.figure(1)
ax = plt.subplot(111)

col = ['r-','g-','b-','y-','c-','m-' ]

plt.plot( fq,dos, 'r-', linewidth=2 )
plt.xlabel(r'$\omega$ (cm$^{-1}$)')
plt.ylabel(r'Phonon DOS')
plt.xlim( [0.0, 300.])
plt.ylim( [0.0, 1.05*max(dos) ])

if (img):
	imgfile = ffile
	imgfile = re.sub(".dat$","",ffile);
	plt.savefig(imgfile+'.png',dpi=300,bbox_inches='tight',pad_inches=0.1)
#	plt.savefig(imgfile+'.pdf',dpi=300,bbox_inches='tight',pad_inches=0.1)

plt.show()

