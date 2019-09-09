#!/bin/bash

docker build --no-cache -t prep-sumstats .
docker tag prep-sumstats gcr.io/finucane-dp5/prep-sumstats:latest
docker push gcr.io/finucane-dp5/prep-sumstats:latest
