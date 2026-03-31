# electron_density_plot.py
import cdflib
from cdflib import cdfepoch
import matplotlib.pyplot as plt
import numpy as np

# -----------------------------
# 1. Open CDF file
# -----------------------------
cdf_file = "C:\\Users\\qdh0004\\Documents\\VSCODE\\MATLAB\\Iono_Proj_2\\se_k0s_vlf_20011016160000_20011017100000_cdaweb.cdf"
cdf = cdflib.CDF(cdf_file)

# -----------------------------
# 2. Inspect variables
# -----------------------------
info = cdf.cdf_info()
print("Record variables (time-dependent):", info.rVariables)
print("zVariables (static or metadata):", info.zVariables)

# -----------------------------
# 3. Extract time and VLF amplitude
# -----------------------------
time = cdf['Epoch']  # zVariable in your file
vlf = cdf['vlf1_Amplitude']

# Convert Epoch to datetime
time_dt = cdfepoch.to_datetime(time)

# -----------------------------
# 4. Plot VLF amplitude vs time
# -----------------------------
plt.figure(figsize=(10,5))
plt.plot(time_dt, vlf)
plt.xlabel("Time")
plt.ylabel("VLF Amplitude")
plt.title("VLF Amplitude Time Series")
plt.grid(True)
plt.tight_layout()
plt.show()