from datetime import date, datetime


def converter_str_date(data_str: str):
    data_convertida = datetime.strptime(data_str, "%b-%d-%Y")
    return data_convertida.date()


def calcular_duracao(data_inicial: date, data_final: date):
    duracao = data_final - data_inicial
    print(duracao)
    return duracao.days


class Viagem:

    def __init__(self,
                 destino: str,
                 data_inicio: str,
                 data_chegada_destino: str,
                 data_partida_destino: str,
                 data_chegada_retorno: str):

        self.destino = destino
        self.data_inicio = converter_str_date(data_inicio)
        self.data_chegada_destino = converter_str_date(data_chegada_destino)
        self.data_partida_destino = converter_str_date(data_partida_destino)
        self.data_chegada_retorno = converter_str_date(data_chegada_retorno)
        self.duracao = calcular_duracao(data_inicial=self.data_inicio, data_final=self.data_chegada_retorno)

    def verificar_viabilidade(self):
        if self.duracao > 0:
            print("Duração > 0")
            if self.data_partida_destino >= self.data_chegada_destino:
                print("Data de partida é maior que data de chegada no destino")
                return True
            else:
                print("Data de partida é menor que data de chegada no destino")
                print("inviavel")
                return False
        else:
            print("Não é viavel")
            return False

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
