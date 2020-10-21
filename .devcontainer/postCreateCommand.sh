#!/bin/bash

## Prepare Python venv for Pulumi
python -m venv ./venv
./venv/bin/python -m pip install -r ./requirements.txt

# Finalize
uname -a
