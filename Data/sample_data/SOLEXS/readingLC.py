from astropy.io import fits
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np

hdul = fits.open("AL1_SOLEXS_20260615_SDD2_L1.lc")


hdul.info()


data = hdul[1].data


print(data.names)


"""
print(data[1])
print(data[2])
print(data[3])
"""

time = data["TIME"]
count = data["COUNTS"]

"""
plt.figure(figsize=(15,5))
plt.plot(time,count)

plt.title("SoLEXS Light Curve")
plt.xlabel("TIME (Unix)")
plt.ylabel("COUNTS")
plt.grid(True)
plt.show()
"""


"""
for t in time[:5]:
    print(datetime.utcfromtimestamp(t))


print(datetime.utcfromtimestamp(time.min()))
print(datetime.utcfromtimestamp(time.max()))
"""

"""
#print("Max Count =",np.nanmax(count))

max_idx = np.nanargmax(count)

print("Peak Observation Index :",max_idx)
print(f"Maximum Count Value : {count[max_idx]} Counts")
print("Peak Time (Unix Timestamp) :",time[max_idx])
print("Peak Time (UTC) :", datetime.utcfromtimestamp(time[max_idx]))
"""

"""
print("Mean Count Value               :", round(np.nanmean(count),2))
print("Median Count Value             :",round(np.nanmedian(count),2))
print("Standard Deviation             :",round(np.nanstd(count),2))

print("Detection Threshold            :",round((np.nanmean(count) + 3*np.nanstd(count)),2))
flare_points = np.where(count>27)
print("Threshold Crossing Points      :",len(flare_points[0]))
print("First 10 flares indices :",flare_points[0][:10])
"""

"""
# Top 10 flare indices (highest counts)
top10_idx = np.argsort(count)[-10:][::-1]
print("\nTop 10 Flares:")
print("-" * 50)

for i, idx in enumerate(top10_idx, start=1):
    print(f"{i}. Time = {time[idx]}, Count = {count[idx]}")

"""
"""
#for creating zoom graph of peak count
peak_idx = np.nanargmax(count)
start = peak_idx - 300
end = peak_idx + 300

print("Start Index:", start)
print("Peak Index:", peak_idx)
print("End Index:", end)

plt.figure(figsize=(15,5))
plt.plot(time[start:end], count[start:end])

plt.title("Zoomed Peak Region")
plt.xlabel("TIME (Unix)")
plt.ylabel("COUNTS")

threshold = np.nanmean(count) + 3*np.nanstd(count)

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
"""
plt.figure(figsize=(15,5))

plt.plot(time, count)
plt.title("SoLEXS Flare Detection Analysis")
plt.xlabel("TIME (Unix)")
plt.ylabel("COUNTS")

threshold = np.nanmean(count) + 3*np.nanstd(count)

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
