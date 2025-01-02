from datetime import date


class Viagem:

    def __init__(self,
                 destino: str,
                 data_inicio: date,
                 data_chegada_destino: date,
                 data_chegada_retorno: date,
                 duracao: int,
                 delta_v: float):
        self.destino = destino
        self.data_inicio = data_inicio
        self.data_chegada_destino = data_chegada_destino
        self.data_chegada_retorno = data_chegada_retorno
        self.delta_v = delta_v
        self.duracao = duracao
