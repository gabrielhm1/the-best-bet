from bs4 import BeautifulSoup
import requests

#criar uma lista das partidas
partidas = []

#obter html do site
with open(r"C:\Users\caio2\Downloads\bet.html", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
    
    #localizar os dados necessários através de classes identificadoras e formatar para obter a saída desejada
    for index,item in enumerate(soup.find_all("div", class_="rcl-ParticipantFixtureDetailsAggregateScore")):
        print("partida", index)
        dados = {
            #"time1":"nome_time1",
            #"time2":"nome_time2",
            #odds{
            #   "odd_mandante":123
            #   "odd_empate":123
            #   "odd_visitante":123
            #}
        }
        #encontrar os nomes dos times que vão se enfrentar
        times = item.find_all("div", class_="rcl-ParticipantFixtureDetailsTeam")
        dados["host_team"] = times[0].text.replace("\n", "").replace(" ", "").replace("SãoPaulo", "São Paulo").replace("CuiabáEC", "Cuiabá").replace("RBBragantino", "Bragantino").replace("AtléticoGoianiense", "Atlético-GO").replace("AthleticoParanaense", "Athletico-PR").replace("AméricaMineiro", "América-MG").replace("AtléticoMineiro", "Atlético-MG")
        dados["away_team"] = times[1].text.replace("\n", "").replace(" ", "").replace("SãoPaulo", "São Paulo").replace("CuiabáEC", "Cuiabá").replace("RBBragantino", "Bragantino").replace("AtléticoGoianiense", "Atlético-GO").replace("AthleticoParanaense", "Athletico-PR").replace("AméricaMineiro", "América-MG").replace("AtléticoMineiro", "Atlético-MG")
        
        #encontrar as odds para vitória de cada time e empate
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
        
        #adicionar cada partida no final da lista 'partidas'
        partidas.append(match_info)

#enviar os dados para a aplicação
for partida in partidas:
    print(partida)
    rqs = requests.post('http://localhost:5000/match', json=partida)
    print(rqs.text)