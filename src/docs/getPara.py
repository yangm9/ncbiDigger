import sys
from . import readme
from optparse import OptionParser

usage=readme.description(sys.argv[0])

def optionSet():
    parser=OptionParser(usage)
    parser.add_option(
        '-i','--acce_list',action='store',type='str',
        dest='acce_file',metavar='FILE',default='',
        help='NCBI登记编号(accession ID)列表文件，目前仅限于Assembly和Project编号。'
    )
    parser.add_option(
        '-t','--acce_type',action='store',type='str',
        dest='acce_type',metavar='STR',default='Assembly',
        help='NCBI登记编号(accession ID)类型，目前可选参数为"Assembly"和"Project"。'
    )
    parser.add_option(
        '-o','--output_dir',action='store',type='str',
        dest='output_dir',metavar='DIR',default='',
        help='输出目录，默认为当前目录。'
    )
    return parser.parse_args()
