#!/bin/bash
# ============================================================
# One-click deploy for the Aligned KPIs marketing website.
# Double-click this file in Finder (or run: bash deploy.command).
# It commits your current files and publishes them to GitHub Pages.
# ============================================================

cd "/Users/johnmuller/Documents/Claude/Projects/Marketing Website" || {
  echo "Could not find the website folder."; read -r -p "Press Enter to close."; exit 1;
}

echo "──────────────────────────────────────────────"
echo "  Deploying the Aligned KPIs website"
echo "──────────────────────────────────────────────"

# 1. Clear stale git lock files (the recurring gotcha on this synced folder)
find .git -name '*.lock' -delete 2>/dev/null

# 1b. Auto-bump the site version (shown subtly in the footer so you can confirm the live build)
VERSION_FILE="version.json"
NEW=""
if [ -f "$VERSION_FILE" ]; then
  CUR=$(grep -oE '[0-9]+\.[0-9]+' "$VERSION_FILE" | head -1)
  [ -z "$CUR" ] && CUR="0.00"
  NEW=$(awk -v v="$CUR" 'BEGIN{printf "%.2f", v+0.01}')
  printf '{ "version": "%s" }\n' "$NEW" > "$VERSION_FILE"
  echo "Version bumped: $CUR -> $NEW"
fi

# 2. Stage every change
git add -A

# 3. Ask for a short description
read -r -p "Describe this update (or just press Enter): " MSG
MSG="${MSG:-Update site}"
[ -n "$NEW" ] && MSG="v${NEW}: ${MSG}"

# 4. Commit (fine if there's nothing new)
git commit -m "$MSG" || echo "(no new changes to commit — will still sync/publish)"

# 5. Pull anything that changed on GitHub, then publish
echo "Syncing with GitHub..."
if ! git pull --rebase origin main; then
  echo ""
  echo "⚠️  Sync hit a snag. Copy everything above and send it to Claude."
  read -r -p "Press Enter to close."; exit 1
fi

if git push origin main; then
  echo ""
  echo "✅  Done! The site will be live in about a minute."
  [ -n "$NEW" ] && echo "    Live footer will read: Website v$NEW"
else
  echo ""
  echo "⚠️  Publish failed. Copy everything above and send it to Claude."
fi

read -r -p "Press Enter to close this window."
