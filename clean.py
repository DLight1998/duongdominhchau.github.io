#!/bin/python
import os
import shutil
keep = ["hugo", "TODO.md", ".git", "clean.py"]
toBeDeleted = set(os.listdir(".")) - set(keep)
toBeDeleted = sorted(toBeDeleted)

print(toBeDeleted)
run = input("Perform the cleanup? [Y/n] ").lower()
if run == "":
    run = "y"
if run != "y":
    exit(0)

for path in toBeDeleted:
    print("Deleting " + path)
    try:
        shutil.rmtree(path)
    except:
        os.remove(path)
