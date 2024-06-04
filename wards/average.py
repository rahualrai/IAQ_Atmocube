import pandas as pd

# Function to process a single file
def process_file(file_name):
    # Read the CSV file
    df = pd.read_csv(file_name)

    # Remove the sensor_id column
    df = df.drop(columns=['sensor_id'])

    # Group by time_stamp and calculate the mean for each group
    df_grouped = df.groupby('time_stamp').mean().reset_index()

    # Save the resulting DataFrame to a new CSV file
    output_file_name = f"./average/{file_name.replace('.csv', '_average.csv')}"
    df_grouped.to_csv(output_file_name, index=False)
    print(f"Processed data saved to '{output_file_name}'")

# Loop through files ward_1_air_quality_data.csv to ward_8_air_quality_data.csv
for i in range(1, 9):
    file_name = f'./ward_{i}_air_quality_data.csv'
    process_file(file_name)
