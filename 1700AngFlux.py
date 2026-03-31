from astropy.io import fits
import matplotlib.pyplot as plt
from astropy.visualization import astropy_mpl_style

# Optional: use astropy's plotting style
plt.style.use(astropy_mpl_style)

# Define the file path
fits_file_path = "C:\\Users\\qdh0004\\Documents\\VSCODE\\MATLAB\\Iono_Proj_2\\AIA20260330_204500_1700.fits"

# Open the FITS file using a 'with' block
with fits.open(fits_file_path) as hdul:
    # Print a summary of the file's contents
    hdul.info()
    
    # Access data and header from the primary HDU (Header Data Unit), usually index 0
    # Data is returned as a NumPy array
    image_data = hdul[1].data
    header = hdul[1].header

# The file is automatically closed outside the 'with' block

# You can now work with the data (e.g., print its shape, access header info)
print(f"Data shape: {image_data.shape}")
# print(f"Object name from header: {header['OBJECT']}") # Access header keywords like a dictionary

# Optional: Plot the image data using matplotlib
plt.figure()
plt.imshow(image_data, cmap='gray')
plt.colorbar()
plt.title(r"Image of 1700$\AA$ Flux 2026-03-30 20:45Z")
plt.show()