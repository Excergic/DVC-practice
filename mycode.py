import pandas as pd
import os

# Simple DataFrame
data = {"Name" : ["Alice", "Bob", "Charlie"],
        "Age" : [20, 25, 30],
        "City" : ["New York", "San Francisco", "Los Angeles"]
        }

df = pd.DataFrame(data)

new_row_loc = {"Name": "GF1", "Age": 21, "City": "San Francisco"}
df.loc[len(df.index)] = new_row_loc



data_dir = "data"
os.makedirs(data_dir, exist_ok=True)

#Define the file path
file_path = os.path.join(data_dir, "sample_data.csv")

#save the dataFrame to the csv file, including column names
df.to_csv(file_path, index=False)

print("csv file saved at ", file_path)

