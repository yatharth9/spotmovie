import os
import gzip
import shutil
import requests
from bs4 import BeautifulSoup

f_name = "name.basics.tsv"
f_gz = f_name + ".gz"


url = f"https://datasets.imdbws.com/{f_gz}"
r = requests.get(url,allow_redirects=True)

open(f_gz,'wb').write(r.content)

with gzip.open(f_gz, 'rb') as f_in:
    with open(f_name, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

if os.path.exists(f_gz):
  os.remove(f_gz)
else:
  print("The file does not exist")