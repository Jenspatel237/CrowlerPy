# with open('persons.csv', 'wb') as csvfile:
        #     filewriter = csv.writer(csvfile, delimiter=',',
        #                             quotechar='|', quoting=csv.QUOTE_MINIMAL)
        #     filewriter.writerow(['Name', 'Profession'])
        #     filewriter.writerow(['Derek', 'Software Developer'])
        #     filewriter.writerow(['Steve', 'Software Developer'])
        #     filewriter.writerow(['Paul', 'Manager'])


import requests
from array import array
import csv
from array import *

from bs4 import BeautifulSoup
from requests import Session


# def parsePOSTstring(POSTstr):
#     paramList = POSTstr.split('&')
#     paramDict = dict([param.split('=') for param in paramList])
#     return paramDict
#
# headers={'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:27.0) Gecko/20100101 Firefox/27.0',
#      'Referer' : 'http://sportsbeta.ladbrokes.com/football'
#     }
#
# #prep the data (POSTstr copied from Firebug raw source)
# POSTstr = "moreId=156%23327&facetCount_156%23327=12&event=&N=4294966750&pageType=EventClass&pageId=p_football_home_page&type=ajaxrequest&eventIDNav=&removedSelectionNav=&currentSelectedId=&form-trigger=moreId"
# payload = parsePOSTstring(POSTstr)




def tread_spider():

    with open('names2016.csv', 'w', newline='') as f:

        id = 1223086
        thewriter = csv.writer(f)
        while id <= 1225364:
            array = []
            url = "https://old.mciindia.org/ViewDetails.aspx?ID=" + str(id)
            # s = Session()
            # s.get('http://sportsbeta.ladbrokes.com/football')
            # # now visit disired url with headers/data
            # r = s.post(url, data=payload, headers=headers)
            source_code = requests.get(url)
            plain_text = source_code.text
          #  plain_text = r.text
          #  print(plain_text)
            print("-------------------------------------------------------------------------------")
            id += 1
            soup = BeautifulSoup(plain_text)



            for link in soup.find_all('span', {'class' : 'label'}):
                href = link.string
                print(href)
                array.append(href)

            thewriter.writerow([array[0], array[1], array[2], array[3], array[4], array[5], array[6], array[7], array[8], array[9], array[10]])

tread_spider()
