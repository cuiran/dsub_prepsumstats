#!/usr/bin/env python

import subprocess
import os

#assign variables
SUMSTAT = os.environ['SUMSTAT']
N = os.environ['N']
OUT = os.environ['OUT']
PATH = '/home/ldsc/' #default ldsc path

#make directories
subprocess.call(['mkdir','/mnt/data/ss/'])
subprocess.call(['mkdir','/mnt/data/result/'])

#copy data
ss_name = SUMSTAT.split('/')[-1]
ss_bgz_name = ss_name+'.bgz'
ss_gz_name = ss_name+'.gz'
subprocess.call(['gsutil','-m','cp','gs://regularized_sldsc/data/sumstats/UKBB/'+ss_bgz_name,'/mnt/data/ss/'])
subprocess.call(['mv','/mnt/data/ss/'+ss_bgz_name,'/mnt/data/ss/'+ss_gz_name])
subprocess.call(['gunzip','/mnt/data/ss/'+ss_gz_name])

#run script
if 'BOLT' in SUMSTAT:
    tag = '--bolt'
elif 'SAIGE' in SUMSTAT:
    tag = '--saige'
subprocess.call(['python','/home/prep-sumstats/format_sumstats.py',
    tag,
    '--ss-fname',SUMSTAT,
    '--N',N,
    '--output-prefix',OUT,
    '--path-to-ldsc',PATH])

subprocess.call(['gsutil','-m','cp','/mnt/data/result/*','gs://regularized_sldsc/data/sumstats_formatted_v092019/'])
