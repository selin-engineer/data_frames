from cProfile import label

import pandas as pd

climate_change_data=pd.read_csv('GlobalTemperature.csv')
climate_change_data.head()

climate_change_data=climate_change_data.rename(columns={'°C':'°C','°F':'°F'})

climate_change_data['Year']=pd.to_datetime(climate_change_data['Year'])
climate_change_data=climate_change_data.sort_values(by='Year')

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime

plt.plot(climate_change_data['Year'],climate_change_data['°C'],label='°C',color='gray')
plt.plot(climate_change_data['Year'],climate_change_data['°F'],label='°F',color='black')
plt.legend()
//plt.show()



