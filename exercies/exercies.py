from .models import MM1CappedPopulation

"""
Problema:

Una empresa de aire acondicionado tiene el servicio de reparación de sistema central de refrigeración en 5 clientes. El equipo que repara los sistemas de refrigeración recibe 2 solicitudes promedio diarias de reparación que siguen una distribución de Poisson y pueden reparar en promedio 12 máquinas por día con distribución exponencial entre tiempos de reparación.

- Tenemos 1 equipo de reparación.
- Arrivos exponenciales, y tiempos de reparación exponenciales.
- La capacidad del sistema es indeterminada
- La población es de 5 clientes, se asume que cada cliente tiene un aire acondicionado.
- Se reciben 2 maquinas por día
- Se pueden reparar 12 máquinas por día.
- Se asume las maquinas se reparan en el orden de llegada

Este analisis lleva a considerar un modelo M/M/1 FIFO/-/5, tasa de servicio de 12 por dia. La tasa de llegada individual la podemos calcular como $lambda_{ind} = lambda_0 = frac{lambda_n}{m} = frac{2}{5} = 0.4$ por día.
"""

LMBDA = (2/5)/24 # tasa de llegada por hora (0.4/dia)
MU = 12/24 # tasa de servicio por hora (12/dia)
POPULATION = 5 # poblacion (5 clientes)

MODEL = MM1CappedPopulation(lmbda=LMBDA, mu=MU, m=POPULATION)

def exercise_a():
    """
    Ejercicio a) Cantidad media de quipos rotos.

    Esta es la cantidad media de unidades en el sistema.
    """

    print(f"Cantidad media de equipos rotos: {MODEL.system_units_amount_mean():.2f} equipos por hora", )

def exercise_b():
    """
    Ejercicio b) Tiempo medio que los equipos esperan para ser reparados.

    Puede ser el tiempo que esperan en fila para empezar a ser reparados, o el tiempo que esperan en el sistema hasta terminar de ser reparados. Se escoje el tiempo en el sistema.
    """

    print(f"Tiempo medio que los equipos esperan para ser reparados: {MODEL.time_in_system_mean()*60:.2f} minutos")

def exercise_c():
    """
    Ejercicio c) Probabilidad de que 2 o más equipos estén fuera de servicio.

    Esta es la probabilidad total menos la probabilidad de que haya 0 o 1 equipos fuera de servicio.
    """

    prob_0 = MODEL.probability_of_zero_units()
    prob_1 = MODEL.probability_of_n_units(1, MM1CappedPopulation.PnStrategies.DEFAULT)

    print(f"Probabilidad de que 2 o más equipos estén fuera de servicio: {(1 - (prob_0 + prob_1))*100:.2f} %")

def run_exercies():
    """
    Función principal para ejecutar los ejercicios.
    """

    print("\nResultados obtenidos al aplicar el modelo M/M/1 FIFO/-/5:")
    print("=========================================================\n")
    print("Ejercicio a)")
    exercise_a()
    print("\nEjercicio b)")
    exercise_b()
    print("\nEjercicio c)")
    exercise_c()
    print("\n=========================================================\n")