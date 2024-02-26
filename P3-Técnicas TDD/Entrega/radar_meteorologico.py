def alcance_del_radar(T: float, tau: float) -> float:
    """Calcula el alcance del radar meteorológico"""
    """ entrada: T, intervalo de repetición de pulsos [segundos]"""
    """ Entrada: tau, ancho del pulso [microsegundos]"""
    """ Salida: Alcance del radar meteorológico [kilómetros]"""
   
   # Verifica que los argumentos no sean booleanos
    if isinstance(T, bool) or isinstance(tau, bool):
        raise TypeError("T y tau deben ser números, no booleanos")

    #Verifica que los valores de entrada sean números
    if T < 0 or T > 0.7 or tau > 4 or tau < 0:
        raise ValueError("Valores de T o tau fuera de rango permitido")

    #Verifica que T sea mayor que tau
    T_en_microsegundos = T * 1e6
    if T_en_microsegundos < tau:
        raise ValueError("T no puede ser menor que tau")

    


    #se ponen todas lass unidades en segundos, solo en necesario tau, T ya lo está
    tau=tau/pow(10,6)

    Co=3*pow(10,5) #Velocidad de la luz, 300000 km/s
    return Co*(T-tau)/2 # Calculo del alcance de radar
    
