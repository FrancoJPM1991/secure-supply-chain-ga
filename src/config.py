# Objective weights / Pesos de los objetivos
ALPHA = 0.7
BETA = 0.3

# Transportation costs (MXN) / Costos de transporte  (MXN)
C_SEC = 1000
C_SALARY = 50
C_FUEL = 25
E_FUEL = 0.3

# Vehicle weight fuel consumption penalty  / Penalización por consumo de combustible por peso del vehículo
W_PLUS = 0.06 / 100

# Operational constraints / Restricciones operativas
MAX_TRANSIT_TIME_HR = 20
MINIMUM_SHIPMENT_WEIGHT = 300

SECURITY_THRESHOLD = 0.7
MAX_CENTERS_PER_ZONE = 2

# GA parameters / Parámetros del AG
ELITISM_PERCENTAGE = 0.05

MUTATION_PROBABILITY = (0.02, 0.15)

CROSSOVER_PROBABILITY = (0.65, 0.95)

TOURNAMENT_PARTICIPANTS = 5

POP_SIZE = 200

N_GENERATIONS = 300

CYCLES = 30

# Crime-risk-speed mapping / Mapeo de riesgo-delito-velocidad
def get_speed(risk):

    if risk < 0.3:
        return 110

    elif risk <= 0.7:
        return 90

    return 70
