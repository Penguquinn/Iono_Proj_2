from cdasws import CdasWs
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt

start = datetime(2026, 3, 29, 0, 0, 0)
end   = datetime(2026, 3, 30, 0, 0, 0)


cdas = CdasWs()

dataset = 'SOHO_CELIAS-PM_30S'
var_names = cdas.get_variable_names(dataset)

# print('Variable names:', var_names)

# example_interval = cdas.get_example_time_interval(dataset)
# print('Example time interval:', example_interval)

status, data = cdas.get_data(dataset, var_names, start, end)
plt.figure(figsize=(8,4))
plt.plot( data["V_p"])
plt.title("Density vs Time")
plt.xlabel("Time Index")
plt.ylabel("Density [cm^-3]")
plt.grid(True)
plt.show(block=False)
# print(data["V_p"])

# with open("output.txt", "w") as f:
#     f.write(str(data))



import requests
import json

url = "https://services.swpc.noaa.gov/json/goes/primary/magnetometers-1-day.json"

response = requests.get(url)
# Raise an error if the request failed
response.raise_for_status()

data = response.json()  # directly parses JSON into Python dict/list

print(type(data))  # usually dict or list