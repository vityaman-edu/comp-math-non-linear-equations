
echo "[INFO] Starting release..."

echo "[INFO] Starting update..."
bash ci/update.sh
echo "[INFO] Successfully updated everything..."

echo "[INFO] Release content:"
git status

echo "[INFO] Press any key to start release..."
read -n 1

git add -A
git commit -m "[release] plots for parsed functions"
git push

echo "[DONE] Successfully released new version"
