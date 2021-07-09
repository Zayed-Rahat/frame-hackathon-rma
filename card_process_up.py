import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import requests

df = pd.read_csv("frameCSV.csv")

fontID = ImageFont.truetype("fonts/Megatron.ttf", size=65)
fontName = ImageFont.truetype("fonts/EBGaramond-SemiBold.ttf", size=75)

records = df.to_dict(orient='record')


def generate_card(data):
    template = Image.open("Template-Empty.png")

    urlDrive = format(data['Upload Your decent Photo'])
    updateUrl = urlDrive.split("=")
    file_id = updateUrl[1]
    url = 'https://drive.google.com/uc?export=view&id='+file_id
    r = requests.get(url, allow_redirects=True)
    ext = r.headers['content-type'].split('/')[-1]
    open(f"photos1/{data['Student ID']}"+"."+ext, 'wb').write(r.content)

    pic_resize = Image.open(
        f"photos1/{data['Student ID']}"+".jpeg").resize((1250, 1230), Image.ANTIALIAS)

    pic_up = Image.new("L", pic_resize.size, 0)
    draw = ImageDraw.Draw(pic_up)
    draw.ellipse((50, 50, 1200, 1200), fill=255)

    temp_up = template.copy()
    temp_up.paste(pic_resize, (690, 85), pic_up)

    draw = ImageDraw.Draw(temp_up)

    draw.text((125, 1630), data['Name'],
              font=fontName, fill=(255, 255, 255))
    draw.text((130, 1720), str(data['Student ID']),
              font=fontID, fill=(255, 255, 255))
    return temp_up


for record in records:
    card = generate_card(record)
    card.save(f"cards/{record['Student ID']}.png")
