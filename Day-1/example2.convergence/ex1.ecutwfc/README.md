# PURPOSE OF THE EXERCISE:
## Convergence test for cutoff energy (ecutwfc) via a Unix shell-script
--------------------------------------------------------------------------------

**Steps to perform:**

1. Read the `ecutwfc.sh` script and try to understand it.


2. To run the pw.x with various values of the ecutwfc parameter, execute:

       ./ecutwfc.sh
   

   The total energy and ecutwfc parameters are saved to `nacl-etot_vs_ecut.dat`.
   Note that the input and output calculation files are moved to the 
   directory `calculation_files`.


3. Plot the dependence of energy on ecutwfc using a Python script:

       python plot.py nacl-etot_vs_ecut.dat
       

4. The plot is saved to `ecut_vs_energy.png`. You can open .png files with

       eog ecut_vs_energy.png

