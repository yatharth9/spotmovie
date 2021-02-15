import os
import gzip
import shutil
import requests
from bs4 import BeautifulSoup

artist_name = "name.basics.tsv"
artist_name_gz = artist_name + ".gz"

title_akas = "title.akas.tsv"
title_akas_gz = title_akas + ".gz"

title_basics = "title.basic.tsv"
title_basics_gz = title_basics + ".gz"

title_crew = "title.crew.tsv"
title_crew_gz = title_crew + ".gz"

title_ratings = "title.ratings.tsv"
title_ratings_gz = title_ratings + ".gz"

url = f"https://datasets.imdbws.com/{artist_name_gz}"
r = requests.get(url,allow_redirects=True)

open(artist_name_gz,'wb').write(r.content)

with gzip.open(artist_name_gz, 'rb') as f_in:
    with open(artist_name, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

if os.path.exists(artist_name_gz):
  os.remove(artist_name_gz)
else:
  print("The file does not exist")