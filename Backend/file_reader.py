from astropy.io import fits
from astropy.time import Time
import numpy as np
import os

def read_solexs(filepath):

    try:
        if not os.path.exists(filepath):
            raise FileNotFoundError(
                f"File not found: {filepath}"
                )

        hdul = fits.open(filepath)
        data = hdul[1].data
        time = data["TIME"]
        counts = data["COUNTS"]
        hdul.close()

        return{
            "time" : time,
            "counts" : counts
            }

    except Exception as e:
        print(f"Error reading SoLEXS file: {e}")

        return None

"""
solexs_data = read_solexs("AL1_SOLEXS_20260615_SDD2_L1.lc")
print(len(solexs_data["time"]))
print(len(solexs_data["counts"]))
"""


def read_hel1os_cdte1(filepath1,filepath2):

    try:
        if not os.path.exists(filepath1):
            raise FileNotFoundError(
                f"File not found: {filepath1}"
            )
            
        if not os.path.exists(filepath2):
            raise FileNotFoundError(
                f"File not found: {filepath2}"
            )
    
        hdul1 = fits.open(filepath1)
        hdul2 = fits.open(filepath2)
        data1 = hdul1[5].data
        data2 = hdul2[5].data
        isot = np.concatenate([data1["ISOT"],data2["ISOT"]])
        ctr = np.concatenate([data1["CTR"],data2["CTR"]])
        unix_time = Time(isot,format='isot').unix

        hdul1.close()
        hdul2.close()

        return{
            "isot" : isot,
            "unix_time" : unix_time,
            "ctr" : ctr
            }
    
    except Exception as e:
        print(f"Error reading HEL1OS file : {e}")

        return None


"""
hel1os_data = read_hel1os_cdte1("lightcurve_cdte1.fits","lightcurve_cdte1_2.fits")
print(len(hel1os_data["unix_time"]))
print(len(hel1os_data["ctr"]))
"""
