# usage: python3 winter.py 1/0


import json
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("set_filename", help="set file name")
parser.add_argument("set_winteroverlay_opacity", help="set opacity of winteroverlay layer")
args = parser.parse_args()

with open(args.set_filename) as infile:
    mapdata = json.load(infile)

for layer in mapdata['layers']:
    if layer['name'] == 'Winterwonderland_bottom':
        layer['opacity'] = float(args.set_winteroverlay_opacity)
        break

for layer in mapdata['layers']:
    if layer['name'] == 'Winterwonderland_overlay':
        layer['opacity'] = float(args.set_winteroverlay_opacity)
        break

with open(args.set_filename, 'w') as outfile:
    outfile.write(json.dumps(mapdata))
