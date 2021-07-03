#!/usr/bin/env python
# coding=utf-8
import os

# height and width from gdalinfo
w = '3898'
h = '3874'

tif_files = (
    ('Geb\xe4udesch\xe4den_1945_gekachelt 01.tif', 'gebschaden_01.tif', '15200', '21720', '18500', '25000'),
    ('Geb\xe4udesch\xe4den_1945_gekachelt 02.tif', 'gebschaden_02.tif', '18500', '21720', '21800', '25000'),
    ('Geb\xe4udesch\xe4den_1945_gekachelt 03.tif', 'gebschaden_03.tif', '21800', '21720', '25100', '25000'),
    ('Geb\xe4udesch\xe4den_1945_gekachelt 04.tif', 'gebschaden_04.tif', '25100', '21720', '28400', '25000'),
    ('Geb\xe4udesch\xe4den_1945_gekachelt 05.tif', 'gebschaden_05.tif', '15200', '18440', '18500', '21720'),
    ('Geb\xe4udesch\xe4den_1945_gekachelt 06.tif', 'gebschaden_06.tif', '18500', '18440', '21800', '21720'),
    ('Geb\xe4udesch\xe4den_1945_gekachelt 07.tif', 'gebschaden_07.tif', '21800', '18440', '25100', '21720'),
    ('Geb\xe4udesch\xe4den_1945_gekachelt 08.tif', 'gebschaden_08.tif', '25100', '18440', '28400', '21720'),
    ('Geb\xe4udesch\xe4den_1945_gekachelt 09.tif', 'gebschaden_09.tif', '15200', '15160', '18500', '18440'),
    ('Geb\xe4udesch\xe4den_1945_gekachelt 10.tif', 'gebschaden_10.tif', '18500', '15160', '21800', '18440'),
    ('Geb\xe4udesch\xe4den_1945_gekachelt 11.tif', 'gebschaden_11.tif', '21800', '15160', '25100', '18440'),
    ('Geb\xe4udesch\xe4den_1945_gekachelt 12.tif', 'gebschaden_12.tif', '25100', '15160', '28400', '18440'),
)

for tmp_file, tif_file, x_bottom_left, y_bottom_left, x_top_right, y_top_right in tif_files:
    cmd = 'gdal_translate -of GTiff -a_srs EPSG:3068 -expand rgb'
    cmd += ' -gcp 0  0  %s %s' % (x_bottom_left, y_top_right)
    cmd += ' -gcp 0  %s %s %s' % (h, x_bottom_left, y_bottom_left)
    cmd += ' -gcp %s 0  %s %s' % (w, x_top_right, y_top_right)
    cmd += ' -gcp %s %s %s %s' % (w, h, x_top_right, y_bottom_left)
    cmd += ' "%s" "%s"' % (os.path.join('tmp', tmp_file), os.path.join('tmp', tif_file))

    os.system(cmd)

    cmd = 'gdalwarp -s_srs EPSG:3068 -t_srs EPSG:3068 -r bilinear -srcnodata 0 -dstalpha %s %s' % (os.path.join('tmp', tif_file), os.path.join('tif', tif_file))

    os.system(cmd)

    cmd = 'gdalbuildvrt -a_srs EPSG:3068 tiles.vrt %s' % ' '.join([
        '"' + os.path.join('tif', file[1]) + '"' for file in tif_files
    ])

    os.system(cmd)
