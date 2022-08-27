from all_functions import Extract_by_name, Extract_the_shit2
import matplotlib.pyplot as plt
import numpy as np
dir='/Users/lmatak/Downloads/paper_case/daily_PM2_5_DRY.csv'
list =[]
list=Extract_the_shit2(dir,list,'PM2_5_DRY_daily ')
plt.plot(list)
plt.ylabel('PM2.5 daily avg')
plt.xlabel('date in January')
plt.xticks(np.arange(0,29))
plt.show()
