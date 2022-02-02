# PURPOSE OF THE EXERCISE: 
## Compare the vc relaxations of graphite with PBE and vdw-df-cx
-------------------------------------------------------

**Steps to perform:**

1. Take a look at the `funct.90` file to see available functionals:

       less /home/user/repo/q-e/Modules/funct.f90


2. Relax the graphite structure with the `PBE` (default) functional:

       pw.x -in 01-graphite-pbe.in | tee 01-graphite-pbe.out


3. Relax the graphite structure with the `vdw-df-cx` functional
   by copying the `PBE` input file and defining the functional.

   Note that the `vdw-df-cx` calculation takes some time to start.
   This is because it is necessary to generate a `van der Waals kernel table`
   used by the functional.


4. Compare the two relaxations with XcrySDen. 
   What are the final interlayer distances in the two cases?
