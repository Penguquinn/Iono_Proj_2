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
times = np.empty([len(data),2], dtype=object)  # for strings
flux = 0 * np.ones((len(data),2))
obs_flux = 0 * np.ones((len(data),2))
electron_correction = 0 * np.ones((len(data),2))
energy = 0 * np.ones(len(data))
el = 0
for entry in data:
    if entry["energy"] == "0.05-0.4nm":
        el =0
    elif entry["energy"] == "0.1-0.8nm":
        el = 1
        elem += 1
    
    times[elem,el] = entry['time_tag']
    flux[elem,el] = entry['flux']
    obs_flux[elem,el] = entry['observed_flux']
    electron_correction[elem,el] = entry['electron_correction']
    

times_dt = [
    datetime.fromisoformat(t.replace('Z', '+00:00')) if t is not None else None
    for t in times[:, 0]
]
times_dt = [t for t in times_dt if t is not None]
# print(times_dt)

ept = 1

# Create a figure with 4 vertical subplots sharing the x-axis
fig, axs = plt.subplots(2, 1, figsize=(12, 10), sharex=True)

# Plot each variable in its own subplot
axs[0].plot(times_dt, np.log10(flux[0:elem,ept]), color='blue')
axs[0].set_ylabel(r'Flux ($Log_{10}$)')
axs[0].set_title('GOES X-Ray Flux')

axs[1].plot(times_dt, np.log10(obs_flux[0:elem,ept]), color='orange')
axs[1].set_ylabel(r'Observed Flux ($Log_{10}$)')

# axs[2].plot(times_dt, electron_correction[0:elem,ept], color='green')
# axs[2].set_ylabel('Electron Correction')

# axs[3].plot(times_dt, energy, color='red')
# axs[3].set_ylabel('Energy')
# axs[3].set_xlabel('Time')

# Format the x-axis dates
locator = mdates.AutoDateLocator(minticks=6, maxticks=12)
formatter = mdates.ConciseDateFormatter(locator)
axs[1].xaxis.set_major_locator(locator)
axs[1].xaxis.set_major_formatter(formatter)
axs[1].tick_params(axis='x', rotation=90)

plt.tight_layout()
plt.show(block=True)