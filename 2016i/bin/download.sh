#!/bin/bash

FILES=(
    'http://fbarc.stadt-berlin.de/FIS_Broker_Atom/DOP/dop20cir_2016/Mitte.zip'
    'http://fbarc.stadt-berlin.de/FIS_Broker_Atom/DOP/dop20cir_2016/Nord.zip'
    'http://fbarc.stadt-berlin.de/FIS_Broker_Atom/DOP/dop20cir_2016/Nordost.zip'
    'http://fbarc.stadt-berlin.de/FIS_Broker_Atom/DOP/dop20cir_2016/Nordwest.zip'
    'http://fbarc.stadt-berlin.de/FIS_Broker_Atom/DOP/dop20cir_2016/Ost.zip'
    'http://fbarc.stadt-berlin.de/FIS_Broker_Atom/DOP/dop20cir_2016/Sued.zip'
    'http://fbarc.stadt-berlin.de/FIS_Broker_Atom/DOP/dop20cir_2016/Suedost.zip'
    'http://fbarc.stadt-berlin.de/FIS_Broker_Atom/DOP/dop20cir_2016/Suedwest.zip'
    'http://fbarc.stadt-berlin.de/FIS_Broker_Atom/DOP/dop20cir_2016/West.zip'
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

