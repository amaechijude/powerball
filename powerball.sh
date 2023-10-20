#!/bin/bash
echo "# powerball" >> README.md
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/amaechijude/powerball.git
git push -u origin main
