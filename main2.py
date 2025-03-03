import pandas as pd

input_data="global_temperature.svg.png"
output_data=("climate_change.png")

with open(input_data,'rb') as i:
    with open(output_data,'wb') as o:
        input_data=i.read()
        o.write(output_data)
