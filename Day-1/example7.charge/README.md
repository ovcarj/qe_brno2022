# PURPOSE OF THE EXERCISE: 
## Calculate the formation energy of a LiC6 2D layer and observe charge transfer due to bond formation
-------------------------------------------------------

**Steps to perform:**

1. Take a look at the input structure:

       xcrysden --pwi 01-lic6-scf.in

   Notice the very long cell Z-axis. 
   You can increase the number of units drawn by pressing Modify -> Number of Units Drawn.


2. Execute the LiC6 SCF calculation:

       pw.x -in 01-lic6-scf.in | tee 01-lic6-scf.out


3. Get the LiC6 ground state charge density:

       pp.x -in 02-lic6-charge.in | tee 02-lic6-charge.out


4. Repeat Steps 2 and 3 for pure Li and C6 structures.
   E.g., for Li, you can make the SCF and PP files by

       cp 01-lic6-scf.in 01-li-scf.in
       cp 02-lic6-charge.in 02-li-charge.in

   Appropriately edit `prefix`, `nat`, `ntyp`, `filplot` and remove references to C atoms.
   You can leave the Li positions as specified in the LiC6 structure.
   Repeat this for C6.


5. Extract the total energy from the SCF outputs, e.g. for LiC6:

       grep "!" 01-lic6-scf.out

   and calculate the formation (adsorption) energy as defined in the slides.


6. Read the contents of the `pp.x` input file `03-lic6-chdiff.in`:

       less 03-lic6-chdiff.in

   and try to understand them
   using the `pp.x` documentation.


7. Calculate the charge transfer:

       pp.x -in 03-lic6-chdiff.in | tee 03-lic6-chdiff.out

   The result is written in the `LiC6-charge_DIFF.xsf` file.


8. View the charge transfer:

       xcrysden --xsf LiC6-charge_DIFF.xsf

   For a nicer plot, you can first repeat the structure, e.g., 3 units
   in the X- and Y- axes directions. Then click Tools -> Data Grid,
   enter some isosurface value (e.g. 0.0025), check Render +/- isovalue,
   expand the isosurface to the whole structure and Submit.


