import pandas as pd
import matplotlib.pyplot as plt

def calculate_hourly_average(file_path, is_single_sensor):
    """Load data from CSV, preprocess it, and calculate the overall hourly average IAQI values."""
    # Load the CSV file
    data = pd.read_csv(file_path)
    
    # Convert 'time_stamp' or 'dtm' to datetime and extract hour
    if is_single_sensor:
        data['time_stamp'] = pd.to_datetime(data['time_stamp'], unit='s')
        data['hour'] = data['time_stamp'].dt.hour
        hourly_avg = data.groupby('hour')['iaqi_value'].mean().reset_index()
    else:
        data['dtm'] = pd.to_datetime(data['dtm'])
        data['hour'] = data['dtm'].dt.hour
        hourly_avg = data.groupby(['name', 'hour'])['iaqi_value'].mean().reset_index()
    
    return hourly_avg

def plot_hourly_averages(ward_number, indoor_file_path, outdoor_file_path):
    """Plot the hourly average IAQI values for a given ward."""
    indoor_data = calculate_hourly_average(indoor_file_path, is_single_sensor=False)
    outdoor_data = calculate_hourly_average(outdoor_file_path, is_single_sensor=True)
    
    indoor_sensors = indoor_data['name'].unique()
    
    plt.figure(figsize=(14, 7))

    # Plot outdoor data with bold lines
    plt.plot(outdoor_data['hour'], outdoor_data['iaqi_value'], label=f'Outdoor Ward {ward_number}', linewidth=2.5)

    # Plot indoor data with dashed lines
    for sensor in indoor_sensors:
        sensor_data = indoor_data[indoor_data['name'] == sensor]
        plt.plot(sensor_data['hour'], sensor_data['iaqi_value'], linestyle='--', label=f'Indoor Ward {ward_number} - {sensor}')

    plt.xlabel('Hour of the Day')
    plt.ylabel('Average IAQI Value')
    plt.title(f'Hourly Average IAQI Values for Ward {ward_number}')
    plt.legend()
    plt.grid(True)
    plt.xticks(range(0, 24))

    # Show the plot
    plt.show()

# Iterate through wards 1 to 8
for ward in range(1, 8):
    indoor_file_path = f'./atmocubes/daily_average/indoor_air_ward_{ward}_hourly_avg.csv'
    outdoor_file_path = f'./wards/daily_average/outdoor_air_ward_{ward}_hourly_avg.csv'
    plot_hourly_averages(ward, indoor_file_path, outdoor_file_path)
