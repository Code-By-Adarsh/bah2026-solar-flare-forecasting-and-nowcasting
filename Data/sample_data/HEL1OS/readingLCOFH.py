from astropy.io import fits
from datetime import datetime
from astropy.time import Time
import numpy as np
import matplotlib.pyplot as plt

# Part 1
hdul1 = fits.open("lightcurve_cdte1.fits")
data1 = hdul1[5].data
"""
print(data1.names)
hdul1.info()
print(data1[0])
"""

# Part 2
hdul2 = fits.open("lightcurve_cdte1_2.fits")
data2 = hdul2[5].data
"""
print(data2.names)
hdul2.info()
print(data2[0])
"""


# Merge
isot = np.concatenate([data1["ISOT"], data2["ISOT"]])
ctr = np.concatenate([data1["CTR"], data2["CTR"]])
err = np.concatenate([data1["STAT_ERR"], data2["STAT_ERR"]])
unix_time = Time(isot,format='isot').unix

"""
print("Total Rows =", len(ctr))
print("Start =", isot[0])
print("End =", isot[-1])

#verification
print(data1["ISOT"][0])
print(data1["ISOT"][-1])

print(data2["ISOT"][0])
print(data2["ISOT"][-1])
"""


"""
#graph of time and ctr in unix format
plt.figure(figsize=(15,5))
plt.plot(unix_time,ctr)

plt.title("HEL1OS CDTE1 Light Curve")
plt.xlabel("Time (Unix)")
plt.ylabel("Count Rate (CTR)")

plt.grid(True)
plt.show()
"""

"""
#peak count graph
max_idx = np.nanargmax(ctr)
print("Peak Observation Index :",max_idx)
print(f"Maximum Count Value : {ctr[max_idx]} Counts")
print("Peak Time (Unix Timestamp) :",unix_time[max_idx])
print("Peak Time (UTC) :", datetime.utcfromtimestamp(unix_time[max_idx]))
"""
"""
start = peak_idx - 300
end = peak_idx + 300

plt.figure(figsize=(15,5))
plt.plot(unix_time[start:end],ctr[start:end])

plt.title("Zoomed Peak Region")
plt.xlabel("Time (Unix)")
plt.ylabel("Count Rate (CTR)")

threshold = np.nanmean(ctr) + 3*np.nanstd(ctr)

plt.axhline(
    y=threshold,
    linestyle="--",
    label="Threshold",
    color = 'red'
)

plt.legend()
plt.grid(True)

plt.show()
"""


print("Mean Count Value               :",round(np.nanmean(ctr),2))
print("Median Count Value             :",round(np.nanmedian(ctr),2))
print("Standard Deviation             :",round(np.nanstd(ctr),2))
threshold=round((np.nanmean(ctr) + 3*np.nanstd(ctr)),2)

print("Detection Threshold            :",round((np.nanmean(ctr) + 3*np.nanstd(ctr)),2))
flare_points = np.where(ctr>threshold)
print("Threshold Crossing Points      :",len(flare_points[0]))


"""
flare_points = np.where(ctr>threshold)
print("Total Flares :",len(flare_points[0]))
print("First 10 flares Indices: ",flare_points[0][:10])
"""

"""
plt.figure(figsize=(15,5))

plt.plot(unix_time, ctr)
plt.title("HEL1OS CDTE1 Flare Detection Analysis")
plt.xlabel("TIME (Unix)")
plt.ylabel("Count Rate (CTR)")

threshold = np.nanmean(ctr) + 3*np.nanstd(ctr)

plt.axhline(
    y=threshold,
    linestyle="--",
    label="Threshold",
    color = 'red'
)

plt.legend()
plt.grid(True)

plt.show()
"""
