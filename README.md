# scrape_interfacelift

Script for downloading wallpapers from InterfaceLIFT.

## Introduction

Inspired by [this repository](https://github.com/stevenbenner/interfacelift-downloader/), (although it didn't work so well for me), as I can't put it in better words:
```
It takes way too long to download all of the great images in InterfaceLIFT's wallpaper collection by hand, and I'm too
much of a cheap bastard to pay them for the privilege of using their bulk download service. So here is the leechers
way of grabbing all of their wallpapers quickly, easily, and for free.
```

## Requirements

* Python >= 3.4. I use `pathlib`.
* `requests`. Use `pip install requests` or `conda install requests`

## Usage

`python scrape_interfacelift.py [-h] [-o OUT_FOLDER] [-s START_PAGE] resolution`

* **resolution** is the resolution you want to download. Check [InterfaceLIFT](interfacelift.com) for available resolutions.
* **OUT_FOLDER** is where the folder (relative or absolute) where you want to store the images. Default is "Wallpapers"
* If your download gets interrupted, set **START_PAGE** as the number of the last page you were downloading to resume from there.
* **-h** displays the argparse help. 
