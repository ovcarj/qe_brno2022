# PURPOSE OF THE EXERCISE:
## Convergence test for the k-point grid density via a Unix shell-script
--------------------------------------------------------------------------------

**Steps to perform:**

1. Read the `kpoints.sh` script and try to understand it.


2. To run the pw.x with various values of the k-point grid density, execute:

       ./kpoints.sh
   

   The total energy and k-point grid parameters are saved to `nacl-etot_vs_kpoint.dat`.
   Note that the input and output calculation files are moved to the 
   directory `calculation_files`.


3. Plot the dependence of energy on ecutwfc using a Python script:

       python plot.py nacl-etot_vs_kpoint.dat
       

4. The plot is saved to `kpoint_vs_energy.png`. You can open .png files with

       eog kpoint_vs_energy.png

