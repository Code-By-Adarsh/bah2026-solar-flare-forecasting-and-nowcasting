from file_reader import (read_solexs,read_hel1os_cdte1)
import numpy as np

def detect_solexs_flare(solexs_data):

    time = solexs_data["time"]
    counts = solexs_data["counts"]

    mean = round(np.nanmean(counts),2)
    median = round(np.nanmedian(counts),2)
    std = round(np.nanstd(counts),2)
    threshold = round((mean + (3*std)),2)
    flare_points = np.where(counts>threshold)[0]
    peak_idx = np.nanargmax(counts)
    peak_value = counts[peak_idx]
    peak_time = time[peak_idx]

    return{
        "mean":float(mean),
        "median":float(median),
        "std":float(std),
        "threshold":float(threshold),
        "peak_value":float(peak_value),
        "peak_time":float(peak_time),
        "peak_idx":int(peak_idx),
        "flares":int(len(flare_points))
        }

"""
solexs_data = read_solexs("AL1_SOLEXS_20260615_SDD2_L1.lc")
result = detect_solexs_flare(solexs_data)
print(result)
"""

def detect_hel1os_flare(hel1os_data):

    unix_time = hel1os_data["unix_time"]
    ctr = hel1os_data["ctr"]

    mean = round(np.nanmean(ctr),2)
    median = round(np.nanmedian(ctr),2)
    std = round(np.std(ctr),2)
    threshold = round((mean+3*std),2)
    flare_points = np.where(ctr>threshold)[0]
    peak_idx = np.nanargmax(ctr)
    peak_value = ctr[peak_idx]
    peak_time = unix_time[peak_idx]

    return{
        "mean":float(mean),
        "median":float(median),
        "std":float(std),
        "threshold":float(threshold),
        "peak_value":float(peak_value),
        "peak_time":float(peak_time),
        "peak_idx":int(peak_idx),
        "flares":int(len(flare_points))
        }

"""
hel1os_data = read_hel1os_cdte1("lightcurve_cdte1.fits","lightcurve_cdte1_2.fits")
result_hel1os = detect_hel1os_flare(hel1os_data)
print(result_hel1os)
"""
