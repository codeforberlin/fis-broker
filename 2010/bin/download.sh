#!/bin/bash

FILES=(
    'http://fbarc.stadt-berlin.de/FIS_Broker_Atom/DOP/dop20c_2010/Mitte.zip'
    'http://fbarc.stadt-berlin.de/FIS_Broker_Atom/DOP/dop20c_2010/Nord.zip'
    'http://fbarc.stadt-berlin.de/FIS_Broker_Atom/DOP/dop20c_2010/Nordost.zip'
    'http://fbarc.stadt-berlin.de/FIS_Broker_Atom/DOP/dop20c_2010/Nordwest.zip'
    'http://fbarc.stadt-berlin.de/FIS_Broker_Atom/DOP/dop20c_2010/Ost.zip'
    'http://fbarc.stadt-berlin.de/FIS_Broker_Atom/DOP/dop20c_2010/Sued.zip'
    'http://fbarc.stadt-berlin.de/FIS_Broker_Atom/DOP/dop20c_2010/Suedost.zip'
    'http://fbarc.stadt-berlin.de/FIS_Broker_Atom/DOP/dop20c_2010/Suedwest.zip'
    'http://fbarc.stadt-berlin.de/FIS_Broker_Atom/DOP/dop20c_2010/West.zip'
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

