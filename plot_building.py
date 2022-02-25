import requests
import rasterio as rio
import numpy as np
import matplotlib.pyplot as plt
import plotly.io as pio
import plotly.graph_objects as go

def get_coordinates():
    '''Get coordinates from an address in Brussels or Flanders'''
    address = input("Type address in Dutch : ") # type address in Dutch
    url = "https://loc.geopunt.be/v4/Location?q=" + address
    response = requests.get(url)
    result = response.json()
    # print(result)
    result_dict = dict(result)
    x = result_dict['LocationResult'][0]['Location']['X_Lambert72']
    print("x:", x)
    y = result_dict['LocationResult'][0]['Location']['Y_Lambert72']
    print("y:", y)
    return x, y

def create_window(x, y):
    '''Create a window around building'''
    left = x - 100
    right = x + 100
    top = y + 100
    bottom = y - 100
    return left, right, top, bottom

def plot_2D(x, y, left, right, top, bottom):
    '''Plot building in 2D'''
    for i in range(1, 10):
        dataset = rio.open(f"C:\\Users\\vpala\\Artificial Intelligence\\BeCode\\3D-houses\\dataset\\DHMVIIDSMRAS1m_k0{i}\\GeoTIFF\\DHMVIIDSMRAS1m_k0{i}.tif")
        if x >= dataset.bounds.left and x <= dataset.bounds.right and y >= dataset.bounds.bottom and y <= dataset.bounds.top:
            window = dataset.window(left=left, bottom=bottom, right=right, top=top)
            plt.imshow(dataset.read(1, window=window))
            plt.show()
    for i in range(10, 44):
        dataset = rio.open(f"C:\\Users\\vpala\\Artificial Intelligence\\BeCode\\3D-houses\\dataset\\DHMVIIDSMRAS1m_k{i}\\GeoTIFF\\DHMVIIDSMRAS1m_k{i}.tif")
        if x >= dataset.bounds.left and x <= dataset.bounds.right and y >= dataset.bounds.bottom and y <= dataset.bounds.top:
            window = dataset.window(left=left, bottom=bottom, right=right, top=top)
            plt.imshow(dataset.read(1, window=window))
            plt.show()

def plot_3D(x, y, left, right, top, bottom):
    '''Plot building in 3D'''
    for i in range(1, 10):
        dataset = rio.open(f"C:\\Users\\vpala\\Artificial Intelligence\\BeCode\\3D-houses\\dataset\\DHMVIIDSMRAS1m_k0{i}\\GeoTIFF\\DHMVIIDSMRAS1m_k0{i}.tif")
        if x >= dataset.bounds.left and x <= dataset.bounds.right and y >= dataset.bounds.bottom and y <= dataset.bounds.top:
            window = dataset.window(left=left, bottom=bottom, right=right, top=top)
            surf = dataset.read(1, window=window)
            X = np.arange(0, surf.shape[0]*1, 1)
            Y = np.arange(0, surf.shape[1]*-1, -1)
            X, Y = np.meshgrid(X,Y)
            fig, ax = plt.subplots(subplot_kw={"projection":"3d"})
            surf = ax.plot_surface(X, Y, surf, cmap=plt.cm.magma)
            fig.colorbar(surf, shrink=0.5, aspect=5)
            fig.set_size_inches(10, 10)
            ax.view_init(75, -90)
            plt.show()
    for i in range(10, 44):
        dataset = rio.open(f"C:\\Users\\vpala\\Artificial Intelligence\\BeCode\\3D-houses\\dataset\\DHMVIIDSMRAS1m_k{i}\\GeoTIFF\\DHMVIIDSMRAS1m_k{i}.tif")
        if x >= dataset.bounds.left and x <= dataset.bounds.right and y >= dataset.bounds.bottom and y <= dataset.bounds.top:
            window = dataset.window(left=left, bottom=bottom, right=right, top=top)
            surf = dataset.read(1, window=window)
            X = np.arange(0, surf.shape[0]*1, 1)
            Y = np.arange(0, surf.shape[1]*-1, -1)
            X, Y = np.meshgrid(X,Y)
            fig, ax = plt.subplots(subplot_kw={"projection":"3d"})
            surf = ax.plot_surface(X, Y, surf, cmap=plt.cm.viridis)
            fig.colorbar(surf, shrink=0.5, aspect=5)
            fig.set_size_inches(10, 10)
            ax.view_init(75, -90)
            plt.show()

def interactive_3D(x, y , left, right, top, bottom):
    '''Plot building with interactive 3D'''
    for i in range(1, 10):
        dataset = rio.open(f"C:\\Users\\vpala\\Artificial Intelligence\\BeCode\\3D-houses\\dataset\\DHMVIIDSMRAS1m_k0{i}\\GeoTIFF\\DHMVIIDSMRAS1m_k0{i}.tif")
        if x >= dataset.bounds.left and x <= dataset.bounds.right and y >= dataset.bounds.bottom and y <= dataset.bounds.top:
            window = dataset.window(left=left, bottom=bottom, right=right, top=top)
            surf = dataset.read(1, window=window)
            X = np.arange(0, surf.shape[0]*1, 1)
            Y = np.arange(0, surf.shape[1]*-1, -1)
            X, Y = np.meshgrid(X,Y)
            pio.renderers.default = 'browser'
            fig = go.Figure(data=go.Surface(x=X, y=Y, z=surf))
            fig.show()
    for i in range(10, 44):
        dataset = rio.open(f"C:\\Users\\vpala\\Artificial Intelligence\\BeCode\\3D-houses\\dataset\\DHMVIIDSMRAS1m_k{i}\\GeoTIFF\\DHMVIIDSMRAS1m_k{i}.tif")
        if x >= dataset.bounds.left and x <= dataset.bounds.right and y >= dataset.bounds.bottom and y <= dataset.bounds.top:
            window = dataset.window(left=left, bottom=bottom, right=right, top=top)
            surf = dataset.read(1, window=window)
            X = np.arange(0, surf.shape[0]*1, 1)
            Y = np.arange(0, surf.shape[1]*-1, -1)
            X, Y = np.meshgrid(X,Y)
            pio.renderers.default = 'browser'
            fig = go.Figure(data=go.Surface(x=X, y=Y, z=surf))
            fig.show()
    
x, y = get_coordinates()
left, right, top, bottom = create_window(x, y)
plot_2D(x, y, left, right, top, bottom)
plot_3D(x, y, left, right, top, bottom)
interactive_3D(x, y, left, right, top, bottom)
