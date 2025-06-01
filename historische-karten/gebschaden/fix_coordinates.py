#!/usr/bin/env python
# coding=utf-8
from subprocess import check_call
from pathlib import Path

# height and width from gdalinfo
w = '3898'
h = '3874'

tif_files = (
    ('Gebudeschden_1945_gekachelt 01.tif', 'gebschaden_01.tif', '15200', '21720', '18500', '25000'),
    ('Gebudeschden_1945_gekachelt 02.tif', 'gebschaden_02.tif', '18500', '21720', '21800', '25000'),
    ('Gebudeschden_1945_gekachelt 03.tif', 'gebschaden_03.tif', '21800', '21720', '25100', '25000'),
    ('Gebudeschden_1945_gekachelt 04.tif', 'gebschaden_04.tif', '25100', '21720', '28400', '25000'),
    ('Gebudeschden_1945_gekachelt 05.tif', 'gebschaden_05.tif', '15200', '18440', '18500', '21720'),
    ('Gebudeschden_1945_gekachelt 06.tif', 'gebschaden_06.tif', '18500', '18440', '21800', '21720'),
    ('Gebudeschden_1945_gekachelt 07.tif', 'gebschaden_07.tif', '21800', '18440', '25100', '21720'),
    ('Gebudeschden_1945_gekachelt 08.tif', 'gebschaden_08.tif', '25100', '18440', '28400', '21720'),
    ('Gebudeschden_1945_gekachelt 09.tif', 'gebschaden_09.tif', '15200', '15160', '18500', '18440'),
    ('Gebudeschden_1945_gekachelt 10.tif', 'gebschaden_10.tif', '18500', '15160', '21800', '18440'),
    ('Gebudeschden_1945_gekachelt 11.tif', 'gebschaden_11.tif', '21800', '15160', '25100', '18440'),
    ('Gebudeschden_1945_gekachelt 12.tif', 'gebschaden_12.tif', '25100', '15160', '28400', '18440'),
)

for tif_file, cog_file, x_bottom_left, y_bottom_left, x_top_right, y_top_right in tif_files:
    input_path = Path('tif') / tif_file
    output_path = Path('fixed') / cog_file

    cmd = f'''
    gdal_translate "{input_path}" "{output_path}"
        -of COG -a_srs EPSG:3068 -expand rgb
        -co COMPRESS=JPEG -co QUALITY=75 -co BLOCKSIZE=512
        -co OVERVIEWS=IGNORE_EXISTING
        -gcp 0   0   {x_bottom_left} {y_top_right}
        -gcp 0   {h} {x_bottom_left} {y_bottom_left}
        -gcp {w} 0   {x_top_right}   {y_top_right}
        -gcp {w} {h} {x_top_right}   {y_bottom_left}
    '''.strip().replace('\n', ' ')

    check_call(cmd, shell=True)
