import pandas as pd

def calculate_hourly_average(file_path, output_file_path):
    """Load data from CSV, preprocess it, and calculate the overall hourly average IAQI values, then save to a file."""
    # Load the CSV file
    data = pd.read_csv(file_path)
    
    # Convert 'dtm' column to datetime and extract hour
    data['dtm'] = pd.to_datetime(data['dtm'])
    data['hour'] = data['dtm'].dt.hour
    
    # Calculate the hourly average over the day for all dates and each sensor
    hourly_avg = data.groupby(['name', 'hour'])['iaqi_value'].mean().reset_index()
    
    # Save the result to a CSV file
    hourly_avg.to_csv(output_file_path, index=False)

# Example usage
for i in range(1,9):
    file_path = f'./indoor/indoor_air_ward_{i}.csv'
    output_file_path = f'./daily_average/indoor_air_ward_{i}_hourly_avg.csv'
    calculate_hourly_average(file_path, output_file_path)
    print(f"Hourly average IAQI values saved to {output_file_path}")