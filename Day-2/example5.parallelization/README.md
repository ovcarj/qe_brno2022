# PURPOSE OF THE EXERCISE: 
## Run parallel calculations
-------------------------------------------------------

**Steps to perform:**

1. Run `pw.x` parallelizing over k-points:

       mpirun -np 2 pw.x -nk 2 -i 01-feo-scf.in > 01-feo-scf.out

   You can follow the calculation in real time in an 
   another terminal using:

       tail -f 01-feo-scf.out


2. Compare the total calculation timing with the results
   of `../example2.magnetism/ex3.feo`

   Note: a nice command to open two files is:

       diff -y file1 file2 | less


3. Run the NaCl SCF calculation necessary
   for the phonon calculation:

       mpirun -np 2 pw.x -nk 2 -i 02-nacl-scf.in > 02-nacl-scf.out


4. Parallelize the phonon calculation over 
   images (irreducible modes):

       mpirun -np 2 ph.x -ni 2 -i 03-nacl-ph-epsil.in > 03-nacl-ph-epsil.out


