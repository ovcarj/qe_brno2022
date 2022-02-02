# PURPOSE OF THE EXERCISE: 
## Calculate the phonon frequencies at gamma-point. Calculate LO-TO splitting.
-------------------------------------------------------

**Steps to perform:**

1. SCF calculation:

       pw.x -in 01-nacl-scf.in | tee 01-nacl-scf.out


2. Run the `ph.x` calculation on a uniform 3x3x3 grid:

       ph.x -in 02-nacl-ph.in | tee 02-nacl-ph.out

   Due to symmetry, the calculation is actually done for 4 wavenumbers
   listed in the `NaCl.dyn0` output file. The results for the respective
   wavenumbers are outputted to the `NaCl.dyn1-4` files.

   Note: the calculation takes ~20 minutes with 1 CPU. 
   To save time, you can copy the results from reference:

       cp reference/NaCl.dyn* .


3. Use the program `q2r.x` to calculate the interatomic force constants:

       q2r.x -in 03-nacl-q2r.in | tee 03-nacl-q2r.out


4. Calculate the frequencies along a 1BZ path using `matdyn.x`:

       matdyn.x -in 04-nacl-matdyn.in | tee 04-nacl-matdyn.out

   The path specified in `04-nacl-matdyn.in` is `GAMMA-L-K-GAMMA-X-U-L-W-GAMMA`.
   Such a path can be generated using XcrySDen.
   The results of the `matdyn.x` calculation are written to the file NaCl.freq


5. Note that the `matdyn.x` input documentation is in the QE source code:

       less ~/repo/q-e/PHonon/PH/matdyn.f90


6. Plot the dispersion:

       python plot_dispersion.py -img


7. `matdyn.x` can also be used to calculate the phonon DOS:

       matdyn.x -in 05-nacl-dos.in | tee 05-nacl-dos.out


8. Plot the DOS

       python plot_dos.py -img
