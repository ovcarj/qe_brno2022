# PURPOSE OF THE EXERCISE: 
## Plot the Fermi surface of Ag crystal
-------------------------------------------------------

**Steps to perform:**

1. Run the SCF calculation:

       pw.x -in 01-ag-scf.in | tee 01-ag-scf.out


2. Calculate the Fermi surface:

       fs.x -in 02-ag-fs.in | tee 02-ag-fs.out

   The result is stored in the `ag_fs.bxsf` file.


3. View the Fermi surface:

       xcrysden --bxsf ag_fs.bxsf

   Press OK. Check the `Band number: 1` and press `Selected`.


