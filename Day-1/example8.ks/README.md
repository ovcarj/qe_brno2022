# PURPOSE OF THE EXERCISE: 
## How to calculate and plot molecular orbitals of benzene
-------------------------------------------------------

**Disclaimer**

This exercise is adapted from 
https://gitlab.com/QEF/material-for-ljubljana-qe-summer-school/-/tree/master/Day-1/example1.benzene

**Steps to perform:**

1. Read the `01-benzene-scf.in` file.

       less 01-benzene-scf.in

   Notice the appearance of a new variable `assume_isolated`.
   Note that only gamma is specified as a k-point.


2. Run the SCF calculation to calculate the Kohn-Sham states:

       pw.x -in 01-benzene-scf.in | tee 01-benzene-scf.out


3. Run the postprocessing calculation of all valence and LUMO
   molecular orbitals ( actually sign(psi(r)) * |psi(r)|^2 )

       pp.x -in 02-benzene-pp.in | tee 02-benzene-pp.out

   the resulting sign(psi(r)) * |psi(r)|^2 are written to files
   `psi2.benzene_K001_B0*.xsf`


4. Plot one of the generated .xsf files with XcrySDen:

       xcrysden --xsf psi2.benzene_K001_B006.xsf

   The plotting procedure is analogous to plotting of charge density.


5. To plot all the molecular orbitals, execute the `plot-psi.sh` shell script:

       ./plot-psi2.sh


6. Look at the plotted orbitals:

       eog montage.png

