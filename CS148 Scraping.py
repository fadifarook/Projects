import requests
from bs4 import BeautifulSoup
import pdfkit
import time
path_wkhtmltopdf = r'C:\Users\badas\AppData\Local\Programs\Python\Python310' \
                   r'\wkhtmltopdf\bin\wkhtmltopdf.exe '
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
#pdfkit.from_url("https://www.teach.cs.toronto.edu/~csc148h/winter/notes/python-recap/memory_model_part2.html", r"CSC148 Notes\out.pdf", configuration=config)

r = requests.get('https://www.teach.cs.toronto.edu/~csc148h/winter/notes')
print(r.status_code)

soup = BeautifulSoup(r.text, 'html.parser')
link_list = []
link_names = []
for link in soup.find_all('a'):
    link_names.append(link.string)
    link_list.append(str(link.get('href')))

link_list.pop()
link_names.pop()
print(link_names)
to_remove = 0
for i in range(len(link_names)):
    if link_names[i] is None:
        to_remove = i
        continue
    link_names[i] = link_names[i].replace(':', '')
link_names[to_remove] = ''
print(link_names)
# how do we get the link from the html

for i in range(len(link_list)):
    link_list[i] = 'https://www.teach.cs.toronto.edu/~csc148h/winter/notes/' + \
                   link_list[i]

#print(link_list)

for i in range(len(link_list)):
    name = link_names[i]+'.pdf'
    print(name)

    try:
        pdfkit.from_url(link_list[i], f'CSC148 Notes/{name}', configuration=config)
    except:
        time.sleep(0.01)






