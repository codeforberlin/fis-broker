#!/bin/bash

FILES=(
    'http://fbarc.stadt-berlin.de/FIS_Broker_Atom/DOP/1928/mitte.zip'
    'http://fbarc.stadt-berlin.de/FIS_Broker_Atom/DOP/1928/nord.zip'
    'http://fbarc.stadt-berlin.de/FIS_Broker_Atom/DOP/1928/nordost.zip'
    'http://fbarc.stadt-berlin.de/FIS_Broker_Atom/DOP/1928/nordwest.zip'
    'http://fbarc.stadt-berlin.de/FIS_Broker_Atom/DOP/1928/ost.zip'
    'http://fbarc.stadt-berlin.de/FIS_Broker_Atom/DOP/1928/sued.zip'
    'http://fbarc.stadt-berlin.de/FIS_Broker_Atom/DOP/1928/suedost.zip'
    'http://fbarc.stadt-berlin.de/FIS_Broker_Atom/DOP/1928/suedwest.zip'
    'http://fbarc.stadt-berlin.de/FIS_Broker_Atom/DOP/1928/west.zip'
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
