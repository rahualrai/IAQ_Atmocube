import pandas as pd

# Function to calculate IAQI for PM2.5
def calculate_iaqi_pm25(concentration):
    if 0 <= concentration <= 12:
        BP_hi, BP_lo, IAQI_hi, IAQI_lo = 12, 0, 50, 0
    elif 12.1 <= concentration <= 35.4:
        BP_hi, BP_lo, IAQI_hi, IAQI_lo = 35.4, 12.1, 100, 51
    elif 35.5 <= concentration <= 55.4:
        BP_hi, BP_lo, IAQI_hi, IAQI_lo = 55.4, 35.5, 150, 101
    elif 55.5 <= concentration <= 150.4:
        BP_hi, BP_lo, IAQI_hi, IAQI_lo = 150.4, 55.5, 200, 151
    elif 150.5 <= concentration <= 250.4:
        BP_hi, BP_lo, IAQI_hi, IAQI_lo = 250.4, 150.5, 300, 201
    elif 250.5 <= concentration <= 500:
        BP_hi, BP_lo, IAQI_hi, IAQI_lo = 500, 250.5, 500, 301
    else:
        return None
    
    IAQI = ((BP_hi - BP_lo) / (IAQI_hi - IAQI_lo)) * (concentration - BP_lo) + IAQI_lo
    return IAQI

def process_file(file_name, i):
    # Read the CSV file
    df = pd.read_csv(file_name)

    # Remove the sensor_id column
    df = df.drop(columns=['sensor_id'])

    # Group by time_stamp and calculate the mean for each group
    df_grouped = df.groupby('time_stamp').mean().reset_index()

    # Calculate IAQI for PM2.5
    df_grouped['iaqi_value'] = df_grouped['pm2.5_atm'].apply(calculate_iaqi_pm25)

    # Save the resulting DataFrame to a new CSV file
    output_file_name = f"./iaqi/outdoor_air_ward_{i}.csv"

    df_grouped = df_grouped[['time_stamp', 'iaqi_value']]
    df_grouped.to_csv(output_file_name, index=False)
    print(f"Processed data saved to '{output_file_name}'")

# Loop through files ward_1_air_quality_data.csv to ward_8_air_quality_data.csv
for i in range(1, 9):
    file_name = f'./separated/ward_{i}_air_quality_data.csv'
    process_file(file_name, i)
