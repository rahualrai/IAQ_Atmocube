import pandas as pd

# Load the filtered data from the CSV file
file_path = "./Filtered_Data.csv"
filtered_data = pd.read_csv(file_path)

# Verify the columns in the loaded data
print("Columns in the CSV file:", filtered_data.columns)

# Check if 'iaqi_value' is in the columns
if 'iaqi_value' in filtered_data.columns:
    # Convert the 'dtm' column to datetime format
    filtered_data['dtm'] = pd.to_datetime(filtered_data['dtm'])

    # Keep only the required columns
    filtered_data = filtered_data[['name', 'dtm', 'iaqi_value']]

    # Round down the datetime to the nearest hour for averaging
    filtered_data['dtm'] = filtered_data['dtm'].dt.floor('H')

    # Calculate the hourly average of iaqi_value for each name
    hourly_avg = filtered_data.groupby(['name', 'dtm']).mean().reset_index()

    # Save the filtered and averaged data to a new CSV file
    hourly_avg.to_csv("Hourly_Avg_Data.csv", index=False)

    print("Filtered and averaged data saved to 'Hourly_Avg_Data.csv'")
else: 
    print("Error: 'iaqi_value' column is not present in the CSV file.")
