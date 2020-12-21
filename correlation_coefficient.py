import numpy as np
import csv 
def get_data_source(data_path):
    ice_cream=[]
    temperature=[]
    with open(data_path) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            temperature.append(float(row["Marks In Percentage"]))
            ice_cream.append(float(row["Days Present"]))

    return {"x":ice_cream, "y":temperature}
def find_correlation_coefficients(data_source):
    correlation=np.corrcoef(data_source["x"],data_source["y"])
    print(f"Correlation : {correlation[0,1]}")
def main():
    path = "Student Marks vs Days Present.csv"
    source = get_data_source(path)
    find_correlation_coefficients(source)
main()
