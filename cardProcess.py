import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import requests

df = pd.read_csv("frameCSV.csv")

fontID = ImageFont.truetype("fonts/Megatron.ttf", size=45)
fontName = ImageFont.truetype("fonts/EBGaramond-SemiBold.ttf", size=40)

records = df.to_dict(orient='record')


def generate_card(data):
    template = Image.open("template.png")
    urlDrive = format(data['Upload Your decent Photo'])
    updateUrl = urlDrive.split("=")
    file_id = updateUrl[1]
    url = 'https://drive.google.com/uc?export=view&id='+file_id
    r = requests.get(url, allow_redirects=True)
    ext = r.headers['content-type'].split('/')[-1]
    open(f"photos/{data['Student ID']}"+"."+ext, 'wb').write(r.content)
    pic = Image.open(
        f"photos/{data['Student ID']}"+"."+ext).resize((597, 502), Image.ANTIALIAS)

    template.paste(pic, (190, 209, 787, 711))
    draw = ImageDraw.Draw(template)
    draw.text((280, 730), data['Name'], font=fontName, fill=(0, 0, 0))
    draw.text((350, 780), str(data['Student ID']), font=fontID, fill=(0, 0, 0))
    return template


for record in records:
    card = generate_card(record)
    card.save(f"cards/{record['Student ID']}.png")
