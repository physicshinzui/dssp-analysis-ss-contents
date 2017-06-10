#!/bin/bash

gsplit -l 219 --additional-suffix=".pdb" -a 5 -d $1 snap
#gsplit -l 308 --additional-suffix=".pdb" -a 5 -d $1 snap #for single nonac CTD 
#gsplit -l 1697 --additional-suffix=".pdb" -a 5 -d $1 snap
