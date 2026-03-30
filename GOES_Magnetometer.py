import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import requests
import json
import matplotlib.dates as mdates

start = datetime(2026, 3, 29, 23, 0, 0)
end   = datetime(2026, 3, 30, 0, 0, 0)

url_goes = "https://services.swpc.noaa.gov/json/goes/primary/magnetometers-1-day.json"

response = requests.get(url_goes)
# Raise an error if the request failed
response.raise_for_status()

data = response.json()  # directly parses JSON into Python dict/list

elem = 0
times = np.empty(len(data), dtype=object)  # for strings
Hn = 0 * np.ones(len(data))
He = 0 * np.ones(len(data))
Hp = 0 * np.ones(len(data))
for entry in data:
    times[elem] = entry['time_tag']
    Hn[elem] = entry['Hn']
    He[elem] = entry['He']
    Hp[elem] = entry['Hp']
    elem += 1

times_dt = [datetime.fromisoformat(t.replace('Z', '+00:00')) for t in times]

plt.figure(figsize=(12, 6))
plt.plot(times_dt, Hn, label='Hn')
plt.plot(times_dt, He, label='He')
plt.plot(times_dt, Hp, label='Hp')
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