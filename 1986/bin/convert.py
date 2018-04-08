#!/usr/bin/env python
import os

# height and width from gdalinfo
w = '3898'
h = '3874'

tif_files = (
    ('images/Berlin_1986_gekachelt\ 01.tif', '15200.000', '21720.000', '18500.000', '25000.000'),
    ('images/Berlin_1986_gekachelt\ 02.tif', '18500.000', '21720.000', '21800.000', '25000.000'),
    ('images/Berlin_1986_gekachelt\ 03.tif', '21800.000', '21720.000', '25100.000', '25000.000'),
    ('images/Berlin_1986_gekachelt\ 04.tif', '25100.000', '21720.000', '28400.000', '25000.000'),
    ('images/Berlin_1986_gekachelt\ 05.tif', '15200.000', '18440.000', '18500.000', '21720.000'),
    ('images/Berlin_1986_gekachelt\ 06.tif', '18500.000', '18440.000', '21800.000', '21720.000'),
    ('images/Berlin_1986_gekachelt\ 07.tif', '21800.000', '18440.000', '25100.000', '21720.000'),
    ('images/Berlin_1986_gekachelt\ 08.tif', '25100.000', '18440.000', '28400.000', '21720.000'),
    ('images/Berlin_1986_gekachelt\ 09.tif', '15200.000', '15160.000', '18500.000', '18440.000'),
    ('images/Berlin_1986_gekachelt\ 10.tif', '18500.000', '15160.000', '21800.000', '18440.000'),
    ('images/Berlin_1986_gekachelt\ 11.tif', '21800.000', '15160.000', '25100.000', '18440.000'),
    ('images/Berlin_1986_gekachelt\ 12.tif', '25100.000', '15160.000', '28400.000', '18440.000'),
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
