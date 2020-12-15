import json
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("set_nightoverlay_opacity", help="set opacity of nightoverlay layer")
args = parser.parse_args()

with open('ebk_garden.json') as infile:
    mapdata = json.load(infile)

for layer in mapdata['layers']:
    if layer['name'] == 'Nightoverlay':
        layer['opacity'] = int(args.set_nightoverlay_opacity)

with open('ebk_garden.json', 'w') as outfile:
    outfile.write(json.dumps(mapdata))
