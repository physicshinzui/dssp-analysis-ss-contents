#!/usr/local/bin/python
import matplotlib.pyplot as plt
import numpy as np
import sys
import glob
import collections

class DsspReadingClass():

  def read_dssp_file(self):
    pass

  def get_amino_acid_sequence(self):
    pass
  
  def get_ss_of_each_resid(self):
    pass

list_input_dssp_file_names = glob.glob("*.dssp")

whole_list_ss = []
for ifile in list_input_dssp_file_names:
  print ""
  print "Input file name: ", ifile

  f_in = open(ifile, "r")
  for line in f_in:
    if line[2] == "#": #This is the start point of description of secondary structure type
      break

  #***begin to read ss 
  list_ss = []
  seq     = []
  for line in f_in:
    resid        = line[0:6].strip()
    resid_in_pdb = line[6:11].strip()
    segid        = line[11:13].strip()
    amino_acid   = line[13:15].strip()
    ss           = line[15:18].strip()

    if ss.strip() == "": ss = "N" ##<= if blank, then disordered.
   
    list_ss.append(ss)

    seq.append(amino_acid)

  whole_list_ss.append(list_ss)

whole_list_ss = np.array(whole_list_ss)

print ""
n_resi = len(whole_list_ss[0])
print "No of residues: ", n_resi
distrib_helix    = []
distrib_sheet    = []
distrib_others = []
for iresi in xrange(n_resi):
  counter_helix  = list(whole_list_ss[:,iresi]).count("H")  + list(whole_list_ss[:,iresi]).count("I") + list(whole_list_ss[:,iresi]).count("G")
  counter_sheet  = list(whole_list_ss[:,iresi]).count("B")  + list(whole_list_ss[:,iresi]).count("E")
  counter_others = list(whole_list_ss[:,iresi]).count("S")  + list(whole_list_ss[:,iresi]).count("T") + list(whole_list_ss[:,iresi]).count("N")

  distrib_helix.append(counter_helix)
  distrib_sheet.append(counter_sheet)
  distrib_others.append(counter_others)

#Normalize
print "Helix sum: ", np.sum(distrib_helix) 
print "Sheet sum: ", np.sum(distrib_sheet) 
print "Other sum: ", np.sum(distrib_others) 
total_sum = float(np.sum(distrib_helix) + np.sum(distrib_sheet))
#total_sum = float(np.sum(distrib_helix) + np.sum(distrib_sheet) + np.sum(distrib_others))

distrib_helix  = np.array(distrib_helix)  / total_sum
distrib_sheet  = np.array(distrib_sheet)  / total_sum
distrib_others = np.array(distrib_others) / total_sum

#check normalization
total_prob = np.sum(distrib_helix) + np.sum(distrib_sheet) 
print "Normalized correctly??(must be 1) =>", total_prob

plt.plot(distrib_helix)
plt.plot(distrib_sheet)
#plt.plot(distrib_others)

plt.xlim()
plt.ylim([0.,0.15])
plt.xticks(fontsize=20)
plt.xticks( [i for i in xrange(n_resi)], seq)
plt.yticks(fontsize=20)
plt.tick_params(width=1.5, length=5, labelleft="on", labelbottom="on")

plt.tight_layout
plt.show()
