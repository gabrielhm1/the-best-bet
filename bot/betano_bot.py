from bs4 import BeautifulSoup
import requests
partidas = []

with open(r"C:\Users\caio2\Downloads\betano.html", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
    
    aux = len(soup.find_all("tr", class_="events-list__grid__event"))
    for index,item in enumerate(soup.find_all("tr", class_="events-list__grid__event")):
        dados = {
            #"time1":"nome_time1",
            #"time2":"nome_time2",
            #"odd_mandante":123
            #"odd_empate":123
            #"odd_visitante":123
        }
        times = item.find_all("span", class_="events-list__grid__info__main__participants__participant-name")
        dados["host_team"] = times[0].text.replace("\n", "").replace(" ", "").replace("SãoPaulo", "São Paulo").replace("Botafogo-RJ", "Botafogo").replace("RBBragantino", "Bragantino").replace("Juventude-RS", "Juventude")
        dados["away_team"] = times[1].text.replace("\n", "").replace(" ", "").replace("SãoPaulo", "São Paulo").replace("Botafogo-RJ", "Botafogo").replace("RBBragantino", "Bragantino").replace("Juventude-RS", "Juventude")
        aux = len(soup.find_all("div", class_="selections"))
        
        odds = {}
        seletor = soup.find_all("div", class_="selections")
        for index_odd,odd in enumerate(seletor[index].find_all("span", class_="selections__selection__odd")):       
            if index_odd == 0:
                odds["host_win"] = odd.text.replace("\n", "").replace(" ", "")
            elif index_odd == 1:
                odds["match_draw"] = odd.text.replace("\n", "").replace(" ", "")
            elif index_odd == 2:
                odds["away_win"] = odd.text.replace("\n", "").replace(" ", "")
                
            odds['company'] = 'betano'
            
            odd_dict = {'odds':odds}
            match_info = dict(dados, **odd_dict)

        partidas.append(match_info)
        
for partida in partidas:
    print(partida)
    rqs = requests.post('http://localhost:5000/match', json=partida)
    print(rqs.text)
    