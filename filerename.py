# this is a quick script that you can use to rename the files in a folder
import os

for root, dirs, files in os.walk("forrenaming"):
    for filename in files:
        newname = "test_" + filename
        os.rename(os.path.join(root, filename), os.path.join(root, newname))
