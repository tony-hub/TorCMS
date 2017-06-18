# -*- coding: utf-8 -*-

'''
Download the f2e libs from internet.
'''

import os
import zipfile
import urllib.request

OUT_PATH = './static/f2elib'

if os.path.exists(OUT_PATH):
    pass
else:
    os.mkdir(OUT_PATH)


def fetch_file(url, filename):
    '''
    Feting the file.
    :param url:
    :param filename:
    :return:
    '''
    outfile = os.path.join(OUT_PATH, filename)
    if os.path.exists(outfile):
        # print('Exists: ', outfile)
        return True
    print('fetch ...')
    print(' ' * 4 + url)

    urllib.request.urlretrieve(url, outfile)
    zip_file = outfile
    f = zipfile.ZipFile(zip_file, 'r')
    for zfile in f.namelist():
        f.extract(zfile, OUT_PATH)


def get_jquery():
    '''
    Get JQuery library.
    :return: None
    '''
    jquery_url = 'http://r.osgeo.cn/f2elib/jquery.zip'
    qian, hou = os.path.split(jquery_url)
    fetch_file(jquery_url, hou)


def get_leaflet():
    '''
    Get LeafletJS library.
    :return: None
    '''
    leaflet_url = 'http://r.osgeo.cn/f2elib/leaflet_1.0.3.zip'
    qian, hou = os.path.split(leaflet_url)
    fetch_file(leaflet_url, hou)


def get_bootstrap():
    '''
    Get BootStrop CSS library.
    :return: None
    '''
    leaflet_url = 'http://r.osgeo.cn/f2elib/bootstrap_3.3.7.zip'
    qian, hou = os.path.split(leaflet_url)
    fetch_file(leaflet_url, hou)


def get_js_valid():
    '''
    Get JQuery-Validation library.
    :return: None 
    '''
    leaflet_url = 'http://r.osgeo.cn/f2elib/jquery-validation_1.15.0.zip'
    qian, hou = os.path.split(leaflet_url)
    fetch_file(leaflet_url, hou)


def get_codemirror():
    '''
    Get CodeMirror JavaScript library.
    :return: None
    '''
    leaflet_url = 'http://r.osgeo.cn/f2elib/codemirror_5.25.0.zip'
    qian, hou = os.path.split(leaflet_url)
    fetch_file(leaflet_url, hou)


def get_jqueryui():
    '''
    Get JQueryUI library.
    :return: None
    '''
    leaflet_url = 'http://r.osgeo.cn/f2elib/jqueryui_1.12.1.zip'
    qian, hou = os.path.split(leaflet_url)
    fetch_file(leaflet_url, hou)


def get_rating():
    '''
    Get BootStrop Star Rating library.
    :return: None
    '''
    leaflet_url = 'http://r.osgeo.cn/f2elib/bootstrap-star-rating-master.zip'
    qian, hou = os.path.split(leaflet_url)
    fetch_file(leaflet_url, hou)


def get_magnific():
    '''
    Get Magnific PopUp JavaScript library.
    :return: None
    '''
    leaflet_url = 'http://r.osgeo.cn/f2elib/magnific-popup_1.1.0.zip'
    qian, hou = os.path.split(leaflet_url)
    fetch_file(leaflet_url, hou)


def get_ol3():
    '''
    Get OpenLayers3 JavaScript library.
    :return: None
    '''
    # ol3_url = 'https://github.com/openlayers/ol3/releases/download/v3.18.2/v3.18.2-dist.zip'

    # qian, hou = os.path.split(ol3_url)
    # fetch_file(ol3_url, hou, outdir='ol3')

    tdir = os.path.join(OUT_PATH, 'ol3')
    if os.path.exists(tdir):
        pass
    else:
        os.mkdir(tdir)

    ol3_css = 'http://cdn.bootcss.com/ol3/3.18.2/ol.css'
    fetch_file(ol3_css, 'ol3/ol.css')

    ol3_js = 'http://cdn.bootcss.com/ol3/3.18.2/ol.js'
    fetch_file(ol3_js, 'ol3/ol.js')


def run_f2elib(*args):
    '''
    Get All the libraries.
    :param args: 
    :return: None
    '''
    get_jqueryui()
    get_codemirror()
    get_js_valid()
    get_leaflet()
    get_jquery()
    # get_ol3()
    get_bootstrap()
    get_rating()
    get_magnific()
