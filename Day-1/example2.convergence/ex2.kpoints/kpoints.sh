#!/bin/sh
# reminder: from now on, what follows the character # is a comment

# cleanup if previous data exists
rm -rf *in *out *save *dat *png calculation_files

# loop over k-point values
for kpoint in 1 3 5 7
do
    echo "Running for k-point grid = $kpoint x $kpoint x $kpoint ..."

    # self-consistent calculation
    cat > nacl-scf_${kpoint}.in << EOF

 &CONTROL
    calculation = 'scf',
    restart_mode ='from_scratch',
    prefix = 'nacl_${kpoint}',
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
    ecutwfc = 40,
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
    ${kpoint} ${kpoint} ${kpoint} 0 0 0
EOF

    # run the pw.x calculation
    pw.x -in nacl-scf_${kpoint}.in > nacl-scf_${kpoint}.out

    # write the k-point grid value and collect the total energy from the pw.x output file
    
    energy=$(grep '!' nacl-scf_${kpoint}.out | awk '{print $5}')
    echo | awk -v k=$kpoint -v e=$energy '{print k, e}' >> nacl-etot_vs_kpoint.dat

done

# move files to an output directory so the main directory isn't cluttered

mkdir calculation_files

mv -t calculation_files *in *out *save *xml
