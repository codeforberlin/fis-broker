#!/bin/bash

FILES=(
    'https://fbinter.stadt-berlin.de/fb/atom/DOP/dop20rgb_2021/Mitte.zip',
    'https://fbinter.stadt-berlin.de/fb/atom/DOP/dop20rgb_2021/Nord.zip',
    'https://fbinter.stadt-berlin.de/fb/atom/DOP/dop20rgb_2021/Nordost.zip',
    'https://fbinter.stadt-berlin.de/fb/atom/DOP/dop20rgb_2021/Nordwest.zip',
    'https://fbinter.stadt-berlin.de/fb/atom/DOP/dop20rgb_2021/Ost.zip',
    'https://fbinter.stadt-berlin.de/fb/atom/DOP/dop20rgb_2021/Sued.zip',
    'https://fbinter.stadt-berlin.de/fb/atom/DOP/dop20rgb_2021/Suedost.zip',
    'https://fbinter.stadt-berlin.de/fb/atom/DOP/dop20rgb_2021/Suedwest.zip',
    'https://fbinter.stadt-berlin.de/fb/atom/DOP/dop20rgb_2021/West.zip'
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
