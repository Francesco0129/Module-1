import pandas as pd
df = pd.read_csv("/Users/francescopacello/BME2315 - Computational/Module 1/Metadata and Protein Data for Module 1.csv")

for header in df.columns:
    print (header)