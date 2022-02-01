# PURPOSE OF THE EXERCISE:
## SCF calculation of an antiferromagnetic system. Hubbard U correction.
--------------------------------------------------------------------------------

**Steps to perform:**

1. Read the `01-nio-scf.in` file:

       less 01-nio-scf.in

   and see how we defined two different atom types for Ni.


2. The SCF calculation is pretty long (~10 minutes). 
   To save time, you can copy the results:

       cp -r reference/01-nio-scf/* .

   Otherwise, you can run it yourself in the usual way:

       pw.x -in 01-nio-scf.in | tee 01-nio-scf.out


3. Check the calculated magnetic moments per site:

       grep -A4 "Magnetic moment" 01-nio-scf.out


4. The DOS calculation is again rather long.
   You can copy the results:

       cp -r reference/0203-nio-dos/* .

   If you want to run it yourself:

       pw.x -in 02-nio-nscf.in | tee 02-nio-nscf.out
       dos.x -in 03-nio-dos.in | tee 03-nio-dos.out
       python plot_dos.py NiO-dos.dat


5. See how the DFT+U correction is incorporated into SCF calculations:

       less 01-nio-hub-scf.in


6. The results of the above calculations with the DFT+U correction
   are also given:

   To reproduce them, run:

       pw.x -in 01-nio-hub-scf.in | tee 01-nio-hub-scf.out
       pw.x -in 02-nio-hub-nscf.in | tee 02-nio-hub-nscf.out
       dos.x -in 03-nio-hub-dos.in | tee 03-nio-hub-dos.out
       python plot_dos.py NiO_hub-dos.dat


7. It's interesting to compare the d-orbital PDOS in calculations
   with and without the Hubbard correction:

       mkdir PDOS
       projwfc.x -in 04-nio-projwfc.in | tee 04-nio-projwfc.out
       projwfc.x -in 04-nio-hub-projwfc.in | tee 04-nio-hub-projwfc.out
       python plot_pdos.py no_hubbard
       python plot_pdos.py hubbard


