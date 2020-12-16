# usage: python3 night.py 1/0


import json
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("set_filename", help="set file name")
parser.add_argument("set_nightoverlay_opacity", help="set opacity of nightoverlay layer")
args = parser.parse_args()

with open(args.set_filename) as infile:
    mapdata = json.load(infile)

for layer in mapdata['layers']:
    if layer['name'] == 'Nightoverlay':
        layer['opacity'] = int(args.set_nightoverlay_opacity)
        break

with open(args.set_filename, 'w') as outfile:
    outfile.write(json.dumps(mapdata))
