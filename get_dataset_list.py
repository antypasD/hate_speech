import re
import pandas as pd
from collections import defaultdict
from bs4 import BeautifulSoup

# 850 h3 instead of h4
# 1510 double Platform
data = defaultdict(lambda: [])

with open("text.html") as f:
    lines = f.readlines()


html_doc = "\n".join(lines)

soup = BeautifulSoup(html_doc, 'html.parser')

# title 
for title in soup.find_all('h4'):
    clean_title = title.get_text()
    clean_title = clean_title.replace("\n", " ").strip(" ")

    data['name'].append(clean_title)


for group in soup.find_all('ul'):
    for li in group.findAll("li"):
        text = li.get_text()
        if "Link to publication:" in text:
            text = text.replace("Link to publication::", "")
            data['pub'].append(text)
        if "Link to data:" in text:
            text = text.replace("Link to data:", "")
            data['data'].append(text)
        if "Task description:" in text:
            text = text.replace("Task description:", "")
            data['desc'].append(text)
        if "Details of task:" in text:
            text = text.replace("Details of task:", "")
            data['details'].append(text)
        if "Size of dataset:" in text:
            text = text.replace("Size of dataset:", "").replace(" ","").replace(",", "")
            data['size'].append(text)
        if "Percentage abusive:" in text:
            text = text.replace("Percentage abusive:", "").strip("%")
            data['percentage'].append(text)
        if  re.search("^Language:", text):
            text = text.replace("Language:", "")
            data['language'].append(text)
        if "Level of annotation:" in text:
            text = text.replace("Level of annotation:", "")
            data['annotation'].append(text)
        if "Platform:" in text:
            text = text.replace("Platform:", "")
            data['platform'].append(text)
        if "Medium:" in text:
            text = text.replace("Medium:", "")
            data['medium'].append(text)
        if "Reference:" in text:
            text = text.replace("Reference:", "")
            data['ref'].append(text)


df = pd.DataFrame(data)
df.to_csv('test.csv', index=False)