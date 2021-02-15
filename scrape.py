# To find the paths
import os
# To unzip the .gz file
import gzip
# For file manipulation
import shutil
# For getting the data from remote server
import requests
# For web scraping
from bs4 import BeautifulSoup

# All the below variables are for the tsv files and their .gz counterparts
artist_name = "name.basics.tsv"
artist_name_gz = artist_name + ".gz"

title_akas = "title.akas.tsv"
title_akas_gz = title_akas + ".gz"

title_basics = "title.basics.tsv"
title_basics_gz = title_basics + ".gz"

title_crew = "title.crew.tsv"
title_crew_gz = title_crew + ".gz"

title_ratings = "title.ratings.tsv"
title_ratings_gz = title_ratings + ".gz"

# Created a list to store the file names
file_list = [artist_name, title_akas, title_basics, title_crew, title_ratings]

# Loops through the file list and then downloads each file
for title in file_list:
  url = f"https://datasets.imdbws.com/{title}.gz"
  r = requests.get(url,allow_redirects=True)

  open(f"{title}.gz",'wb').write(r.content)
  print(f"Written {title}.gz")

  with gzip.open(f"{title}.gz", 'rb') as f_in:
      with open(title, 'wb') as f_out:
          shutil.copyfileobj(f_in, f_out)
  print(f"Extracted {title} from {title}.gz")
  
  if os.path.exists(f"{title}.gz"):
    os.remove(f"{title}.gz")
    print(f"Removed {title}.gz")
  else:
    print("The file does not exist")