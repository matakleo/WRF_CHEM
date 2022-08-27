from turtle import right
from typing import Counter
from wrf import (getvar, interplevel, smooth2d, to_np, latlon_coords, get_cartopy, cartopy_xlim, cartopy_ylim)
from all_functions import Extract_Track_Data,list_ncfiles,Extract_the_shit2
from cartopy.mpl.gridliner import LongitudeFormatter, LATITUDE_FORMATTER
from cartopy.feature import NaturalEarthFeature
import matplotlib as mpl
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.pyplot as plt
import scipy.ndimage as ndimage
from netCDF4 import Dataset
import cartopy.crs as crs
import numpy as np

from mpl_toolkits.axes_grid1 import make_axes_locatable
import os
import cartopy.feature as cfeature


fig, ax = plt.subplots(nrows=1, ncols=3,subplot_kw={'projection': crs.PlateCarree()},figsize=(16.3, 8.3))


cmap=plt.get_cmap(
    'twilight_shifted')
cmap2=plt.get_cmap(
    'plasma'
)


titles=['wspd@500m - YSU to LES -d01','wspd@500m - YSU to LES -d02','wspd@500m - YSU to LES -d03','wspd@500m - YSU to LES -d03']
max_wspd=0
agl=500
time_idx=0
Input_Dir = '/Users/lmatak/Downloads/'
os.chdir(Input_Dir)
ncfiles=[]
ncfiles = list_ncfiles(Input_Dir, ncfiles)
print(ncfiles)

for i in range(len(ncfiles)):

    Data = Dataset(ncfiles[i])
    # height = getvar(Data, "height_agl",time_idx)
    # z=getvar(Data,"z",time_idx)
    # temp = getvar(Data, "U",time_idx)
    wspd = getvar(Data, "wspd", timeidx = 0)
    height = getvar(Data, "height_agl")
    wspd_500 = interplevel(wspd, height, agl)
    # print(temp)
    # temp=interplevel(temp,height,agl)
    # print(temp)
    lvls=[]

    # wspd_100=interplevel(wspd,height,agl)
    # if np.amax(wspd_100)>max_wspd:
    #     max_wspd=np.amax(wspd_100)
    # co_agl=interplevel(co,height,agl)


    # ax[i].stock_img()
    # ax[i].coastlines('110m', linewidth=0.8)
    # ax[i].add_feature(cfeature.LAND)
    # ax[i].add_feature(cfeature.STATES)
    # ax[i].add_feature(cfeature.OCEAN)

    lats1, lons1 = latlon_coords(wspd_500)

    ax[i].set_extent([float(lons1[0][0]),float(lons1[-1][-1]),float(lats1[0][0]),float(lats1[-1][-1])])

    # # Get the cartopy mapping object
    cart_proj = get_cartopy(wspd_500)
    ax[i].contourf(to_np(lons1), to_np(lats1), to_np(wspd_500), 255, 
        transform=crs.PlateCarree(), 
        cmap=cmap)
    ax[i].set_title(titles[i])
    gl = ax[i].gridlines(crs=crs.PlateCarree(), draw_labels=True,
                        linewidth=0.2, color='black', alpha=0.2, linestyle='--')
    gl.top_labels = False
    gl.right_labels = False
    gl.xlabel_style= {'size': 12, 'color': 'black'}  
    gl.ylabel_style= {'size': 12, 'color': 'black'}
    # ax[1].contourf(to_np(lons1), to_np(lats1), to_np(co_agl), 255, 
    #     transform=crs.PlateCarree(), 
    #     cmap=cmap)
    

    real_data_file='/Users/lmatak/Desktop/WRF_chem_scripts/wrf_chem_real_data/xlsx/measureing_locations.csv'

    obs_stations_longitudes =[]
    obs_stations_latitudes=[]
    obs_stat_sim_lats=[]
    obs_stat_sim_lons=[]
    obs_stations_longitudes=Extract_the_shit2(real_data_file,obs_stations_longitudes,'LON')
    obs_stations_latitudes=Extract_the_shit2(real_data_file,obs_stations_latitudes,'LAT')
    obs_stat_sim_lons=Extract_the_shit2(real_data_file,obs_stat_sim_lons,'LON_sim')
    obs_stat_sim_lats=Extract_the_shit2(real_data_file,obs_stat_sim_lats,'LAT_sim')
    # print(obs_stations_latitudes,obs_stations_longitudes)
    ax[i].scatter(obs_stations_longitudes,obs_stations_latitudes,s=55,c='red',transform=crs.PlateCarree(), )
    ax[i].scatter(obs_stat_sim_lons,obs_stat_sim_lats,s=55,c='blue',transform=crs.PlateCarree(), )
norm1 = mpl.colors.Normalize(vmin=0, vmax=np.amax(wspd_500))

cbar1=fig.colorbar(mpl.cm.ScalarMappable(norm=norm1, cmap=cmap),
ax=ax[2], orientation='horizontal',  extend='both',
label="wspd at 500m")
    





# h,l=ax[0].get_legend_handles_labels()
# ax[0].legend(h,l)

plt.show()