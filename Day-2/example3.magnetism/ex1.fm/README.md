# PURPOSE OF THE EXERCISE:
## SCF calculation of a ferromagnetic system. Plotting DOS projected to atomic orbitals.
--------------------------------------------------------------------------------

**Steps to perform:**

1. Read the `01-fe-scf.in` file:

       less 01-fe-scf.in

   and notice the appearance of new variables `nspin` and `starting_magnetization(i)`.


2. Run the spin-polarized SCF calculation:

       pw.x -in 01-fe-scf.in | tee 01-fe-scf.out


3. The total and absolute magnetization are written during
   the SCF cycles:

       grep -A1 "total magnetization" 01-fe-scf.out


4. The final magnetic moment per site can be extracted like this:

       grep -A2 "Magnetic moment" 01-fe-scf.out


5. Run the same calculation with `starting_magnetization(1)=0.0`:

       pw.x -in 01-fe-nfm-scf.in | tee 01-fe-nfm-scf.out

   and confirm that a nonmagnetic state is obtained. 


6. Compare the energies between the magnetic and nonmagnetic state:

       grep "!" 01-fe-scf.out 01-fe-nfm-scf.out


7. Run the usual DOS calculations:

       pw.x -in 02-fe-nscf.in | tee 02-fe-nscf.out
       pw.x -in 02-fe-nfm-nscf.in | tee 02-fe-nfm-nscf.out
       dos.x -in 03-fe-dos.in | tee 03-fe-dos.out
       dos.x -in 03-fe-nfm-dos.in | tee 03-fe-nfm-dos.out

   Notice that spin-up and spin-down densities are separated
   in the `Fe-dos.dat` and `Fe_nfm-dos.dat` files.


8. Plot the calculated DOS's:

       python plot_dos.py Fe-dos.dat
       python plot_dos.py Fe_nfm-dos.dat


9. Calculate the DOS projected onto localized atomic orbitals (pDOS):

       mkdir PDOS
       projwfc.x -in 04-fe-projwfc.in | tee 04-fe-projwfc.out

   Take a look at the output file `04-fe-projwfc.out` and the directory PDOS.
   projwfc.x documentation can be found at https://www.quantum-espresso.org/Doc/INPUT_PROJWFC.html


10. Plot the PDOS:

       python plot_pdos.py
