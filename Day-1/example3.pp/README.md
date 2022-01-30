# PURPOSE OF THE EXERCISE: 
## Explore the basic usage of pp.x
-------------------------------------------------------

**Steps to perform:**

1. As in the preceding exercises, first run the SCF calculation using `pw.x`:

       pw.x -in 01-nacl-scf.in | tee 01-nacl-scf.out


2. Look at the `02-nacl-charge.in` `pp.x` input file:

       less 02-nacl-charge.in

   and try to understand the meaning of its contents using the `pp.x` documentation at
   https://www.quantum-espresso.org/Doc/INPUT_PP.html


3. Run the `pp.x` calculation:

       pp.x -in 02-nacl-charge.in | tee 02-nacl-charge.out


3. Open the obtained charge density in XcrySDen:

       xcrysden --xsf NaCl-rho.xsf

   Click Tools -> Data grid -> (press OK when prompted).
   Enter a isosurface value (e.g. 0.01) and press Submit.
