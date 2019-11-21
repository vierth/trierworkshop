# this basic script will remove markup from documents
from bs4 import BeautifulSoup
import os

sourcefolder = "corpus"
savefolder = "nohtml"

if not os.path.isdir(savefolder):
    os.mkdir(savefolder)

for root, dirs, files in os.walk(sourcefolder):
    for filename in files:
        with open(os.path.join(root, filename), "r", encoding="utf8", errors="ignore") as rf:
            html = rf.read()
        
        text = BeautifulSoup(html, "lxml").text

        newfilename = filename[:filename.rfind(".")]+".txt"
        with open(os.path.join(savefolder, newfilename), "w", encoding="utf8", errors="ignore") as wf:
            wf.write(text)