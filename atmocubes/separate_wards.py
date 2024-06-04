import pandas as pd

# Load the hourly averaged data
hourly_avg_file_path = "./Hourly_Avg_Data.csv"
hourly_avg_data = pd.read_csv(hourly_avg_file_path)

# Load the atmocube ward data
ward_file_path = "./atmocubes_wards.csv"
ward_data = pd.read_csv(ward_file_path)

merged_data = pd.merge(hourly_avg_data, ward_data, on='name')

for ward_number in merged_data['ward_number'].unique():
    ward_data_subset = merged_data[merged_data['ward_number'] == ward_number]
    ward_data_subset = ward_data_subset[['name', 'dtm', 'iaqi_value']]
    output_file_path = f"./indoor/indoor_air_ward_{int(ward_number)}.csv"
    ward_data_subset.to_csv(output_file_path, index=False)
    print(f"Data for ward {int(ward_number)} saved to '{output_file_path}'")

print("All ward files have been created.")