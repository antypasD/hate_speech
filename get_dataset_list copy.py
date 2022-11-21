import re
import pandas as pd
from collections import defaultdict

with open("text.html") as f:
    lines = f.readlines()


corpus = " ".join(lines)

results = defaultdict(lambda: [])



for idx, line in enumerate(lines):
    if "<ul>" in line:
        if "</h4>" not in lines[idx-1]:
            print(idx, line)
        
    if "Link to publication:" in line:
        try:
            temp = re.findall("<a href=\"(.*)\">", line)[0]
        except:
            try:
                temp = re.findall("href=\"(.*)\">", lines[idx+1])[0]
            except:
                temp = None
            
        results["pub"].append(temp)

    if "Link to data:" in line:
        try:
            temp = re.findall("<a href=\"(.*)\">", line)[0]
        except:
            try:
                temp = re.findall("href=\"(.*)\">", lines[idx+1])[0]
            except:
                temp = None

        results["data"].append(temp)

    if "Task description:" in line:
        try:
            if "</li>" in line:
                temp = re.findall("Task description:(.*)</li>", line)[0]
            else:
                temp = re.findall("Task description:(.*)", line)[0]

        except:
            temp = None
        results['desc'].append(temp)

    if "<li>Language:" in line:
        temp = re.findall("Language:(.*)</li>", line)[0]

        results['lang'].append(temp)


df = pd.DataFrame(results)
