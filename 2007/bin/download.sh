#!/bin/bash

FILES=(
    'http://fbarc.stadt-berlin.de/FIS_Broker_Atom/DOP/dop20c_2007/Mitte.zip'
    'http://fbarc.stadt-berlin.de/FIS_Broker_Atom/DOP/dop20c_2007/Nord.zip'
    'http://fbarc.stadt-berlin.de/FIS_Broker_Atom/DOP/dop20c_2007/Nordost.zip'
    'http://fbarc.stadt-berlin.de/FIS_Broker_Atom/DOP/dop20c_2007/Nordwest.zip'
    'http://fbarc.stadt-berlin.de/FIS_Broker_Atom/DOP/dop20c_2007/Ost.zip'
    'http://fbarc.stadt-berlin.de/FIS_Broker_Atom/DOP/dop20c_2007/Sued.zip'
    'http://fbarc.stadt-berlin.de/FIS_Broker_Atom/DOP/dop20c_2007/Suedost.zip'
    'http://fbarc.stadt-berlin.de/FIS_Broker_Atom/DOP/dop20c_2007/Suedwest.zip'
    'http://fbarc.stadt-berlin.de/FIS_Broker_Atom/DOP/dop20c_2007/West.zip'
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

