#!/bin/bash

dsub \
    --provider google-v2 \
    --project finucane-dp5 \
    --zones "us-east1-b" \
    --disk-size 100 \
    --logging gs://regularized_sldsc/logging/format_ss_bolt/ \
    --machine-type n1-standard-2 \
    --image "gcr.io/finucane-dp5/prep-sumstats:latest" \
    --script "run_format_ss.py" \
    --task "submit_sample.tsv"
