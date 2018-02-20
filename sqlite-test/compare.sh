#!/bin/bash

python unqtest.py > temp && meld temp sampleB64.txt
