import pandas as pd

def calculate_hourly_average_single_sensor(file_path, output_file_path):
    """Load data from CSV, preprocess it, and calculate the overall hourly average IAQI values for a single sensor, then save to a file."""
    # Load the CSV file
    data = pd.read_csv(file_path)
    
    # Convert 'time_stamp' to datetime and extract hour
    data['time_stamp'] = pd.to_datetime(data['time_stamp'], unit='s')
    data['hour'] = data['time_stamp'].dt.hour
    
    # Calculate the hourly average over the day for all dates
    hourly_avg = data.groupby('hour')['iaqi_value'].mean().reset_index()
    
    # Save the result to a CSV file
    hourly_avg.to_csv(output_file_path, index=False)

# Example usage
for i in range(0,9):
    file_path = f'./iaqi/outdoor_air_ward_{i}.csv'
    output_file_path = f'./hourly_avg_outdoor/{i}.csv'
    calculate_hourly_average_single_sensor(file_path, output_file_path)
    print(f"Hourly average IAQI values saved to {output_file_path}")
