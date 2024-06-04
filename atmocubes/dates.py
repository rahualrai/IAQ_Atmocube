import pandas as pd

# Load the data from the CSV file
file_path = "./All_Data.csv"
data = pd.read_csv(file_path)

# Convert the 'dtm' column to datetime format
data['dtm'] = pd.to_datetime(data['dtm'])

# Define the date range
start_date = '2023-11-21'
end_date = '2023-12-09'

# Filter the data to isolate entries within the date range
filtered_data = data[(data['dtm'] >= start_date) & (data['dtm'] <= end_date)]

filtered_data.to_csv("Filtered_Data.csv", index=False)