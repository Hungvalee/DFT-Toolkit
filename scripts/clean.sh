#!/usr/bin/env bash

echo "Cleaning VASP output files..."

rm -f WAVECAR
rm -f CHGCAR
rm -f CHG
rm -f DOSCAR
rm -f EIGENVAL
rm -f IBZKPT
rm -f LOCPOT
rm -f ELFCAR
rm -f OUTCAR
rm -f OSZICAR
rm -f vasprun.xml
rm -f PROCAR
rm -f XDATCAR
rm -f PARCHG
rm -f PCDAT

echo "Done."
