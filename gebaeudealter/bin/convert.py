#!/usr/bin/env python
# coding=utf-8
import os

tif_files = (
    ('images/Gebudealter_1992-93_nordwest_gekachelt_01.tif', '2380', '2260', '16085', '23887', '18105', '25797'),
    ('images/Gebudealter_1992-93_nordwest_gekachelt\ 02.tif', '2380', '2260','18105', '23887', '20125', '25797'),
    ('images/Gebudealter_1992-93_nordwest_gekachelt\ 03.tif', '2380', '2260','20125', '23887', '22145', '25797'),
    ('images/Gebudealter_1992-93_nordwest_gekachelt\ 04.tif', '2380', '2260','22145', '23887', '24165', '25797'),
    ('images/Gebudealter_1992-93_nordwest_gekachelt\ 05.tif', '2380', '2260','16085', '21977', '18105', '23887'),
    ('images/Gebudealter_1992-93_nordwest_gekachelt\ 06.tif', '2380', '2260','18105', '21977', '20125', '23887'),
    ('images/Gebudealter_1992-93_nordwest_gekachelt\ 07.tif', '2380', '2260','20125', '21977', '22145', '23887'),
    ('images/Gebudealter_1992-93_nordwest_gekachelt\ 08.tif', '2380', '2260','22145', '21977', '24165', '23887'),
    ('images/Gebudealter_1992-93_nordwest_gekachelt\ 09.tif', '2380', '2260','16085', '20060', '18105', '21977'),
    ('images/Gebudealter_1992-93_nordwest_gekachelt\ 10.tif', '2380', '2260','18105', '20060', '20125', '21977'),
    ('images/Gebudealter_1992-93_nordwest_gekachelt\ 11.tif', '2380', '2260','20125', '20060', '22145', '21977'),
    ('images/Gebudealter_1992-93_nordwest_gekachelt\ 12.tif', '2380', '2260','22145', '20060', '24165', '21977'),
    ('images/Gebudealter_1992-93_sdwest_gekachelt\ 01.tif', '2383', '2079', '16085', '18322', '18105', '20077'),
    ('images/Gebudealter_1992-93_sdwest_gekachelt\ 02.tif', '2383', '2079', '18105', '18322', '20125', '20077'),
    ('images/Gebudealter_1992-93_sdwest_gekachelt\ 03.tif', '2383', '2079', '20125', '18322', '22145', '20077'),
    ('images/Gebudealter_1992-93_sdwest_gekachelt\ 04.tif', '2383', '2079', '22145', '18322', '24165', '20077'),
    ('images/Gebudealter_1992-93_sdwest_gekachelt\ 05.tif', '2383', '2079', '16085', '16558', '18105', '18322'),
    ('images/Gebudealter_1992-93_sdwest_gekachelt\ 06.tif', '2383', '2079', '18105', '16558', '20125', '18322'),
    ('images/Gebudealter_1992-93_sdwest_gekachelt\ 07.tif', '2383', '2079', '20125', '16558', '22145', '18322'),
    ('images/Gebudealter_1992-93_sdwest_gekachelt\ 08.tif', '2383', '2079', '22145', '16558', '24165', '18322'),
    ('images/Gebudealter_1992-93_sdwest_gekachelt\ 09.tif', '2383', '2079', '16085', '14800', '18105', '16558'),
    ('images/Gebudealter_1992-93_sdwest_gekachelt\ 10.tif', '2383', '2079', '18105', '14800', '20125', '16558'),
    ('images/Gebudealter_1992-93_sdwest_gekachelt\ 11.tif', '2383', '2079', '20125', '14800', '22145', '16558'),
    ('images/Gebudealter_1992-93_sdwest_gekachelt\ 12.tif', '2383', '2079', '22145', '14800', '24165', '16558'),
    ('images/Gebudealter_1992-93_nordost_gekachelt\ 01.tif', '1849', '2256', '24135', '23887', '25702', '25797'),
    ('images/Gebudealter_1992-93_nordost_gekachelt\ 02.tif', '1849', '2256', '25702', '23887', '27280', '25797'),
    ('images/Gebudealter_1992-93_nordost_gekachelt\ 03.tif', '1849', '2256', '27280', '23887', '28830', '25797'),
    ('images/Gebudealter_1992-93_nordost_gekachelt\ 04.tif', '1849', '2256', '28830', '23887', '30410', '25797'),
    ('images/Gebudealter_1992-93_nordost_gekachelt\ 05.tif', '1849', '2256', '24135', '21977', '25702', '23887'),
    ('images/Gebudealter_1992-93_nordost_gekachelt\ 06.tif', '1849', '2256', '25702', '21977', '27280', '23887'),
    ('images/Gebudealter_1992-93_nordost_gekachelt\ 07.tif', '1849', '2256', '27280', '21977', '28830', '23887'),
    ('images/Gebudealter_1992-93_nordost_gekachelt\ 08.tif', '1849', '2256', '28830', '21977', '30410', '23887'),
    ('images/Gebudealter_1992-93_nordost_gekachelt\ 09.tif', '1849', '2256', '24135', '20060', '25702', '21977'),
    ('images/Gebudealter_1992-93_nordost_gekachelt\ 10.tif', '1849', '2256', '25702', '20067', '27280', '21977'),
    ('images/Gebudealter_1992-93_nordost_gekachelt\ 11.tif', '1849', '2256', '27280', '20067', '28830', '21977'),
    ('images/Gebudealter_1992-93_nordost_gekachelt\ 12.tif', '1849', '2256', '28830', '20067', '30410', '21977'),
    ('images/Gebudealter_1992-93_sdost_gekachelt_01.tif', '1859', '2096', '24135', '18332', '25702', '20110'),
    ('images/Gebudealter_1992-93_sdost_gekachelt_02.tif', '1859', '2096', '25702', '18332', '27280', '20110'),
    ('images/Gebudealter_1992-93_sdost_gekachelt_03.tif', '1859', '2096', '27280', '18332', '28830', '20110'),
    ('images/Gebudealter_1992-93_sdost_gekachelt_04.tif', '1859', '2096', '28830', '18332', '30410', '20110'),
    ('images/Gebudealter_1992-93_sdost_gekachelt_05.tif', '1859', '2096', '24135', '16558', '25702', '18332'),
    ('images/Gebudealter_1992-93_sdost_gekachelt_06.tif', '1859', '2096', '25702', '16558', '27280', '18332'),
    ('images/Gebudealter_1992-93_sdost_gekachelt_07.tif', '1859', '2096', '27280', '16558', '28830', '18322'),
    ('images/Gebudealter_1992-93_sdost_gekachelt_08.tif', '1859', '2096', '28830', '16558', '30410', '18322'),
    ('images/Gebudealter_1992-93_sdost_gekachelt_09.tif', '1859', '2096', '24135', '14800', '25702', '16558'),
    ('images/Gebudealter_1992-93_sdost_gekachelt_10.tif', '1859', '2096', '25702', '14800', '27280', '16558'),
    ('images/Gebudealter_1992-93_sdost_gekachelt_11.tif', '1859', '2096', '27280', '14800', '28830', '16558'),
    ('images/Gebudealter_1992-93_sdost_gekachelt_12.tif', '1859', '2096', '28830', '14800', '30410', '16558')
)

for tif_file, width, height, x_bottom_left, y_bottom_left, x_top_right, y_top_right  in tif_files:
    cmd = 'gdal_translate -of GTiff -a_srs EPSG:3068 -expand rgb'
    cmd += ' -gcp 0  0  %s %s' % (x_bottom_left, y_top_right)
    cmd += ' -gcp 0  %s %s %s' % (height, x_bottom_left, y_bottom_left)
    cmd += ' -gcp %s 0  %s %s' % (width, x_top_right, y_top_right)
    cmd += ' -gcp %s %s %s %s' % (width, height, x_top_right, y_bottom_left)
    cmd += ' %s %s' % (tif_file, tif_file + '.tmp.tif')

    os.system(cmd)

    cmd = 'gdalwarp -overwrite -s_srs EPSG:3068 -t_srs EPSG:3068 -r bilinear -srcnodata 0 -dstalpha %s %s' % (tif_file + '.tmp.tif', tif_file + '.gdal.tif')

    os.system(cmd)

cmd = 'gdalbuildvrt -a_srs EPSG:3068 -overwrite tiles.vrt images/*.gdal.tif'
os.system(cmd)
