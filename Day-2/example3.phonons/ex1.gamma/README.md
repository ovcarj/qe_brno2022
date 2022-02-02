# PURPOSE OF THE EXERCISE: 
## Calculate the phonon frequencies at gamma-point. Calculate LO-TO splitting.
-------------------------------------------------------

**Steps to perform:**

1. SCF calculation:

       pw.x -in 01-nacl-scf.in | tee 01-nacl-scf.out


2. In this calculation, the `ph.x` input file 
   has a very simple structure:

       less 02-nacl-ph.in

   The documentation is at https://www.quantum-espresso.org/Doc/INPUT_PH.html


3. Run the calculation of phonon frequencies at gamma-point:

       ph.x -in 02-nacl-ph.in | tee 02-nacl-ph.out

   The phonon frequencies and the dynamical matrix is outputted
   to the `NaCl.dynG` file.


4. Get the frequencies:

       grep "freq" NaCl.dynG


5. Redo the calculation with the dielectric constant calculation included:

       ph.x -in 02-nacl-ph-epsil.in | tee 02-nacl-ph-epsil.out


6. Use `dynmat.x` to rediagonalize the dynamical matrix with the added 
   non-analytical term and imposed the acoustic sum rule:

       dynmat.x -in 03-nacl-dynmat.in | tee 03-nacl-dynmat.out 

   The documentation is at https://www.quantum-espresso.org/Doc/INPUT_DYNMAT.html


7. The LO-TO modes are now splitted:

       grep "freq" NaCl.phon


8. View the modes:

       xcrysden --axsf dynmat.axsf

   Press `f` to view the displacement directions.
   For a nicer view, you can press `translational asymmetric unit`
   at the bottom of the screen.


