#!/usr/bin/python

import os
import sys
import re
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
#from mpl_toolkits.axes_grid.anchored_artists import AnchoredText

# ----------------------------------------

usage = """ \
        Usage: %s [OPTION...]
Options:
  -dat    <input file name> 
  -img    <write image file>
  -h      <this help>
""" % sys.argv[0]

# ---------------------------------------
#       Default parameters
# ---------------------------------------

img = 0
ffile = 'NaCl.freq'

omx = 300.0

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

# ----------------------------------------

if (ffile == ''):
	print >>sys.stderr, usage
	sys.exit(1)

# ----------------------------------------
#		Crystal data
# ----------------------------------------

# From 01-nacl-scf.out

a1 = [ -0.500000, 0.000000, 0.500000 ]
a2 = [  0.000000, 0.500000, 0.500000 ]
a3 = [ -0.500000, 0.500000, 0.000000 ]

# BZ special points: izvuceno iz supportInfo.kpath

sp = [ [r"$\Gamma$", [ 0.000,  0.000,  0,000 ]],
       [r"$L$",      [ 0.000,  0.000, -0.500 ]],
       [r"$K$",      [ 0.375,  0.000, -0.375 ]],
       [r"$X$",      [ 0.500,  0.500,  0.000 ]],
       [r"$U$",      [ 0.375,  0.375, -0.250 ]],
       [r"$W$",      [ 0.500,  0.250, -0.250 ]]  ]

# ----------------------------------------

xx = []
y1 = []; y2 = []; y3 = []; y4 = []; y5 = []; y6 = []
xt = []; xl = []

ff = open(ffile)

line  = ff.readline().strip()
i = 0
while (ff):
	#
	line  = ff.readline().strip()
	dd = line.split()
	if (len(dd) == 0): break
	kx=float(dd[0].strip());ky=float(dd[1].strip());kz=float(dd[2].strip())
	kk = [kx,ky,kz]
	k1 = np.dot( kk, a1 )
	if (k1 < -0.5): k1 += 1.0
	k2 = np.dot( kk, a2 );
	if (k2 < -0.5): k2 += 1.0
	k3 = np.dot( kk, a3 );
	if (k3 < -0.5): k3 += 1.0
	#
	line  = ff.readline().strip()
	dd = line.split()
	o1=float(dd[0].strip());o2=float(dd[1].strip());o3=float(dd[2].strip())
	o4=float(dd[3].strip());o5=float(dd[4].strip());o6=float(dd[5].strip())
	#
	if (len(xx)>0):
		dx = np.sqrt((kx-x0[0])**2+(ky-x0[1])**2+(kz-x0[2])**2)
		x = xx[-1]+dx
		x0 = [ kx, ky, kz ]
	else:
		x = 0.0
		x0 = [ kx, ky, kz ]
	xx.append( x )
	(o1,o2,o3,o4,o5,o6) = np.sort( [o1,o2,o3,o4,o5,o6] )
	y1.append( o1 )
	y2.append( o2 )
	y3.append( o3 )
	y4.append( o4 )
	y5.append( o5 )
	y6.append( o6 )
	#
	for j in range(len(sp)):
		q1 = sp[j][1][0] ; q2 = sp[j][1][1] ; q3 = sp[j][1][2]
		if   ( abs(k1-q1) + abs(k2-q2) + abs(k3-q3) < 0.001 ):
			xt.append( x ); xl.append( sp[j][0] )
ff.close()

# ====================================

mpl.rcParams['lines.linewidth'] = 2
mpl.rcParams['xtick.major.size'] = 0
llines  = [ 'r-','g-','b-','y-','c-','m-' ]

fig = plt.figure(1)
ax = plt.subplot(111)

#at = AnchoredText("NaCl", prop=dict(size=30), loc=9 )
#ax.add_artist(at)

plt.plot( xx, y1, llines[0] )
plt.plot( xx, y2, llines[1] )
plt.plot( xx, y3, llines[2] )
plt.plot( xx, y4, llines[3] )
plt.plot( xx, y5, llines[4] )
plt.plot( xx, y6, llines[5] )

plt.ylabel(r"Phonon frequencies (cm$^{-1}$)")
for i in range(len(xt)):
	plt.plot( [xt[i],xt[i]], [0.0,omx], 'k-' )
plt.xticks( xt, xl, size='x-large' )

plt.xlim( [xt[0],xt[-1]] )
plt.ylim( [0.0,omx] )

if (img):
	ifile = re.sub(".freq$","",ffile) + '-freq'
	plt.savefig( ifile+'.png',dpi=300,bbox_inches='tight',pad_inches=0.1)
#	plt.savefig( ifile+'.pdf',dpi=300,bbox_inches='tight',pad_inches=0.1)

plt.show()
