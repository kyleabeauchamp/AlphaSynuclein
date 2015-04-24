"""
pdb2gmx -ff amber99sb-ildn -f ../pdb/resi-1-15.pdb  -ignh -water tip3p -vsite hydrogens
editconf -f conf.gro -o conf.gro -bt cubic -c -d 0.8
genbox -cp conf.gro -cs spc216.gro -o conf.gro -p topol.top
"""
