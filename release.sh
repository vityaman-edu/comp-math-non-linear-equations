
echo "Starting release..."

echo "Updating res/plot.png..."
python3 eq/plot.py
echo "Successfully updated res/plot.png..."

echo "Press any key to start release..."
read -n 1

git checkout trunk
git add -A
git commit -m "[release] 1-2 done"
git push

echo "Successfully released new version"
