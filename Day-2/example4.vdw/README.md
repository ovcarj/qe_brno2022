# PURPOSE OF THE EXERCISE: 
## Compare the vc relaxations of graphite with PBE, LDA and vdw-df-cx
-------------------------------------------------------

**Steps to perform:**

1. Take a look at the `funct.90` file to see available functionals:

       less /home/user/repo/q-e/Modules/funct.f90


2. Relax the graphite structure with the `PBE` functional:

       pw.x -in 01-graphite-pbe.in | tee 01-graphite-pbe.out


3. Relax the graphite structure with the `vdw-df-cx` functional
   by copying the `PBE` input file and defining the functional.

   Note that the `vdw-df-cx` calculation takes some time to start.
   This is because it is necessary to generate a `van der Waals kernel table`
   used by the functional.


4. Relax the graphite structure with the `LDA` functional
   by choosing the `C.pbe-rrkjus.UPF` pseudopotential.


5. Compare the relaxations with XcrySDen. 
   What are the final interlayer distances in the three cases?
   Note: the experimental interlayer distance is 3.336 A.
