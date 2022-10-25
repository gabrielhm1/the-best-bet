from bs4 import BeautifulSoup

#cria uma lista das partidas
partidas = []

with open(r"C:\Users\trica\Downloads\bet.html", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
    
    for index,item in enumerate(soup.find_all("div", class_="rcl-ParticipantFixtureDetailsAggregateScore")):
        print("partida", index)
        dados = {
            #"time1":"nome_time1",
            #"time2":"nome_time2",
            #"odd_mandante":123
            #"odd_empate":123
            #"odd_visitante":123
        }
        times = item.find_all("div", class_="rcl-ParticipantFixtureDetailsTeam")
        dados["host_team"] = times[0].text
        dados["away_team"] = times[1].text
        
        odds = {}
        for index_odd,odd in enumerate(soup.find_all("div", class_="sgl-MarketOddsExpand")):
            odd_valor = odd.find_all("span", class_="sgl-ParticipantOddsOnly80_Odds")
            
            if index_odd == 0:
                odds["host_win"] = odd_valor[index].text
            elif index_odd == 1:
                odds["match_draw"] = odd_valor[index].text
            elif index_odd == 2:
                odds["away_win"] = odd_valor[index].text
            
        
            odds['company'] = 'bet365'

            odd_dict = {'odds':{**odds}}
            match_info = dict(dados, **odd_dict)
        partidas.append(match_info)

print(partidas)
        
