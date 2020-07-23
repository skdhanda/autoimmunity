# autoimmunity
Autoimmunity project in collaborations with Navchetan, UCSF, California, USA. 

## Fetching of sequences 
The sequences were fetched using the sequence retrival code <a href="fetchUniport.py">fetchUniport.py</a> from the accession list provided by Navchetan. 

## Setting up alleles 

### Name of alleles

```console
  
HLA-DRB1*03:01
HLA-DRB3*01:07
HLA-DQA1*01:01/HLA-DQB1*02:01	
HLA-DQA1*01:01/HLA-DQB1*03:02
HLA-DRB1*04:01
```

### Retrieve HLA sequence 
There was an additional alleles, for which we have to download the sequence from IMGT/HLA to run predictions using NETMHCIIpan, using the following url <a href="https://www.ebi.ac.uk/cgi-bin/ipd/imgt/hla/get_allele.cgi?DRB3*01:07"> https://www.ebi.ac.uk/cgi-bin/ipd/imgt/hla/get_allele.cgi?DRB3*01:07</a>

The protein sequence for this allele was stored to run predictions. 

## NetMHCIIpan predictions
The binding affinities for the peptides in the provided sequences were predicted using <a href="http://www.cbs.dtu.dk/services/NetMHCIIpan/"> NetMHCIIpan version 3.2 </a> using default parameters. 

Result file : <a href="updated_data/31785_NetMHCIIpan_5_Allelels.xls">updated_data/31785_NetMHCIIpan_5_Allelels.xls </a>

## CD4EpiScore prediction 
The immnogenicity was predicted using <a href="http://tools.iedb.org/CD4episcore/" > CD4EpiScore</a>. 
  
Result file <a href="updated/CD4_episcore_results.csv">CD4_episcore_results.csv</a>

## Clustering results
The clustering was performed on the selected predicted binders (based on their IC50 <=1000nm). The fasta file was generated for these binders can be found in  <a href="updated_data/31785_NetMHCIIpan_5_Allelels.xls">updated_data/31785_NetMHCIIpan_5_Allelels.xls </a>. 

Clustering was performed using using <a href="http://tools.iedb.org/cluster/" > Clustering tool</a>.

Result file:  <a href="updated_data/clustering_results.csv">updated_data/clustering_results.csv </a>

The peptides across different proteins were then manually selected, if the peptides were grouped together.
 
## References
UniProt Database : The UniProt Consortium, 2019 PMID <a href="https://www.ncbi.nlm.nih.gov/pubmed/30395287">  30395287 </a>

CD4EpiScore : Dhanda et. al. 2018 PMID <a  href="https://www.ncbi.nlm.nih.gov/pubmed/29963059"> 29963059</a>

IEDB-AR : Dhanda et. al. 2019 PMID <a  href="https://www.ncbi.nlm.nih.gov/pubmed/29963059"> 29963059</a>

NetMHCIIpan : Jensen et. al. 2018  <a  href="https://www.ncbi.nlm.nih.gov/pubmed/29315598"> 29315598</a>

Clustering: Dhanda et. al. 2018 <a href="https://pubmed.ncbi.nlm.nih.gov/30014462/"> 30014462</a>
