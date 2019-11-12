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

