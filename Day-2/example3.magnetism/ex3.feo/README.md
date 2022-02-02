# PURPOSE OF THE EXERCISE:
## Obtaining the insulating state of FeO using DFT and DFT+U
------------------------------------------------------------------------------------

**Disclaimer**

This exercise is adapted from 
https://gitlab.com/QEF/material-for-ljubljana-qe-summer-school/-/tree/master/Day-2/example4.functionals/ex1.DFT%2BU

**Steps to perform:**

1. Standard DFT (no Hubbard correction) calculation:

       pw.x -in 01-feo-scf.in | tee 01-feo-scf.out
       pw.x -in 02-feo-nscf.in | tee 02-feo-nscf.out
       mkdir PDOS
       projwfc.x -in 03-feo-projwfc.in | tee 03-feo-projwfc.out
       python plot_pdos.py no_correction

   The obtained system is a metal.


2. DFT+U calculation:

       pw.x -in 01-feo_hub-scf.in | tee 01-feo_hub-scf.out
       pw.x -in 02-feo_hub-nscf.in | tee 02-feo_hub-nscf.out
       projwfc.x -in 03-feo_hub-projwfc.in | tee 03-feo_hub-projwfc.out
       python plot_pdos.py hubbard

   The obtained system is an insulator.
