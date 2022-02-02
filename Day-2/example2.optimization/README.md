# PURPOSE OF THE EXERCISE: 
## Optimize the structure of a NaCl crystal
-------------------------------------------------------

**Steps to perform:**

1. Check the contents of the `pw.x` input file:

       less nacl-vc_relax.in

   and see how it differs from an input file for a 
   single SCF calculation.


2. Run the structure optimization:

       pw.x -in nacl-vc_relax.in | tee nacl-vc_relax.out


3. See how the total energy is lowered during the optimization:

       grep "!" nacl-vc_relax.out


4. Get the optimized atomic positions:

       grep -A2 "ATOMIC" nacl-vc_relax.out | tail -3

   They should be the same as the starting positions.


5. Get the optimized cell parameters:

       grep -A3 "CELL" nacl-vc_relax.out | tail -4


6. See how the optimization proceeded with XcrySDen:

       xcrysden --pwo nacl-vc_relax.out

   To see the whole optimization, select the 
   `Display all Coordinates as Animation` option.


