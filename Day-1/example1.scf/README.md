# PURPOSE OF THE EXERCISE: 
## Perform and understand a basic SCF calculation 
-------------------------------------------------------

**Steps to perform:**

1. Read the contents of the `nacl-scf.in` file:

       less nacl-scf.in

   Try to understand the meaning of its contents using the slides
   and the documentation webpage:
   https://www.quantum-espresso.org/Doc/INPUT_PW.html


2. View the crystal structure in the `nacl-scf.in` file:

       xcrysden --pwi nacl-scf.in

   Press OK when prompted.


3. Run the SCF calculation using `pw.x`:

       pw.x -in nacl-scf.in | tee nacl-scf.out

   If you don't want the output to be written on the screen during
   the calculation, you can run the calculation by:

       pw.x -in nacl-scf.in > nacl-scf.out


4. Read the `nacl-scf.out` output file, showing the line numbers:

       less -N nacl-scf.out

   and try to understand the meaning of its contents using the slides.


5. See how the SCF calculation accuracy converges along with the energy:

       grep -B1 "estimated scf accuracy" nacl-scf.out


