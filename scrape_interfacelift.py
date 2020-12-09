import argparse
from pathlib import Path
import requests
import re
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


ap = argparse.ArgumentParser()
ap.add_argument("resolution", help="Wallpapers resolution")
ap.add_argument("-o", "--out-folder", default="Wallpapers",
                help="Folder to store wallpapers at")
ap.add_argument("-s", "--start-page", type=int, default=1,
                help="Page number to start downloading (useful for resuming download)")

args = ap.parse_args()

out_folder = Path(args.out_folder)
out_folder.mkdir(exist_ok=True)
url_root = "https://interfacelift.com/wallpaper/downloads/date/any/" + args.resolution + "/index"
re_pattern = '/wallpaper/[a-zA-Z0-9]+/[a-zA-Z0-9_]+_' + args.resolution + '.jpg'

i = args.start_page
while True:
    cur_url = url_root + str(i) + ".html"
    page = requests.get(cur_url, verify=False)
    images = re.findall(re_pattern, str(page.content))
    if len(images) == 0:
        break
    print(f"Found {len(images)} images in page {i}.")
    for img in images:
        img_url = "https://interfacelift.com" + img
        img_name =  img.split("/")[-1]
        print(f"Downloading {img_name}")
        img_data = requests.get(img_url, verify=False)
        with open(out_folder / img_name, 'wb') as f:
            f.write(img_data.content)
    i += 1
print("Finished downloading images.")
