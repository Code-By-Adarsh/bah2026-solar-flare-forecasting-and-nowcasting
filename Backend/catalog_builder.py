#from file_reader import (read_solexs,read_hel1os_cdte1)
#from flare_detector import (detect_solexs_flare,detect_hel1os_flare)
import pandas as pd
from datetime import datetime, timezone

def build_master_catalog(solexs_result,hel1os_result):

    catalog = [
        {
            "Event_ID":"S001",
            "Source":"SoLEXS",
            "Peak_Time":datetime.fromtimestamp(solexs_result["peak_time"],tz=timezone.utc),
            "Peak_Value":solexs_result["peak_value"],
            "Threshold":solexs_result["threshold"],
            "Flare_Points":solexs_result["flares"]

        },

        {
            "Event_ID": "H001",
            "Source": "HEL1OS",
            "Peak_Time":datetime.fromtimestamp(hel1os_result["peak_time"],tz=timezone.utc),
            "Peak_Value":hel1os_result["peak_value"],
            "Threshold":hel1os_result["threshold"],
            "Flare_Points":hel1os_result["flares"]

        }

    ]

    df = pd.DataFrame(catalog)
    df.to_csv("Outputs/master_flare_catalogue.csv",index=False)
    return df

"""
solexs_data = read_solexs("AL1_SOLEXS_20260615_SDD2_L1.lc")
hel1os_data = read_hel1os_cdte1("lightcurve_cdte1.fits","lightcurve_cdte1_2.fits")
solexs_result = detect_solexs_flare(solexs_data)
hel1os_result = detect_hel1os_flare(hel1os_data)
catalog = build_master_catalog(solexs_result,hel1os_result)
print(catalog)
"""

