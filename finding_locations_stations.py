
from audioop import avg
from netCDF4 import Dataset
from numpy.core.fromnumeric import shape, size, transpose
from wrf import getvar,interplevel,latlon_coords
import numpy as np
import math
import csv
import os

from xarray import Coordinate
from all_functions import list_ncfiles, create_file
import glob


def find_nearest(array, value):
    array = np.asarray(array)
    # print(np.abs(array - value))
    idx = (np.abs(array - value)).argmin()
    return idx


#check the output folder!!!!

Input_Dir = '/Users/lmatak/Downloads/test_domain2/'

#what you wanna get:?
var="PM2_5_DRY"
#at what altitude?
alt=50

### this is for four domain run!
# CAMS1_pos=([120],[72])
# CAMS55_pos=([105],[58])
# CAMS35_pos=([75],[109])
# CAMS695_pos=([97],[24])
# CAMS416_pos=([83],[43])
## theser are for three domain run:

# CAMS1_pos=([64],[73])
# CAMS55_pos=([61],[70])
# CAMS35_pos=([55],[80])
# CAMS695_pos=([59],[63])
# CAMS416_pos=([56],[67])

## these are for two domain run

CAMS1_pos=([67],[69])
CAMS55_pos=([67],[69])
CAMS35_pos=([66],[71])
CAMS695_pos=([66],[67])
CAMS416_pos=([66],[68])

CAMS_POSITIONS=[CAMS1_pos,CAMS55_pos,CAMS35_pos,CAMS695_pos,CAMS416_pos]


time_idx=0
os.chdir(Input_Dir)
ncfiles = []
########## list to hold the wrfout files ##########
for file in glob.glob(Input_Dir+'wrfout_d02*'):
    ncfiles.append(file)



cams1_long=-95.220582
cams1_lat=29.767996
cams55_long=-95.257605
cams55_lat=	29.733741
cams35_long=-95.12851
cams35_lat=	29.670058
cams695_long=-95.3414
cams695_lat=29.7176
cams416_long=-95.294722
cams416_lat=29.686389

cams=3
cams_names=['cams1','cams55','cams35','cams695','cams416']
cams_lats=[cams1_lat,cams55_lat,cams35_lat,cams695_lat,cams416_lat]
cams_longs=[cams1_long,cams55_long,cams35_long,cams695_long,cams416_long]

for ncfile in ncfiles:
    print('ncfile = '+ncfile)

    ########## load the data ##########
    data = Dataset(ncfile)
    height = getvar(data, "height_agl",time_idx)
    T2=getvar(data,'T2',0)


    ## HERE YOU FIND THE POSITIONS OF THE CAMS MEASURE POSITION
    ## READ THE NUMBER FROM THE PRINT STATEMENTS, THEY ARE POSITIONS IN DOMAIN!
    ## UPDATE ON CARYA FOR EXTRACTION!!
    ## number at T2.XLONG[X] doesn't even matter..
    ## just enter here which camsx_long and camsx_lat you're looking for, and it will spit out 
    ## inteeger positions
    ## and btw the order of the positions is reversed! so what you get from the print statement, just reverse it!
    for cams in range(len(cams_lats)):
        print(cams_names[cams]+' lat=',int(find_nearest(T2.XLAT,cams_lats[cams])/len(T2.XLAT)), cams_names[cams]+' lon=',find_nearest(T2.XLONG[10],cams_longs[cams])) 

    # print(cams_names[cams]+' lon=',find_nearest(T2.XLONG[10],cams_longs[cams]))
    
    #THIS print statement is optional, if you wanna comapre with excel positions
i=0
for cams_pos in CAMS_POSITIONS:
    # print(float(T2[cams_pos].XLONG)-cams_longs[i],float(T2[cams_pos].XLAT-cams_lats[i]))
    print(float(T2[cams_pos].XLONG),float(T2[cams_pos].XLAT))
    i+=1
   

