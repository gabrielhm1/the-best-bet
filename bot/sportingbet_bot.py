from bs4 import BeautifulSoup
import requests
partidas = []

with open(r"C:\Users\caio2\Downloads\sportingbet.html", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
    for index,item in enumerate(soup.find_all("div", class_="grid-event-wrapper")):
        print("partida", index)
        dados = {
            #"team1":"name_team1",
            #"team2":"name_team2",
            #"odd_host":123
            #"odd_draw":123
            #"odd_away":123
        }
        times = item.find_all("div", class_="participant")
        dados["host_team"] = times[0].text.replace(" ","").replace("PaísdeWales", "Wales").replace("Gales", "Wales").replace("Holanda", "Netherlands").replace("Inglaterra", "England").replace("Brasil", "Brazil").replace("Sérvia", "Serbia").replace("PaísdeGales", "Wales").replace("PaísesBaixos", "Netherlands").replace("Equador", "Equator").replace("Tunísia", "Tunisia").replace("Austrália", "Australia").replace("Polônia", "Poland").replace("ArábiaSaudita", "Saudi Arabia").replace("França", "France").replace("Dinamarca", "Denmark").replace("México", "Mexico").replace("Japão", "Japan").replace("CostaRica", "Costa Rica").replace("Bélgica", "Belgium").replace("Marrocos", "Morocco").replace("Croácia", "Croatia").replace("Canadá", "Canada").replace("Espanha", "Spain").replace("Alemanha", "Germany").replace("Camarões", "Cameroon").replace("CoreiadoSul", "South Korea").replace("Gana", "Ghana").replace("Suíça", "Switzerland").replace("Uruguai", "Uruguay").replace("EUA", "USA").replace("EstadosUnidos", "USA").replace("Irã", "Iran").replace("Catar", "Qatar").replace("CoréiadoSul", "South Korea").replace("Croácia", "Croatia")
        dados["away_team"] = times[1].text.replace(" ","").replace("PaísdeWales", "Wales").replace("Gales", "Wales").replace("Holanda", "Netherlands").replace("Inglaterra", "England").replace("Brasil", "Brazil").replace("Sérvia", "Serbia").replace("PaísdeGales", "Wales").replace("PaísesBaixos", "Netherlands").replace("Equador", "Equator").replace("Tunísia", "Tunisia").replace("Austrália", "Australia").replace("Polônia", "Poland").replace("ArábiaSaudita", "Saudi Arabia").replace("França", "France").replace("Dinamarca", "Denmark").replace("México", "Mexico").replace("Japão", "Japan").replace("CostaRica", "Costa Rica").replace("Bélgica", "Belgium").replace("Marrocos", "Morocco").replace("Croácia", "Croatia").replace("Canadá", "Canada").replace("Espanha", "Spain").replace("Alemanha", "Germany").replace("Camarões", "Cameroon").replace("CoreiadoSul", "South Korea").replace("Gana", "Ghana").replace("Suíça", "Switzerland").replace("Uruguai", "Uruguay").replace("EUA", "USA").replace("EstadosUnidos", "USA").replace("Irã", "Iran").replace("Catar", "Qatar").replace("CoréiadoSul", "South Korea").replace("Croácia", "Croatia")
        odds = {}
        for index_odd,odd in enumerate(item.find_all("div", class_="option option-value ng-star-inserted")):
            print(index_odd,odd.text)
            if index_odd == 0:
                odds["host_win"] = odd.text
            elif index_odd == 1:
                odds["match_draw"] = odd.text
            elif index_odd == 2:
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
    