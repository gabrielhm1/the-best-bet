with open(r"betano.html", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
    
    aux = len(soup.find_all("tr", class_="events-list_grid_event"))
    for index,item in enumerate(soup.find_all("tr", class_="events-list_grid_event")):
        dados = {
            #"time1":"nome_time1",
            #"time2":"nome_time2",
            #"odd_mandante":123
            #"odd_empate":123
            #"odd_visitante":123
        }
        times = item.find_all("span", class_="events-list_gridinfomainparticipants_participant-name")
        dados["mandante"] = times[0].text.replace("\n", "").replace(" ", "").replace("SãoPaulo", "São Paulo")
        dados["visitante"] = times[1].text.replace("\n", "").replace(" ", "").replace("SãoPaulo", "São Paulo")
        
        aux = len(soup.find_all("div", class_="selections"))

        seletor = soup.find_all("div", class_="selections")
        for index_odd,odd in enumerate(seletor[index].find_all("span", class_="selections_selection_odd")):       
            if index_odd == 0:
                dados["odd_mandante"] = odd.text.replace("\n", "").replace(" ", "")
            elif index_odd == 1:
                dados["odd_empate"] = odd.text.replace("\n", "").replace(" ", "")
            elif index_odd == 2:
                dados["odd_visitante"] = odd.text.replace("\n", "").replace(" ", "")
        partidas.append(dados)