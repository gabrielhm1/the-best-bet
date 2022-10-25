 from bs4 import BeautifulSoup
import requests
partidas = []

with open(r"C:\Users\caio2\Downloads\sportingbet.html", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
    
    for index,item in enumerate(soup.find_all("div", class_="participants-pair-game")):
        print("partida", index)
        odds = {}
        dados = {
            #"time1":"nome_time1",
            #"time2":"nome_time2",
            #"odd_mandante":123
            #"odd_empate":123
            #"odd_visitante":123
        }
        times = item.find_all("div", class_="participant")
        dados["host_team"] = times[0].text
        dados["away_team"] = times[1].text
        
        
        for index_odd,odd in enumerate(soup.find_all("div", class_="option option-value ng-star-inserted")):
            print(index_odd,odd.text)
            if index_odd%3 == 0:
                odds["host_win"] = odd.text
            elif index_odd%3 == 1:
                odds["match_draw"] = odd.text
            elif index_odd%3 == 2:
                odds["away_win"] = odd.text
                break
            odds['company'] = 'sportingbet'
            odd_dict = {'odds':odds}
            match_info = dict(dados, **odd_dict)
        print(dados)
        partidas.append(match_info)
        
for partida in partidas:
    rqs = requests.post('http://localhost:5000/match', json=partida)
    print(rqs.text)