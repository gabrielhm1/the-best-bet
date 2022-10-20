from bs4 import BeautifulSoup

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
        dados["mandante"] = times[0].text
        dados["visitante"] = times[1].text
        
        for index_odd,odd in enumerate(soup.find_all("div", class_="sgl-MarketOddsExpand")):
            print("odd", index_odd)
            odd_valor = odd.find_all("span", class_="sgl-ParticipantOddsOnly80_Odds")
        
            if index_odd == 0:
                dados["odd_mandante"] = odd_valor[index].text
            elif index_odd == 1:
                dados["odd_empate"] = odd_valor[index].text
            elif index_odd == 2:
                dados["odd_visitante"] = odd_valor[index].text
        partidas.append(dados)

print(partidas)
        
