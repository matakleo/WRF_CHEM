
import numpy as np
import matplotlib.pyplot as plt
from all_functions import Extract_by_name, Extract_the_shit2
import glob


fig, axes = plt.subplots(nrows=3, ncols=2,figsize=(17,8)) 
row=0
col=0
##REAL DATA
dir='/Users/lmatak/Desktop/WRF_chem_scripts/wrf_chem_real_data/'
real_data = dir+'CAMS1_AND_35_avg_apr26_apr27.csv'
real_data_vars_to_plot=["PM2.5","Temperature","NO","NO2","WSPD","O3"]
for real_data_var in real_data_vars_to_plot:
    tmp_list=[]
    tmp_list=Extract_the_shit2(real_data,tmp_list,real_data_var)
    axes[row,col].plot(tmp_list,label='OBS data', linewidth=3,color='black')
    col+=1
    if col>1:
        row+=1
        col=0
    if row>2:
        row=0
        col=0

    


## SIM DATA ##
sim_dir='/Users/lmatak/Downloads/two_domain_PBLS/'
sim_files=[]
for file in glob.glob(sim_dir+'*.csv'):
    sim_files.append(file)
sim_files.sort()
print(sim_files)

##PLOTTING ##
sims_to_plot=['chem_112','chem_202']
vars_to_plot=["pm25","Temperature","no","no2","WSPD","ozone"]


sim_file_number=0
for sim_file in sim_files:
    print(sim_file)
    for tmp_var in vars_to_plot:
        
        tmp_list=[]
        tmp_list=Extract_by_name(sim_file,tmp_list,tmp_var)
        axes[row,col].plot(tmp_list,label=sims_to_plot[sim_file_number])
        axes[row,col].set_title(tmp_var)
        col+=1
        if col>1:
            row+=1
            col=0
        if row>2:
            row=0
    sim_file_number+=1
    
plt.legend()
plt.show()