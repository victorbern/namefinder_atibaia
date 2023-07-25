from bs4 import BeautifulSoup

from urllib.request import Request, urlopen

req = Request('http://www.prefeituradeatibaia.com.br/imprensa/index.php?ano=2023', headers={'User-Agent': 'Mozila/5.0'})

html = urlopen(req)

soup = BeautifulSoup(html, 'html.parser')
pdfLinks = []
for i in soup.find_all(class_ = 'modal'):
    links = i.find(class_='modal-content').table.find_all('a', href=True)
    for link in links:
        
        if (link != []):
            pdfLinks.append(link['href'])

url = 'http://www.prefeituradeatibaia.com.br/imprensa/'
i = 0

documento = urlopen(url+pdfLinks[0]).read().decode('utf-8')
print(documento)

# for doc in pdfs:
#     i+=1
#     documentoLido = urlopen(url+doc)
#     pdf = open("pdf"+str(i)+".pdf", 'wb')
#     pdf.write(documentoLido.read())
#     pdf.close()


# pdf = open("pdf"+str(i)+".pdf", 'wb') 
        
#         pdf.close() 
# print (pdfs)