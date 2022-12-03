from bs4 import BeautifulSoup
import requests
partidas = []

with open(r"betano.html", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
    
    aux = len(soup.find_all("tr", class_="events-list__grid__event"))
    for index,item in enumerate(soup.find_all("tr", class_="events-list__grid__event")):
        dados = {
            #"team1":"name_team1",
            #"team2":"name_team2",
            #"odd_host":123
            #"odd_draw":123
            #"odd_away":123
        }
        times = item.find_all("span", class_="events-list__grid__info__main__participants__participant-name")
        dados["host_team"] = times[0].text.replace("\n", "").replace("PaísdeWales", "Wales").replace("Gales", "Wales").replace(" ", "").replace("Holanda", "Netherlands").replace("Inglaterra", "England").replace("Brasil", "Brazil").replace("Sérvia", "Serbia").replace("PaísdeGales", "Wales").replace("PaísesBaixos", "Netherlands").replace("Equador", "Equator").replace("Tunísia", "Tunisia").replace("Austrália", "Australia").replace("Polônia", "Poland").replace("ArábiaSaudita", "Saudi Arabia").replace("França", "France").replace("Dinamarca", "Denmark").replace("México", "Mexico").replace("Japão", "Japan").replace("CostaRica", "Costa Rica").replace("Bélgica", "Belgium").replace("Marrocos", "Morocco").replace("Croácia", "Croatia").replace("Canadá", "Canada").replace("Espanha", "Spain").replace("Alemanha", "Germany").replace("Camarões", "Cameroon").replace("CoreiadoSul", "South Korea").replace("Gana", "Ghana").replace("Suíça", "Switzerland").replace("Uruguai", "Uruguay").replace("EUA", "USA").replace("EstadosUnidos", "USA").replace("Irã", "Iran").replace("Catar", "Qatar").replace("CoréiadoSul", "South Korea").replace("Croácia", "Croatia")
        dados["away_team"] = times[1].text.replace("\n", "").replace("PaísdeWales", "Wales").replace("Gales", "Wales").replace(" ", "").replace("Holanda", "Netherlands").replace("Inglaterra", "England").replace("Brasil", "Brazil").replace("Sérvia", "Serbia").replace("PaísdeGales", "Wales").replace("PaísesBaixos", "Netherlands").replace("Equador", "Equator").replace("Tunísia", "Tunisia").replace("Austrália", "Australia").replace("Polônia", "Poland").replace("ArábiaSaudita", "Saudi Arabia").replace("França", "France").replace("Dinamarca", "Denmark").replace("México", "Mexico").replace("Japão", "Japan").replace("CostaRica", "Costa Rica").replace("Bélgica", "Belgium").replace("Marrocos", "Morocco").replace("Croácia", "Croatia").replace("Canadá", "Canada").replace("Espanha", "Spain").replace("Alemanha", "Germany").replace("Camarões", "Cameroon").replace("CoreiadoSul", "South Korea").replace("Gana", "Ghana").replace("Suíça", "Switzerland").replace("Uruguai", "Uruguay").replace("EUA", "USA").replace("EstadosUnidos", "USA").replace("Irã", "Iran").replace("Catar", "Qatar").replace("CoréiadoSul", "South Korea").replace("Croácia", "Croatia")
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
    