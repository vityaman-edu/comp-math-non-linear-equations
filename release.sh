
echo "[INFO] Starting release..."

echo "[INFO] Updating res/plot.png..."
python3 eq/plot.py
echo "[INFO] Successfully updated res/plot.png..."

echo "[INFO] Release content:"
git status

echo "[INFO] Press any key to start release..."
read -n 1

git add -A
git commit -m "[release] 1-2 done"
git push

echo "[DONE] Successfully released new version"
