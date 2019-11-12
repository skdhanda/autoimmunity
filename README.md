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

Result file : <a href="24062_NetMHCIIpan_Nov12.xls"> 24062_NetMHCIIpan_Nov12.xls </a>

## CD4EpiScore prediction 
The immnogenicity was predicted using <a href="http://tools.iedb.org/CD4episcore/" > CD4EpiScore</a>. 
  
Result file <a href="CD4EpiScore_Nov_12_2019.csv"> CD4EpiScore_Nov_12_2019.csv</a>


## References
UniProt Database : The UniProt Consortium, 2019 PMID <a href="https://www.ncbi.nlm.nih.gov/pubmed/30395287">  30395287 </a>

CD4EpiScore : Dhanda et. al. 2018 PMID <a  href="https://www.ncbi.nlm.nih.gov/pubmed/29963059"> 29963059</a>

IEDB-AR : Dhanda et. al. 2019 PMID <a  href="https://www.ncbi.nlm.nih.gov/pubmed/29963059"> 29963059</a>

NetMHCIIpan : Jensen et. al. 2018  <a  href="https://www.ncbi.nlm.nih.gov/pubmed/29315598"> 29315598</a>
