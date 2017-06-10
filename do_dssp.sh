#!/bin/bash

list_of_pdbs=`ls -v snap*.pdb`
#echo $list_of_pdbs

for isnap in $list_of_pdbs; do
  echo -ne "$isnap"\\r
  mkdssp -i $isnap -o ${isnap%.pdb}.dssp
done
