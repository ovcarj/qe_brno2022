# PURPOSE OF THE EXERCISE: 
## Plot the band structure of Ag crystal
-------------------------------------------------------

**Steps to perform:**

1. The first step is again the SCF calculation:

       pw.x -in 01-ag-scf.in | tee 01-ag-scf.out

   Of course, in reality, we would use the results already 
   obtained in Exercise 4.


2. The next step is to define the k-path with XcrySDen. 
   Open the SCF input file:

       xcrysden --pwi 01-ag-scf.in

   Click on Tools -> k-path Selection. 
   Select the path: `W-L-GAMMA-X-W-K` and press OK.
   Note that you can remove a selected point by clicking on it again. 


3. Set `Total number of k-points along the path` to 100. Press OK.


4. Set `File name` to `Ag-kpath.pwscf`, choose the `*.pwscf` file type and Save.


5. Paste the contents of `Ag-kpath.pwscf` to the end of `02-ag-nscf_bands.in`.


6. Run the NSCF calculation along the selected k-path:

       pw.x -in 02-ag-nscf_bands.in | tee 02-ag-nscf_bands.out


7. Extract the band structure from the NSCF calculation using `bands.x`

       bands.x -in 03-ag-pp_bands.in | tee 03-ag-pp_bands.out


8. Plot the Ag band structure:

       python plot_bands.py -dat Ag-bands.dat -ef 16.4458 -img

   Note that the Fermi energy is written in `01-ag-scf.out`

       grep "Fermi" 01-ag-scf.out


9. Let's also simultaneously plot the band structure and DOS we
   calculated in the last exercise:

       cp reference/Ag-dos.dat .
       python plot_bands_dos.py -dat Ag-bands.dat -dos Ag-dos.dat -ef 16.4458 -img

