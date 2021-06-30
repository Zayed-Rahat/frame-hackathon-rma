import pandas as pd
from PIL import Image
import requests

df = pd.read_csv("frameCSV.csv")
records = df.to_dict(orient='record')


def generate_card(data):
    urlDrive = format(data['Upload Your decent Photo'])
    updateUrl = urlDrive.split("=")
    file_id = updateUrl[1]
    url = 'https://drive.google.com/uc?export=view&id='+file_id
    r = requests.get(url, allow_redirects=True)
    ext = r.headers['content-type'].split('/')[-1]
    open(f"photos/{data['Student ID']}"+"."+ext, 'wb').write(r.content)


for record in records:
    card = generate_card(record)
