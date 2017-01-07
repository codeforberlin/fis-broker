#!/bin/bash

mkdir images
cd images
for f in ../zip/*.zip
    do unzip $f
done
cd ..
