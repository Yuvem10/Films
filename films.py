import unidecode
import requests
from bs4 import BeautifulSoup


# Definition of varaibles
url = 'https://www.allocine.fr/film/agenda/'
res = requests.get(url)


# Connexion control 
if res.ok:


    # Definition of varaibles
    soup = BeautifulSoup(res.text, "html.parser")
    infos = soup.findAll("div", {"class":"meta-body-item meta-body-info"})
    titleFunction = soup.findAll("div", {'class':'card entity-card entity-card-list cf'})
    lstSpan = []
    lstTitle = []


    
    
    


    # add all span class in the list
    for info in infos:
        function = info.findAll('span')
        lstSpan.append(function)


    # add all a in list for write properly in console 
    for title in titleFunction:
        function = title.find('a')
        lstTitle.append(function)
    

    # control if there are several genres
    for i in range(len(infos)):
        
        if len(lstSpan[i]) == 4:
            print(unidecode.unidecode(lstTitle[i].text)+" | "+unidecode.unidecode(lstSpan[i][2].text)+", "+unidecode.unidecode(lstSpan[i][3].text))
            

        elif len(lstSpan[i]) == 5:
            print(unidecode.unidecode(lstTitle[i].text)+" | "+unidecode.unidecode(lstSpan[i][2].text)+", "+unidecode.unidecode(lstSpan[i][3].text)+" "+unidecode.unidecode(lstSpan[i][4].text))
            
           
        elif len(lstSpan[i]) == 6:
            print(unidecode.unidecode(lstTitle[i].text)+" | "+unidecode.unidecode(lstSpan[i][2].text)+", "+unidecode.unidecode(lstSpan[i][3].text)+" "+unidecode.unidecode(lstSpan[i][4].text)+" "+unidecode.unidecode(lstSpan[i][5].text))
            
        
        else:
            print(unidecode.unidecode(lstTitle[i].text)+" | "+unidecode.unidecode(lstSpan[i][2].text))
            
        
else: 
    print("Il y a un probleme au niveau du serveur")

    
 
    
   
        
