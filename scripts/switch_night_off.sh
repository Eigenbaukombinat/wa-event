git pull
cd maps
python3 ../scripts/night.py ebk_garden.json 0
cd ..
git add .
git commit -m "switch night off"
git push
