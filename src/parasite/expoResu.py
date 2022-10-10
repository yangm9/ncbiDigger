#!/usr/bin/env python3
import os
import sys
import copy
from ..configs import setConst
from ..getData import fetchInfo

def outputInfo(opts):
    """
    将字典输出到数据表中。
    """
    acce_type_s=opts.acce_type
    InfoDict=setConst.InfoDict
    acce_info_f=f'{opts.output_dir}/{acce_type_s}_info.xls'
    if os.path.isfile(acce_info_f): os.remove(acce_info_f)
    ASSELIST=open(opts.acce_file)
    INFO=open(acce_info_f,'w')
    INFOHEAD='\t'.join(InfoDict[acce_type_s])
    INFO.write(f'accession_id\t{INFOHEAD}\n')
    for accession in ASSELIST:
        accession=accession.strip()
        print(f'Processing {accession}')
        TabDict={}
        TabDict=fetchInfo.MethDict[acce_type_s](accession)
        INFO.write(accession)
        ITEMS=InfoDict[acce_type_s]
        for j in range(len(ITEMS)):
            INFO.write('\t'+str(TabDict[ITEMS[j]]))
        INFO.write('\n')
    INFO.close()
    return 0

if __name__=='__main__':
    if len(sys.argv)>1:
        outputInfo(sys.argv[1],sys.argv[2],sys.argv[3])
    else:
        print(f'''
Description:
    Search the BioSample link by NCBI Assembly accession ID and extract the sampling information from NCBI BioSample.

Usage: 
    {sys.argv[0]} -i <accession_list> [-t <accession_type>] -o <out_dir>
        -i <accession_list>: NCBI assembly accession list file, i.e., GCA_013202315.1\\nGCA_013202525.1\\n 
        -t <accession_type>: Accession ID type, i.e., Assembly, Project
        -o <out_dir>: output directory
''')
