
echo "[INFO] Updating requirements.txt..."
pip freeze > requirements.txt
echo "[INFO] Successfully updated requirements.txt."

echo "[INFO] Generating docs resources..."
python3 tool.py example
echo "[INFO] Successfully generated resources."

echo "[INFO] Assembly README.md..."
cat res/*.part > README.md
echo "[INFO] README.md is ready."
