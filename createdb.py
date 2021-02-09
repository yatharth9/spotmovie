import pandas as pd

filename = "name.basics.tsv"

filedelimiter = "\t"

moviedata = pd.read_csv(filename, delimiter=filedelimiter)

print(moviedata.head(3))