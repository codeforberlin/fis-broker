#!/bin/bash

FILES=(
    'http://fbarc.stadt-berlin.de/FIS_Broker_Atom/Berlin_um/Berlin1650.zip'
)

mkdir zip
cd zip
for f in ${FILES[@]}
    do wget $f
done
cd ..

mkdir images
cd images
for f in ../zip/*.zip
    do unzip $f
done
cd ..
