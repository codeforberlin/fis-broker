#!/bin/bash

FILES=(
    'http://fbarc.stadt-berlin.de/FIS_Broker_Atom/DOP/dop20rgb_2019/Mitte.zip'
    'http://fbarc.stadt-berlin.de/FIS_Broker_Atom/DOP/dop20rgb_2019/Nord.zip'
    'http://fbarc.stadt-berlin.de/FIS_Broker_Atom/DOP/dop20rgb_2019/Nordost.zip'
    'http://fbarc.stadt-berlin.de/FIS_Broker_Atom/DOP/dop20rgb_2019/Nordwest.zip'
    'http://fbarc.stadt-berlin.de/FIS_Broker_Atom/DOP/dop20rgb_2019/Ost.zip'
    'http://fbarc.stadt-berlin.de/FIS_Broker_Atom/DOP/dop20rgb_2019/Sued.zip'
    'http://fbarc.stadt-berlin.de/FIS_Broker_Atom/DOP/dop20rgb_2019/Suedost.zip'
    'http://fbarc.stadt-berlin.de/FIS_Broker_Atom/DOP/dop20rgb_2019/Suedwest.zip'
    'http://fbarc.stadt-berlin.de/FIS_Broker_Atom/DOP/dop20rgb_2019/West.zip'
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
