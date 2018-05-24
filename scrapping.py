from urllib.request import urlopen
from bs4 import BeautifulSoup
import sys, json

links = [
    'https://pharmnet-dz.com/alphabet.aspx?char=A',
    'https://pharmnet-dz.com/alphabet.aspx?char=B',
    'https://pharmnet-dz.com/alphabet.aspx?char=C',
    'https://pharmnet-dz.com/alphabet.aspx?char=D',
    'https://pharmnet-dz.com/alphabet.aspx?char=E',
    'https://pharmnet-dz.com/alphabet.aspx?char=F',
    'https://pharmnet-dz.com/alphabet.aspx?char=G',
    'https://pharmnet-dz.com/alphabet.aspx?char=H',
    'https://pharmnet-dz.com/alphabet.aspx?char=I',
    'https://pharmnet-dz.com/alphabet.aspx?char=J',
    'https://pharmnet-dz.com/alphabet.aspx?char=K',
    'https://pharmnet-dz.com/alphabet.aspx?char=L',
    'https://pharmnet-dz.com/alphabet.aspx?char=M',
    'https://pharmnet-dz.com/alphabet.aspx?char=N',
    'https://pharmnet-dz.com/alphabet.aspx?char=O',
    'https://pharmnet-dz.com/alphabet.aspx?char=P',
    'https://pharmnet-dz.com/alphabet.aspx?char=Q',
    'https://pharmnet-dz.com/alphabet.aspx?char=R',
    'https://pharmnet-dz.com/alphabet.aspx?char=S',
    'https://pharmnet-dz.com/alphabet.aspx?char=T',
    'https://pharmnet-dz.com/alphabet.aspx?char=U',
    'https://pharmnet-dz.com/alphabet.aspx?char=V',
    'https://pharmnet-dz.com/alphabet.aspx?char=W',
    'https://pharmnet-dz.com/alphabet.aspx?char=X',
    'https://pharmnet-dz.com/alphabet.aspx?char=Y',
    'https://pharmnet-dz.com/alphabet.aspx?char=Z',
]


meds = {}
nb_total_meds = 0
print('------------------------------')
## going through letters
for index, link in enumerate(links):
    print('letter ' + str(link[-1]))
    char_page = urlopen(link)
    soup = BeautifulSoup(char_page, "html5lib")
    nb_pages = len(soup.find_all('a', class_ ="btn btn-xs btn-warning")) + len(soup.find_all('a', class_ ="btn btn-danger"))
    meds[link[-1]] = []
    
    ## going through pages
    for i in range(1, nb_pages + 1):
        print('\rPage ' + str(i), end='')
        page_to_scrap = BeautifulSoup(urlopen(link + '&p=' + str(i)), "html5lib")
        all_meds = page_to_scrap.find_all(attrs={'scope':'row'})

        ## going through drugs
        for y, med in enumerate(all_meds):
            med_link = med.find_all('a')[0]['href']
            meds[link[-1]] += [med_link]

    nb_meds = len(meds[link[-1]])
    nb_total_meds += nb_meds
    print("\rnumber of meds : {}".format(nb_meds), "\n-------------------------------------")


with open('result.json', 'w') as fp:
    json.dump(meds, fp)