#!/usr/bin/env python3
import os
from src.docs import getPara
from src.parasite import expoResu

def main():
    opts,args=getPara.optionSet() #接收外部参数
    if not os.path.exists(opts.output_dir): os.makedirs(opts.output_dir)
    expoResu.outputInfo(opts)
    return 0

if __name__=='__main__': main()

