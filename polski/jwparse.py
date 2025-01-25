# to parse daily text to list of versiculos
import requests

tab =[]
l =1
for x in range(12):
    print("Loading: "+str(round(100*l/12))+" % " + "*"*l,end='\r')
    l+=1

    if x<10:
        link = "https://wol.jw.org/pl/wol/d/r12/lp-p/110202520"+str(x)
    else:
        link = "https://wol.jw.org/pl/wol/d/r12/lp-p/11020252"+str(x)

    f = requests.get(link)
    source = f.text
   
    for i in range(3,96,3):

        poz = source.find("""<p id="p""" +str(i))
        if poz == -1 : break
        poz2 = source.find("<em>",poz)+4
        poz3 = source.find("</em>",poz2)
        poz4 = source.find("<em>",poz3)+4
        poz5 = source.find("</em>",poz4)

        res = source[poz2:poz3]+source[poz4:poz5]+")."
        tab.append(res)

print(tab)