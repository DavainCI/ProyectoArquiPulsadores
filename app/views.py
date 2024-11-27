from django.shortcuts import render

def leaderboard(request):
    jugadores = [
        {"posicion": "1°", "nombre": "ASTHRI", "puntuacion": 160},
        {"posicion": "2°", "nombre": "LEONARDO", "puntuacion": 10},
        {"posicion": "3°", "nombre": "CARLOS", "puntuacion": 300},
    ]
    
    # Ordenar por puntuación de mayor a menor
    jugadores_ordenados = sorted(jugadores, key=lambda x: x['puntuacion'], reverse=True)
    
    # Recalcular las posiciones
    for idx, jugador in enumerate(jugadores_ordenados):
        jugador['posicion'] = f"{idx + 1}°"
    
    sala = "0001"
    estado = "Jugando..."
    
    return render(request, 'leaderboard.html', {'jugadores': jugadores_ordenados, 'sala': sala, 'estado': estado})
