#!/usr/bin/env python

import subprocess
import os
import pandas as pd

#assign variables
SUMSTAT = os.environ['SUMSTAT']
OUT = os.environ['OUT']

#make directories
subprocess.call(['mkdir','/mnt/data/ss/'])

#copy data
ss_name = SUMSTAT.split('/')[-1]
ss_bgz_name = ss_name+'.bgz'
ss_gz_name = ss_name+'.gz'
subprocess.call(['gsutil','-m','cp','gs://regularized_sldsc/data/sumstats/UKBB/'+ss_bgz_name,'/mnt/data/ss/'])
subprocess.call(['mv','/mnt/data/ss/'+ss_bgz_name,'/mnt/data/ss/'+ss_gz_name])
subprocess.call(['gunzip','/mnt/data/ss/'+ss_gz_name])

#run script
df = pd.read_csv(SUMSTAT,delim_whitespace=True)
df['P_LINREG'] = pd.to_numeric(df['P_LINREG'],errors='coerce')
df.to_csv(SUMSTAT,sep='\t',index=False)

subprocess.call(['gsutil','mv','gs://regularized_sldsc/data/sumstats/UKBB/'+ss_bgz_name,'gs://regularized_sldsc/data/sumstats/UKBB/'+ss_bgz_name+'.bak'])
subprocess.call(['gzip',SUMSTAT])
subprocess.call(['mv',SUMSTAT+'.gz',SUMSTAT+'.bgz'])
subprocess.call(['gsutil','-m','cp',SUMSTAT+'.bgz','gs://regularized_sldsc/data/sumstats/UKBB/'])
