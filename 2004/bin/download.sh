#!/bin/bash

FILES=(
    'http://fbarc.stadt-berlin.de/FIS_Broker_Atom/DOP/dop25c_2004/Mitte.zip'
    'http://fbarc.stadt-berlin.de/FIS_Broker_Atom/DOP/dop25c_2004/Nord.zip'
    'http://fbarc.stadt-berlin.de/FIS_Broker_Atom/DOP/dop25c_2004/Nordost.zip'
    'http://fbarc.stadt-berlin.de/FIS_Broker_Atom/DOP/dop25c_2004/Nordwest.zip'
    'http://fbarc.stadt-berlin.de/FIS_Broker_Atom/DOP/dop25c_2004/Ost.zip'
    'http://fbarc.stadt-berlin.de/FIS_Broker_Atom/DOP/dop25c_2004/Sued.zip'
    'http://fbarc.stadt-berlin.de/FIS_Broker_Atom/DOP/dop25c_2004/Suedost.zip'
    'http://fbarc.stadt-berlin.de/FIS_Broker_Atom/DOP/dop25c_2004/Suedwest.zip'
    'http://fbarc.stadt-berlin.de/FIS_Broker_Atom/DOP/dop25c_2004/West.zip'
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

