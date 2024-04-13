def new_Structure(names,goals,goals_avoided,assists,dictionary):
    name_list= names.split(", ")
    for player in range(len(name_list)):
        stats=[goals[player],goals_avoided[player],assists[player]]
        dictionary[name_list[player]]=stats
        print(dictionary)
#En el inciso B yo puedo destacar 2 casos pq no se especifica muy bien a q se refiere:
#Por ejemplo, en el 1, podria ser de buscar a un jugador
# que ya existe y devolver la cantidad de goles.
#En el 2, podria buscarse al jugador q metió mas goles en el equipo.
def get_Player1(names_list,name):
    player=name.lower()
    aux="El jugador ",name," ha metido un total de ",names_list[player][0]," goles."
    return aux