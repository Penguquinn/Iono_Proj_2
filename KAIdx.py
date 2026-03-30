import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import requests
import json
import matplotlib.dates as mdates

start = datetime(2026, 3, 29, 23, 0, 0)
end   = datetime(2026, 3, 30, 0, 0, 0)

url_goes = "https://services.swpc.noaa.gov/json/goes/primary/xrays-1-day.json"

response = requests.get(url_goes)
# Raise an error if the request failed
response.raise_for_status()

data = response.json()  # directly parses JSON into Python dict/list

# for entry in data:
#     print(entry)

elem = 0
times = np.empty(len(data), dtype=object)  # for strings
flux = 0 * np.ones(len(data))
obs_flux = 0 * np.ones(len(data))
electron_correction = 0 * np.ones(len(data))
energy = 0 * np.ones(len(data))
for entry in data:
    times[elem] = entry['time_tag']
    flux[elem] = entry['flux']
    obs_flux[elem] = entry['observed_flux']
    electron_correction[elem] = entry['electron_correction']
    energy = entry['energy']
    elem += 1

times_dt = [datetime.fromisoformat(t.replace('Z', '+00:00')) for t in times]

plt.figure(figsize=(12, 6))
plt.plot(times_dt, flux, label='flux')
# plt.plot(times_dt, obs_flux, label='observed_flux')
plt.plot(times_dt, electron_correction, label='electron_correction')
# Use AutoDateLocator to space ticks intelligently
locator = mdates.AutoDateLocator(minticks=6, maxticks=12)  
formatter = mdates.ConciseDateFormatter(locator)  

print(times_dt[0], times_dt[-1])

plt.gca().xaxis.set_major_locator(locator)
plt.gca().xaxis.set_major_formatter(formatter)
plt.xlabel('Time')
plt.ylabel('Magnetic Field (nT)')
plt.title('GOES Magnetometer Data (1 Day)')
plt.xticks(rotation=90)
plt.legend()
plt.tight_layout()
plt.show(block=True)