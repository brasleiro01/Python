"""
CONSTANTE = "Variáveis" que não vão mudar.
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""

velocidade = 61 # velocidade atual do carro
local_carro = 90 # local em que o carro esta na estrada

RADAR_1 = 60 # velocidade maxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # a distancia onde o radar pega

if velocidade > RADAR_1:
    print('velocidade acima do permitido')

if local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE) and \
        velocidade > RADAR_1:
    print('carro multado em radar 1')