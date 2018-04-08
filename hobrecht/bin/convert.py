#!/usr/bin/env python
# coding=utf-8
import os

# height and width from gdalinfo
w = '3375'
h = '3103'

tif_files = (
    ('images/Hobrecht-Plan_1862_gekachelt01.tif', '16920', '22360', '19790', '25000'),
    ('images/Hobrecht-Plan_1862_gekachelt02.tif', '19790', '22360', '22655', '25000'),
    ('images/Hobrecht-Plan_1862_gekachelt03.tif', '22655', '22360', '25520', '25000'),
    ('images/Hobrecht-Plan_1862_gekachelt04.tif', '25520', '22360', '28390', '25000'),
    ('images/Hobrecht-Plan_1862_gekachelt05.tif', '16920', '19700', '19790', '22360'),
    ('images/Hobrecht-Plan_1862_gekachelt06.tif', '19790', '19700', '22655', '22360'),
    ('images/Hobrecht-Plan_1862_gekachelt07.tif', '22655', '19700', '25520', '22360'),
    ('images/Hobrecht-Plan_1862_gekachelt08.tif', '25520', '19700', '28390', '22360'),
    ('images/Hobrecht-Plan_1862_gekachelt09.tif', '16920', '17070', '19790', '19700'),
    ('images/Hobrecht-Plan_1862_gekachelt10.tif', '19790', '17070', '22655', '19700'),
    ('images/Hobrecht-Plan_1862_gekachelt11.tif', '22655', '17070', '25520', '19700'),
    ('images/Hobrecht-Plan_1862_gekachelt12.tif', '25520', '17070', '28390', '19700'),
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
