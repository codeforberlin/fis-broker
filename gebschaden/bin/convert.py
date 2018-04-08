#!/usr/bin/env python
# coding=utf-8
import os

# height and width from gdalinfo
w = '3898'
h = '3874'

tif_files = (
    ('images/Gebudeschden_1945_gekachelt\ 01.tif', '15200', '21720', '18500', '25000'),
    ('images/Gebudeschden_1945_gekachelt\ 02.tif', '18500', '21720', '21800', '25000'),
    ('images/Gebudeschden_1945_gekachelt\ 03.tif', '21800', '21720', '25100', '25000'),
    ('images/Gebudeschden_1945_gekachelt\ 04.tif', '25100', '21720', '28400', '25000'),
    ('images/Gebudeschden_1945_gekachelt\ 05.tif', '15200', '18440', '18500', '21720'),
    ('images/Gebudeschden_1945_gekachelt\ 06.tif', '18500', '18440', '21800', '21720'),
    ('images/Gebudeschden_1945_gekachelt\ 07.tif', '21800', '18440', '25100', '21720'),
    ('images/Gebudeschden_1945_gekachelt\ 08.tif', '25100', '18440', '28400', '21720'),
    ('images/Gebudeschden_1945_gekachelt\ 09.tif', '15200', '15160', '18500', '18440'),
    ('images/Gebudeschden_1945_gekachelt\ 10.tif', '18500', '15160', '21800', '18440'),
    ('images/Gebudeschden_1945_gekachelt\ 11.tif', '21800', '15160', '25100', '18440'),
    ('images/Gebudeschden_1945_gekachelt\ 12.tif', '25100', '15160', '28400', '18440'),
)

for tif_file, x_bottom_left, y_bottom_left, x_top_right, y_top_right  in tif_files:
    cmd = 'gdal_translate -of GTiff -a_srs EPSG:3068 -expand rgb'
    cmd += ' -gcp 0  0  %s %s' % (x_bottom_left, y_top_right)
    cmd += ' -gcp 0  %s %s %s' % (h, x_bottom_left, y_bottom_left)
    cmd += ' -gcp %s 0  %s %s' % (w, x_top_right, y_top_right)
    cmd += ' -gcp %s %s %s %s' % (w, h, x_top_right, y_bottom_left)
    cmd += ' %s %s' % (tif_file, tif_file + '.tmp.tif')

    os.system(cmd)

    cmd = 'gdalwarp -overwrite -s_srs EPSG:3068 -t_srs EPSG:3068 -r bilinear -srcnodata 0 -dstalpha %s %s' % (tif_file + '.tmp.tif', tif_file + '.gdal.tif')

    os.system(cmd)

cmd = 'gdalbuildvrt -a_srs EPSG:3068 -overwrite tiles.vrt images/*.gdal.tif'
os.system(cmd)
