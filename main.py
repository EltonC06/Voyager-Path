from datetime import datetime

from viagem import Viagem
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window

duracao_total = 0
dias_permanencia = 0
data_partida_terra = None
data_chegada_destino = None
data_partida_destino = None
data_chegada_terra = None
data_escolha = None

Window.size = (Window.height * 9 / 16, Window.height)


def ler_datas(linha: str):
    linha = linha.split(",")
    linha.pop()  # removendo o ultimo elemento da linha csv, pois ele sempre será '\n' e é inutil
    return linha


class Menu(Screen):
    pass


class ViagensPlanejadas(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.datas_reservadas = open("viagens_reservadas.csv").readlines()
        self.carregar_viagens_planejadas()
        self.contador = None

    def carregar_viagens_planejadas(self):
        cor_fundo_1 = [0, 0.5, 0.5, 1]
        cor_fundo_2 = [0, 0.3, 0.5, 1]
        self.contador = 1
        for linha in self.datas_reservadas:
            dados_viagem = ler_datas(linha)
            if self.contador % 2 == 0:
                btn = Button(text=f"Destino: {dados_viagem[0]}\n"
                                  f"Início da viagem: {dados_viagem[1]}, Chegada no destino: {dados_viagem[2]}\n"
                                  f"Data de retorno da viagem: {dados_viagem[3]}, Data de chegada na Terra:{dados_viagem[4]}\n"
                                  f"Duração total da viagem: {dados_viagem[5]} dias",
                             background_color=cor_fundo_1)
            else:
                btn = Button(text=f"Destino: {dados_viagem[0]}\n"
                                  f"Início da viagem: {dados_viagem[1]}, Chegada no destino: {dados_viagem[2]}\n"
                                  f"Data de retorno da viagem: {dados_viagem[3]}, Data de chegada na Terra:{dados_viagem[4]}\n"
                                  f"Duração total da viagem: {dados_viagem[5]} dias",
                             background_color=cor_fundo_2)

            self.ids.viagens_reservadas.add_widget(btn)
            self.contador += 1

    pass


class ReservarViagem(Screen):
    def __init__(self, destino: str, **kw):
        super().__init__(**kw)
        self.datas_retorno = None
        self.datas_ida = None
        self.data_retorno_escolhida = None
        self.data_ida_escolhida = None
        self.viagem_escolhida = None
        self.datas = None
        self.destino = destino
        self.contador = 1
        self.carregar_datas_ida(destino)

    def carregar_datas_ida(self, destino):
        self.contador = 1
        match destino:
            case "lua":
                print("Lua")
                self.datas_ida = open("terra-lua.csv").readlines()
                for linha in self.datas_ida:
                    data = ler_datas(linha)
                    btn = Button(text=f"[{self.contador}] Início da viagem: {data[0]}, Chegada na Lua: {data[1]}",
                                 on_press=lambda instance, c=self.contador: self.salvar_ida("lua", c)
                                 )
                    self.ids.viagens_grid.add_widget(btn)
                    self.contador += 1

            case "marte":  # !
                print("Carregando ida: Marte")
                self.datas_ida = open("terra-marte.csv").readlines()
                for linha in self.datas_ida:
                    data = ler_datas(linha)
                    btn = Button(text=f"[{self.contador}] Início da viagem: {data[0]}, Chegada em Marte: {data[1]}",
                                 on_press=lambda instance, c=self.contador: self.salvar_ida("marte", c)
                                 )
                    self.ids.viagens_grid.add_widget(btn)
                    self.contador += 1

            case "jupiter":
                print("Jupiter")
                self.datas_ida = open("terra-jupiter.csv").readlines()
                for linha in self.datas_ida:
                    data = ler_datas(linha)
                    btn = Button(text=f"[{self.contador}] Início da viagem: {data[0]}, Chegada em Jupiter: {data[1]}",
                                 on_press=lambda instance, c=self.contador: self.salvar_ida("jupiter", c)
                                 )
                    self.ids.viagens_grid.add_widget(btn)
                    self.contador += 1

    def salvar_ida(self, destino: str, num_ida: int):
        match destino:
            case "marte":
                print("Salvando ida: Marte")
                self.data_ida_escolhida = ler_datas(self.datas_ida[num_ida-1])
                print("ida escolhida: " + self.data_ida_escolhida[0] + " " + self.data_ida_escolhida[1])
                self.ids.viagens_grid.clear_widgets()
                self.carregar_datas_retorno("marte")

            case "lua":
                self.data_ida_escolhida = ler_datas(self.datas_ida[num_ida-1])
                self.ids.viagens_grid.clear_widgets()
                self.carregar_datas_retorno("lua")

            case "jupiter":
                self.data_ida_escolhida = ler_datas(self.datas_ida[num_ida-1])
                self.ids.viagens_grid.clear_widgets()
                self.carregar_datas_retorno("jupiter")

    def carregar_datas_retorno(self, destino: str):
        print("Carregando datas retorno")
        self.contador = 1
        match destino:
            case "marte":
                print("Marte")
                self.datas_retorno = open("marte-terra.csv").readlines()
                for linha in self.datas_retorno:  # gerar botões com as datas de retorno
                    data = ler_datas(linha)
                    btn = Button(text=f"[{self.contador}] Data de partida: {data[0]},"
                                      f"Data de chegada na Terra: {data[1]}",
                                 on_press=lambda instance, c=self.contador: self.salvar_retorno("marte", c))
                    self.ids.viagens_grid.add_widget(btn)
                    self.contador += 1

            case "lua":
                self.datas_retorno = open("lua-terra.csv").readlines()
                for linha in self.datas_retorno:
                    data = ler_datas(linha)
                    btn = Button(text=f"[{self.contador}] Data de partida: {data[0]},"
                                      f"Data de chegada na Terra: {data[1]}",
                                 on_press=lambda instance, c=self.contador: self.salvar_retorno("lua", c))
                    self.ids.viagens_grid.add_widget(btn)
                    self.contador += 1

            case "jupiter":
                self.datas_retorno = open("jupiter-terra.csv").readlines()
                for linha in self.datas_retorno:
                    data = ler_datas(linha)
                    btn = Button(text=f"[{self.contador}] Data de partida: {data[0]},"
                                      f"Data de chegada na Terra: {data[1]}",
                                 on_press=lambda instance, c=self.contador: self.salvar_retorno("jupiter", c))
                    self.ids.viagens_grid.add_widget(btn)
                    self.contador += 1

    def salvar_retorno(self, destino: str, num_volta: int):
        print("Salvando retorno")
        match destino:
            case "marte":
                print("Marte")
                self.data_retorno_escolhida = ler_datas(self.datas_retorno[num_volta-1])
                print("Data retorno escolhida: " + self.data_retorno_escolhida[0] + " " + self.data_retorno_escolhida[1])
                self.ids.viagens_grid.clear_widgets()
                self.salvar_viagem("marte")
            case "lua":
                self.data_retorno_escolhida = ler_datas(self.datas_retorno[num_volta-1])
                self.ids.viagens_grid.clear_widgets()
                self.salvar_viagem("lua")
            case "jupiter":
                self.data_retorno_escolhida = ler_datas(self.datas_retorno[num_volta-1])
                self.ids.viagens_grid.clear_widgets()
                self.salvar_viagem("jupiter")

    def salvar_viagem(self, destino: str):
        viagem = Viagem(
            destino,  # destino
            converter_str_date(self.data_ida_escolhida[0]),  # data inicio
            converter_str_date(self.data_ida_escolhida[1]),  # data chegada no destino
            converter_str_date(self.data_retorno_escolhida[0]),  # data partida do destino
            converter_str_date(self.data_retorno_escolhida[1])  # data de chegada na Terra
        )
        # salvando viagem escolhida em formato csv
        open("viagens_reservadas.csv", "a").writelines(viagem.converter_csv())
        # Retorno à tela inicial
        self.retornar_menu()

    def retornar_menu(self):
        self.clear_widgets()
        app.tela_menu_inicial()
    pass


class MainApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sm = None

    def build(self):
        self.sm = ScreenManager()
        # Adicionando telas no objeto ScreenManager
        self.sm.add_widget(Menu(name="Menu"))
        self.sm.add_widget(ViagensPlanejadas(name="ViagensPlanejadas"))
        return self.sm

    def tela_menu_inicial(self):
        self.sm.current = "Menu"

    def tela_menu_viagens_planejadas(self):
        self.sm.current = "ViagensPlanejadas"

    def tela_reservar_viagem(self, destino: str):
        # Criando a tela assim que aperta o botão
        # E se aperto o botão pela segunda vez,
        # o programa vai detectar que ja tem uma tela criada, apagará e criará uma nova
        for tela in self.sm.screens:
            if "ReservarViagem" in tela.name:
                self.sm.remove_widget(tela)

        self.sm.add_widget(ReservarViagem(name="ReservarViagem", destino=destino))
        self.sm.current = "ReservarViagem"


def converter_str_date(data_str: str):
    data_convertida = datetime.strptime(data_str, "%b-%d-%Y")
    return data_convertida.date()


if __name__ == '__main__':
    app = MainApp()
    app.run()
