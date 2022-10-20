from bs4 import BeautifulSoup
partidas = []

with open(r"sportingbet.html", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
    
    for index,item in enumerate(soup.find_all("div", class_="participants-pair-game")):
        print("partida", index)
        dados = {
            #"time1":"nome_time1",
            #"time2":"nome_time2",
            #"odd_mandante":123
            #"odd_empate":123
            #"odd_visitante":123
        }
        times = item.find_all("div", class_="participant")
        dados["mandante"] = times[0].text
        dados["visitante"] = times[1].text
        
        
        for index_odd,odd in enumerate(soup.find_all("div", class_="option option-value ng-star-inserted")):
            print(index_odd,odd.text)
            if index_odd%3 == 0:
                dados["odd_mandante"] = odd.text
            elif index_odd%3 == 1:
                dados["odd_empate"] = odd.text
            elif index_odd%3 == 2:
                dados["odd_visitante"] = odd.text
                break
        print(dados)
        partidas.append(dados)

print(partidas)