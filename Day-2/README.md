# Day-2 :
---------

### Topics of Day-2 hands-on session

- Structure optimization
- Phonons
- Magnetic systems
- Projection to atomic orbitals
- DFT+U (Hubbard correction)
- Van der Waals functional
- Parallel calculations

-----------

**Exercise 1:** Relax the cell and atomic positions
                of a NaCl crystal.

    cd example1.optimization
    less README.md

**Exercise 2:** Calculate the phonon frequencies
                of a NaCl crystal at gamma-point.
                Calculate the LO-TO splitting.
                Calculate the phonon dispersion and DOS.

    cd example2.phonons
    less README.md

**Exercise 3:** Perform an SCF calculation
                on a ferromagnetic Fe crystal.
                Plot the DOS projected on atomic d-orbitals.
                Perform an SCF calculation
                on an antiferromagnetic NiO crystal.
                Learn about the DFT+U (Hubbard) correction.

    cd example3.magnetism
    less README.md

**Exercise 4:** Compare cell and atomic positions
                relaxations with PBE, LDA and `vdw-df-cx`
                functionals.

    cd example4.vdw
    less README.md

**Exercise 5:** Run calculations parallelized
                over k-points and images.

    cd example5.parallelization
    less README.md
