import requests, time
from bs4 import BeautifulSoup

def getbyRelation(relationID):
    print(relationID)
    requestUrl = "https://www.openstreetmap.org/relation/" + str(relationID)
    session = requests.session()
    code = session.get(requestUrl)

    plain = code.text
    s = BeautifulSoup(plain, "html.parser")
    data =""

    tr = s.find('a', text="de:amtlicher_gemeindeschluessel").parent.parent
    data = tr.find('td').text
    # for paragraph in s.findAll('tr', {'class':'sp-m-zugehoerigePdfFormulare'}):
    #     if ():

    #         data = str(paragraph.previousSibling).strip()
    return data

relations = [62428, 62429, 62430]
OSM_dict = {} 
for ID in relations:
    schluessel = getbyRelation(ID)
    OSM_dict[ID] = schluessel
    time.sleep(0.5)
print(OSM_dict)