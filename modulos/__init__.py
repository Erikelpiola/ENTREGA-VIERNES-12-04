
#Genera un estructura diccionario donde por cada nombre, se le asignan sus estadisticas
def new_Structure(names,goals,goals_avoided,assists,stats):
    name_list= names.split(", ")
    for player in range(len(name_list)):
        aux=[goals[player],goals_avoided[player],assists[player]]
        stats[name_list[player]]=aux

#En el inciso B yo puedo destacar 2 casos pq no se especifica muy bien a q se refiere:

#Por ejemplo, en el 1, podria ser de buscar a un jugador
#que ya existe y devolver la cantidad de goles.
def get_Player1(stats,name):
    player=name.lower()
    aux=f"El jugador {player} ha metido un total de {stats[player][0]} goles."
    return aux


#En el 2, podria buscarse al jugador q metió mas goles en el equipo.
def get_Player2(stats):
    max=-1
    max_player=""
    for player,stats in stats.items():
        goal= stats[0]
        if goal>max:
            max_player=player
            max=goal
    return max_player,max


def max_Influence(stats):
    #crea una dupla con nombre, data
    points = [(nombre,float (((data[0]*1.5) + (data[1]*1.25) + data[2]))) for nombre,data in stats.items()]
    #toma el valor x[1] para calcular el maximo jugador y [0] para retornar el mismo
    max_player=max(points, key= lambda x:(x[1]))
    return max_player[0]

#de cada nombre en el diccionario, suma los goles a favor de los mismos y devuelve el promedio.
def prom_Goals(stats):
    total_goals= sum(data[0] for data in stats.values())
    return total_goals/25

#Saco el promedio goles del jugador especifico
def goals_prom_Player1(name,stats):
    player=name.lower()
    return (stats[player][0]/25)

#Obtengo a la mayor goleador/a y su cantidad de goles para luego sacar el prom
def goals_prom_Player2(stats):
    max_player,max=get_Player2(stats)
    return max/25