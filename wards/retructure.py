import pandas as pd

# Read the CSV file
df = pd.read_csv('ward_6_air_quality_data.csv')

# Reorder the columns
df = df[['time_stamp', 'humidity', 'temperature', 'pm2.5_atm', 'pm10.0_atm', 'sensor_id']]

# Save the DataFrame to a new CSV file
df.to_csv('re_ward_6_air_quality_data.csv', index=False)
