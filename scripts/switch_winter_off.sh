git pull
for x in `ls *.json`; do
        echo $x;
        python3 ./scripts/winter.py $x 0;
done
cd maps
for x in `ls *.json`; do
	echo $x;
	python3 ../scripts/winter.py $x 0;
done
cd ..
git add .
git commit -m "switch winter off"
git push
