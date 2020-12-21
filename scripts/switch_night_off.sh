git pull
for x in `ls *.json`; do
        echo $x;
        python3 ./scripts/night.py $x 0;
done
cd maps
for x in `ls *.json`; do
	echo $x;
	python3 ../scripts/night.py $x 0;
done
cd ..
git add .
git commit -m "switch night off"
git push
