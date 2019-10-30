#!/bin/bash

echo "GIT SCRIPT"
cd Docs
echo "In Docs"
mv This.jpg Diagram.jpg
cd ..
echo "Not In Docs"
git add .
git commit -m "Git Script Commit 1"
git pull origin Library
git push origin Library
echo "Done?"