import os

def description(name):
    basename=os.path.basename(name)
    readme=f'''
Name: {basename}
Discription:
    A information digger for NCBI.
    Search the BioSample link by NCBI Assembly accession ID and extract the sampling information from NCBI BioSample.
Usage:
    python {name} [opts] -o <output_dir>
Author: 
    yangming, yangm9@icloud.com
Version: 
    0.0.1, 2022-09-05 12:43
'''
    return readme
