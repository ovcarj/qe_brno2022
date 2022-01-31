#!/usr/bin/python

# Example:
# python plot_band-QE.py -dat Ag-bands.dat -ef 16.4458

import os
import sys
import re
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid.anchored_artists import AnchoredText

# =====================================================================
# CONFIGURE, CONFIGURE, CONFIGURE
# =====================================================================
# Look at: ag-scf.out		-> a_i vec
#          ag-bands.in		-> kp
# =====================================================================

# unit cell vectors (a_i vec)

a1 = [ -0.500000,   0.000000,   0.500000 ]
a2 = [  0.000000,   0.500000,   0.500000 ]
a3 = [ -0.500000,   0.500000,   0.000000 ]

# special BZ points and their coordinates (see also `supportInfo.kpath`)

kp = [  [r'$W$',        [-0.250,     0.250,    -0.500]],
        [r'$L$',        [ 0.000,     0.500,     0.000]],
        [r'$\Gamma$',   [ 0.000,     0.000,     0.000]],
        [r'$X$',        [-0.500,     0.000,    -0.500]],
        [r'$K$',        [ 0.000,     0.375,    -0.375]] ]

# =====================================================================
#			END OF CONFIGURATION
# =====================================================================

# ----------------------------------------
#               help
# ---------------------------------------

usage = """ \
        Usage: %s [OPTION...]
Options:
  -dat    <input file name>                      - MUST BE PROVIDED
  -ef     <Fermi energy>                         - MUST BE PROVIDED
  -emn    <minimal energy>
  -emx    <maximal energy>
  -img    <write image file>
  -h      <this help>
""" % sys.argv[0]

# ---------------------------------------
#       Default parameters
# ---------------------------------------

img = 0
ffile = ''
ef  = -100.0	# eV
emn = -8.0
emx = +6.0

# ---------------------------------------
#       command line parameters
# ---------------------------------------

i = len(sys.argv)
j = 1
while (i > j):
        if sys.argv[j] == '-dat' :
                j = j+1
                ffile = sys.argv[j]
        elif sys.argv[j] == '-emn' :
                j = j+1
                emn = float(sys.argv[j])
        elif sys.argv[j] == '-emx' :
                j = j+1
                emx = float(sys.argv[j])
        elif sys.argv[j] == '-ef' :
                j = j+1
                ef = float(sys.argv[j])
        elif sys.argv[j] == '-img' :
                img = 1
        elif sys.argv[j] == '-h' :
                print( usage, file=sys.stderr)
                sys.exit(1)
        else:
                print( usage, file=sys.stderr)
                sys.exit(1)
        j = j+1

# ---------------------------------------
#		TESTS
# ---------------------------------------

if (ffile == ''):
        print( usage, file=sys.stderr)
        sys.exit(1)

if (ef == -100.0):
        print( usage, file=sys.stderr)
        sys.exit(1)

# ---------------------------------------
#		DATA READING
# ---------------------------------------

try:
        ff = open(ffile)
except:
        print( 'no input file:',ffile )
        sys.exit(1)

line  = ff.readline().strip()
dat = re.match('.*=\s*(\d+), nks=\s*(\d+)\s*/.*',line).groups()
nband  = int( dat[0] )          # bands
npoint = int( dat[1] )          # Qs

xx = []
yy = []
xt = []; xl = []

ko = [ 0.0,0.0,0.0 ]
for i in range(nband): yy.append( [] )

for n in range(npoint):
	#
	line = ff.readline().strip()
	#
	qq = [ float(x) for x in line.split() ]		# Cartesian coordinates
	k1 = np.dot( qq, a1 )
	if (k1 < -0.5): k1=k1+1.0
	k2 = np.dot( qq, a2 )
	if (k2 < -0.5): k2=k2+1.0
	k3 = np.dot( qq, a3 )
	if (k3 < -0.5): k3=k3+1.0
	#					k1,k2,k3 - Crystal coordinates
	if (n == 0):
		x = 0.0
	else:
		dx = np.sqrt((qq[0]-q0[0])**2+(qq[1]-q0[1])**2+(qq[2]-q0[2])**2)
		x = xx[-1]+dx
	xx.append( x )
	q0 = qq
	#
	# ---------------------------------------
	#         PATHs in BRILLOUIN ZONE
	# ---------------------------------------
	#
	for j in range(len(kp)):
		q1,q2,q3 = kp[j][1][0],kp[j][1][1],kp[j][1][2]
		if (abs(k1-q1) + abs(k2-q2) +abs(k3-q3) < 0.005):
			xt.append( x ); xl.append( kp[j][0] )

	#
	#
	# energies
	#
	en = []
	zz = len(en)
	while (zz < nband):
		line = ff.readline().strip()
		el = line.split()
		zl = len(el)
		for i in range(zl):
			en.append( float(el[i]) )
		zz += zl
	#
	if (nband != len(en)):
		print( "something wrong!" )
		sys.exit()
	en = np.sort( en )
	#
	for i in range(nband): yy[i].append( en[i]-ef )
ff.close()

ss = []

for band in range(nband):
	ss.append( False )
	for n in range(npoint):
		ee = yy[band][n]
		if ((ee < emx) and (ee > emn)): ss[band] = True

# ====================================
#		PLOT
# ====================================

mpl.rcParams['lines.linewidth'] = 2
mpl.rcParams['xtick.major.size'] = 0

#llabels = ( "Total", "Nb", "S"  )
llines  = [ 'r-','g-','b-','y-','c-','m-' ]

fig = plt.figure(1)
ax = plt.subplot(111)

# at = AnchoredText("Silver", prop=dict(size=20), loc=1 )
# ax.add_artist(at)

li=0
for band in range(nband):
	if ss[band]:
		plt.plot( xx, yy[band], llines[li%len(llines)])
		li = li+1

plt.plot( [xx[0],xx[-1]],[0.0,0.0], 'k--')
for i in range(len(xt)): plt.plot( [xt[i],xt[i]], [emn,emx], 'k-' )

plt.xticks( xt, xl, fontsize=10 )
plt.ylabel("Energy (eV)", fontsize=16)
plt.xlim( [xx[0], xx[-1]] )
plt.ylim( [emn, emx] )

#plt.axes().set_aspect( 0.2 )

if img:
	imgfile = ffile
	imgfile = re.sub(".dat$","",ffile)
	plt.savefig(imgfile+'.png',dpi=300,bbox_inches='tight',pad_inches=0.1)
#	plt.savefig(imgfile+'.pdf',dpi=300,bbox_inches='tight',pad_inches=0.1)

plt.show()
