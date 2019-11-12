#!/usr/bin/python

from Bio import ExPASy
from Bio import SeqIO
import subprocess, os

def fetchUniprot(accessions,file_path):
    uni_id=[]
    for accession in accessions:
       try:
         handle = ExPASy.get_sprot_raw(accession)
         record=SeqIO.read(handle,"swiss")
         if record.id not in uni_id: 
           uni_id.append(record.id)
         else:
            print("duplicate record found", str(accession))
       except:
         print("WARNING: Accession %s not found" % accession)
    all_record='+OR+'.join(uni_id)
    url='https://www.uniprot.org/uniprot/?query=\"'+all_record+'&format=fasta\"'
    cmd='curl -o ' + file_path + ' ' + url
    try: 
      subprocess.call(cmd,shell=True)
    except:
      print("File could not be downloaded")
    
accessions=['P21980','Q99259','P01308','Q05084','Q8IWU4','P18573','P07202']
fetchUniprot(accessions,"sequence.fasta")
