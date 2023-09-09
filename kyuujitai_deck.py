import json
import os
import html

with open("kyujitai.json") as f:
    data: dict[str, list[str]] = json.load(f)

for shinjitai, kyujitai_list in data.items():
    images = [f'{ord(html.unescape(kanji)):#0{7}x}.svg'[2:] for kanji in kyujitai_list]
    print(shinjitai, "<br>".join(kyujitai_list), "<br>".join(f'<img src="{image}">' for image in images if os.path.exists("kanji/" + image)), sep="\t")