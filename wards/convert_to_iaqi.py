import pandas as pd

# Load ward air quality data for each ward
ward_1 = pd.read_csv('./ward_1_air_quality_data.csv')
ward_2 = pd.read_csv('./ward_2_air_quality_data.csv')
ward_3 = pd.read_csv('./ward_3_air_quality_data.csv')
ward_4 = pd.read_csv('./ward_4_air_quality_data.csv')
ward_5 = pd.read_csv('./ward_5_air_quality_data.csv')
ward_7 = pd.read_csv('./ward_7_air_quality_data.csv')
ward_8 = pd.read_csv('./ward_8_air_quality_data.csv')

# IAQI Breakpoint table for PM2.5
breakpoints_pm25 = [
    (0, 14, 0, 20),
    (15, 34, 21, 50),
    (35, 61, 51, 90),
    (62, 95, 91, 140),
    (96, 150, 141, 200),
]

# Function to calculate IAQI for PM2.5
def pm25_iaqi(pm25):
    return calculate_iaqi(pm25, breakpoints_pm25)

# Function to calculate IAQI
def calculate_iaqi(concentration, breakpoints):
    for bp in breakpoints:
        if bp[0] <= concentration <= bp[1]:
            iaqi = ((bp[3] - bp[2]) / (bp[1] - bp[0])) * (concentration - bp[0]) + bp[2]
            return iaqi
    return None  # Return None if the concentration is out of range

# Calculate IAQI for PM2.5 for each ward
ward_1['IAQI_PM2.5'] = ward_1['pm2.5_atm'].apply(pm25_iaqi)
ward_2['IAQI_PM2.5'] = ward_2['pm2.5_atm'].apply(pm25_iaqi)
ward_3['IAQI_PM2.5'] = ward_3['pm2.5_atm'].apply(pm25_iaqi)
ward_4['IAQI_PM2.5'] = ward_4['pm2.5_atm'].apply(pm25_iaqi)
ward_5['IAQI_PM2.5'] = ward_5['pm2.5_atm'].apply(pm25_iaqi)
ward_7['IAQI_PM2.5'] = ward_7['pm2.5_atm'].apply(pm25_iaqi)
ward_8['IAQI_PM2.5'] = ward_8['pm2.5_atm'].apply(pm25_iaqi)

# Save each ward's data with IAQI values for PM2.5 to separate CSV files
ward_1.to_csv('ward_1_air_quality_with_iaqi.csv', index=False)
ward_2.to_csv('ward_2_air_quality_with_iaqi.csv', index=False)
ward_3.to_csv('ward_3_air_quality_with_iaqi.csv', index=False)
ward_4.to_csv('ward_4_air_quality_with_iaqi.csv', index=False)
ward_5.to_csv('ward_5_air_quality_with_iaqi.csv', index=False)
ward_7.to_csv('ward_7_air_quality_with_iaqi.csv', index=False)
ward_8.to_csv('ward_8_air_quality_with_iaqi.csv', index=False)
