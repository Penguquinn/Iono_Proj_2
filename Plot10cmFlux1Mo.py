import requests
import matplotlib.pyplot as plt
import numpy as np

# URL of the flux data
url = "https://spaceweather.gc.ca/solar_flux_data/daily_flux_values/fluxtable.txt"

# Fetch the file
response = requests.get(url)
response.raise_for_status()  # Raise error if request fails

# Split into lines
lines = response.text.splitlines()

# Prepare lists for each column
fluxdate = []
fluxtime = []
fluxjulian = []
fluxcarrington = []
fluxobsflux = []
fluxadjflux = []
fluxursi = []

# Skip the first two lines (header + dashes)
for line in lines[2:]:
    parts = line.strip().split()
    if len(parts) == 7:
        fluxdate.append(parts[0])
        fluxtime.append(parts[1])
        fluxjulian.append(float(parts[2]))
        fluxcarrington.append(float(parts[3]))
        fluxobsflux.append(float(parts[4]))
        fluxadjflux.append(float(parts[5]))
        fluxursi.append(float(parts[6]))

nobs = np.array(fluxobsflux)
mean = np.mean(nobs)
std = np.std(nobs)
outidx = nobs >= 4*std
nobs[outidx] = mean

plt.figure(figsize=(10, 5))
plt.plot(fluxjulian, nobs, linestyle='-', color='blue')
plt.xlabel("Julian Date")
plt.ylabel("Adjusted Flux (10.7cm)")
plt.title("Adjusted Solar Flux (10.7cm) vs Julian Date")
plt.grid(True)
plt.tight_layout()
plt.show()
