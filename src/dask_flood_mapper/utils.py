import xarray as xr
import numpy as np

def post_process_eodc_cube(dc: xr.Dataset, items, bands):
    if not isinstance(bands, tuple):
        bands = tuple([bands])
    for i in bands:
        dc[i] = post_process_eodc_cube_(dc[i], items, i)
    return dc

def post_process_eodc_cube_(dc: xr.Dataset, items, band):
    scale = items[0].assets[band].extra_fields.get('raster:bands')[0]['scale']
    nodata = items[0].assets[band].extra_fields.get('raster:bands')[0]['nodata']
    return dc.where(dc != nodata) / scale

def extract_orbit_names(items):
    return np.array([items[i].properties["sat:orbit_state"][0].upper() + str(items[i].properties["sat:relative_orbit"]) for i in range(len(items))])