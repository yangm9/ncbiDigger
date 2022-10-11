import os

def description(name):
    basename=os.path.basename(name)
    readme=f'''
Name: {basename}
Discription:
    A information digger for NCBI.
    1) Search the BioSample link by NCBI Assembly accession ID and extract the sampling information from NCBI BioSample.
    2) Fetch the BioProject infomation by accession ID from NCBI.
Usage:
    python {name} -i <accession_id_list> [options] -o <output_dir>
Author: 
    yangming, yangm9@icloud.com
Version: 
    0.0.1, 2022-09-05 12:43
'''
    return readme
