#!/bin/sh
# reminder: from now on, what follows the character # is a comment

# cleanup if previous data exists
rm -rf *in *out *save *dat *png calculation_files

# loop over ecutwfc value
for ecut in 15 20 25 30 35 40 45
do
    echo "Running for ecutwfc = $ecut ..."

    # self-consistent calculation
    cat > nacl-scf_${ecut}.in << EOF

 &CONTROL
    calculation = 'scf',
    restart_mode ='from_scratch',
    prefix = 'nacl_${ecut}',
    outdir = './',
    tstress = .true.,
    tprnfor = .true.,
    verbosity = 'high',
 /

 &SYSTEM
    ibrav =  2,
    celldm(1) = 10.571,
    nat =  2,
    ntyp = 2,
    nbnd = 10,
    ecutwfc = $ecut,
    ecutrho = 600,
 /

 &ELECTRONS
    mixing_beta = 0.7,
    conv_thr = 1.0d-10,
 /

 ATOMIC_SPECIES
    Na  22.9898   na_pbe_v1.5.uspp.F.UPF
    Cl  35.453    cl_pbe_v1.4.uspp.F.UPF

 ATOMIC_POSITIONS {crystal}
    Na 0.00 0.00 0.00
    Cl 0.50 0.50 0.50

 K_POINTS {automatic}
    5 5 5 0 0 0
EOF

    # run the pw.x calculation
    pw.x -in nacl-scf_${ecut}.in > nacl-scf_${ecut}.out

    # collect the ecutwfc and total energy from the pw.x output file
    
    grep -e 'kinetic-energy cutoff' -e ! nacl-scf_${ecut}.out | \
        awk '/kinetic-energy/ {ecut=$(NF-1)}
             /!/              {print ecut, $(NF-1)}' >> nacl-etot_vs_ecut.dat

done

# move files to an output directory so the main directory isn't cluttered

mkdir calculation_files

mv -t calculation_files *in *out *save *xml
