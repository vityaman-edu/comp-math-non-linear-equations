
echo "[INFO] Updating requirements.txt..."

pip freeze > requirements.txt

echo "[INFO] Successfully updated requirements.txt..."

echo "[INFO] Updating res/plot.png..."

python3 eq/plot.py

echo "[INFO] Successfully updated res/plot.png..."
