#!/usr/bin/env python
import os

# height and width from gdalinfo
w = '3375'
h = '3103'

name = 'images/Berlin1850.tif'

tif_files = (
    ('images/Berlin_um_1880_01.tif', '16915.000', '22352.100', '19772.500', '24995.500'),
    ('images/Berlin_um_1880_02.tif', '19772.500', '22352.100', '22630.000', '24995.500'),
    ('images/Berlin_um_1880_03.tif', '22630.000', '22352.100', '25487.500', '24995.500'),
    ('images/Berlin_um_1880_04.tif', '25487.500', '22352.100', '28345.000', '24995.500'),
    ('images/Berlin_um_1880_05.tif', '16915.000', '19708.800', '19772.500', '22352.100'),
    ('images/Berlin_um_1880_06.tif', '19772.500', '19708.800', '22630.000', '22352.100'),
    ('images/Berlin_um_1880_07.tif', '22630.000', '19708.800', '25487.500', '22352.100'),
    ('images/Berlin_um_1880_08.tif', '25487.500', '19708.800', '28345.000', '22352.100'),
    ('images/Berlin_um_1880_09.tif', '16915.000', '17065.500', '19772.500', '19708.800'),
    ('images/Berlin_um_1880_10.tif', '19772.500', '17065.500', '22630.000', '19708.800'),
    ('images/Berlin_um_1880_11.tif', '22630.000', '17065.500', '25487.500', '19708.800'),
    ('images/Berlin_um_1880_12.tif', '25487.500', '17065.500', '28345.000', '19708.800'),
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
