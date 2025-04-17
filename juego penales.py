import random
import time

def mostrar_introduccion():
  """Displays the game introduction and rules."""
  print("************************************")
  print("* ¡Bienvenido a la Tanda de Penales! *")
  print("************************************")
  print("\nReglas:")
  print("- Tienes 5 intentos para meter más goles que la computadora.")
  print("- En cada intento, elige dónde patear: 'izquierda', 'centro' o 'derecha'.")
  print("- La computadora (arquero) elegirá dónde atajar.")
  print("- Si eliges un lugar diferente al arquero, ¡es GOL!")
  print("- Si eligen el mismo lugar, ¡atajó el arquero!")
  print("\n¡Mucha suerte!")
  print("------------------------------------\n")

def obtener_eleccion_jugador():
  """Gets and validates the player's shot choice."""
  opciones_validas = ['izquierda', 'centro', 'derecha']
  while True:
    eleccion = input("Elige dónde patear (izquierda, centro, derecha): ").lower().strip()
    if eleccion in opciones_validas:
      return eleccion
    else:
      print("Opción inválida. Por favor, escribe 'izquierda', 'centro' o 'derecha'.")

def obtener_eleccion_computadora():
  """Gets the computer's (goalkeeper's) dive choice."""
  opciones = ['izquierda', 'centro', 'derecha']
  return random.choice(opciones)

def determinar_resultado(eleccion_jugador, eleccion_computadora):
  """Determines if the shot is a goal or a save."""
  print(f"\nHas pateado hacia la {eleccion_jugador}.")
  print("El arquero se prepara...")
  time.sleep(1) # Add a small delay for suspense
  print(f"¡El arquero se tira hacia la {eleccion_computadora}!")
  time.sleep(0.5)

  if eleccion_jugador == eleccion_computadora:
    print("\n¡ATAJÓ EL ARQUERO! 🧤")
    return False # No goal
  else:
    print("\n¡¡¡GOOOOOOOOOOL!!! ⚽🥅")
    return True # Goal

def jugar_tanda():
  """Main function to play the penalty shootout game."""
  mostrar_introduccion()

  goles_jugador = 0
  goles_computadora = 0 # In this simple version, computer doesn't shoot, only saves.
                       # We can track saves instead if preferred. Let's count player goals vs saves.
  rondas = 5

  for i in range(rondas):
    print(f"\n--- Ronda {i + 1} de {rondas} ---")

    eleccion_jugador = obtener_eleccion_jugador()
    eleccion_computadora = obtener_eleccion_computadora()

    if determinar_resultado(eleccion_jugador, eleccion_computadora):
      goles_jugador += 1

    # In a more complex game, the computer would also take a shot here.
    # For simplicity, we just focus on the player's shots.

    print(f"\nMarcador actual: Jugador {goles_jugador} - Arquero (atajadas) {i + 1 - goles_jugador}")
    print("------------------------------------")
    time.sleep(1) # Pause before next round

  # Determine the winner
  print("\n--- ¡Fin de la tanda de penales! ---")
  print(f"Resultado final: Jugador {goles_jugador} goles en {rondas} intentos.")
  # We compare goals scored vs saves made by the computer
  saves_computadora = rondas - goles_jugador
  print(f"El arquero atajó {saves_computadora} penales.")

  if goles_jugador > saves_computadora: # Win if you score more than half the rounds + 1 (implicitly)
      print("\n¡FELICITACIONES! ¡Has ganado la tanda de penales! 🎉🏆")
  elif goles_jugador == saves_computadora and rondas % 2 != 0 : # Specific check for odd rounds draw, less likely
       print("\n¡EMPATE! Fue una tanda muy reñida. 🤝")
  elif goles_jugador < saves_computadora: # Lose if computer saves more
       print("\n¡Mejor suerte la próxima! El arquero ha ganado esta vez. 🧤")
  else: # Handle potential even round draws if logic were different
       print("\n¡EMPATE! Fue una tanda muy reñida. 🤝")


# Start the game when the script is run
if __name__ == "__main__":
  jugar_tanda()
