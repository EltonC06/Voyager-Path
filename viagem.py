from datetime import date


class Viagem:

    def __init__(self,
                 destino: str,
                 data_inicio: date,
                 data_chegada_destino: date,
                 data_partida_destino: date,
                 data_chegada_retorno: date):

        self.destino = destino
        self.data_inicio = data_inicio
        self.data_chegada_destino = data_chegada_destino
        self.data_partida_destino = data_partida_destino
        self.data_chegada_retorno = data_chegada_retorno
        self.duracao = 100

    def converter_csv(self):
        return (
            [self.destino + "," + str(self.data_inicio) + "," + str(self.data_chegada_destino) + "," +
             str(self.data_partida_destino) + "," + str(self.data_chegada_retorno) + "," + str(self.duracao) + ",\n"]
        )

    def __str__(self):
        return f'Destino: {self.destino}\n' \
               f'Data de início viagem: {self.data_inicio}\n' \
               f'Data de chegada em {self.destino}: {self.data_chegada_destino}\n' \
               f'Data de partida de {self.destino}: {self.data_partida_destino}\n' \
               f'Data de chegada na Terra: {self.data_chegada_retorno}\n' \
               f'Duração total da viagem: {self.duracao}'
