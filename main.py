from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup

from entities.viagem import Viagem
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
        self.viagem_cancelar = None
        self.datas_reservadas = open("database/viagens_reservadas.csv").readlines()
        self.carregar_viagens_planejadas()
        self.contador = None

    def carregar_viagens_planejadas(self):
        cor_fundo_1 = [0, 0.5, 0.5, 0.9]
        cor_fundo_2 = [0, 0.3, 0.5, 0.9]
        self.contador = 1

        for linha in self.datas_reservadas:
            dados_viagem = ler_datas(linha)
            if self.contador % 2 == 0:
                btn = Button(text=f"Viagem [{self.contador}]\n"
                                  f"Destino: {dados_viagem[0]}\n"
                                  f"Início da viagem: {dados_viagem[1]}, Chegada no destino:{dados_viagem[2]}\n"
                                  f"Retorno da viagem: {dados_viagem[3]}, "
                                  f"Chegada na Terra: {dados_viagem[4]}\n"
                                  f"Duração total da viagem: {dados_viagem[5]} dias",
                             halign='center',
                             valign="middle",
                             background_normal="",
                             background_color=cor_fundo_1,
                             on_press=lambda instance, num_viagem=self.contador: self.popup_cancelar_viagem(num_viagem))
            else:
                btn = Button(text=f"Viagem [{self.contador}]\n"
                                  f"Destino: {dados_viagem[0]}\n"
                                  f"Início da viagem: {dados_viagem[1]}, Chegada no destino: {dados_viagem[2]}\n"
                                  f"Retorno da viagem: {dados_viagem[3]}, "
                                  f"Chegada na Terra:{dados_viagem[4]}\n"
                                  f"Duração total da viagem: {dados_viagem[5]} dias",
                             halign='center',
                             valign="middle",
                             background_normal="",
                             background_color=cor_fundo_2,
                             on_press=lambda instance, num_viagem=self.contador: self.popup_cancelar_viagem(num_viagem))

            self.ids.viagens_reservadas.add_widget(btn)
            self.contador += 1

    def popup_cancelar_viagem(self, num_viagem: int):  # mostra pop up perguntando se quer cancelar viagem
        gridlayout = BoxLayout(
            orientation="vertical",
            size=(1, 1)
        )

        aviso = Label(
            text=f"Você deseja cancelar a viagem [{num_viagem}]?",
            text_size=(150, None),
            halign="center",
            valign="middle"
        )

        botao_sim = Button(
            text='Sim',
            size_hint=(1, 0.2),
            on_press=lambda instance, viagem=num_viagem: self.cancelar_viagem(viagem)
        )

        botao_nao = Button(
            text='Não',
            size_hint=(1, 0.2)
        )

        gridlayout.add_widget(aviso)
        gridlayout.add_widget(botao_sim)
        gridlayout.add_widget(botao_nao)

        popup = Popup(title="Cancelar viagem",
                      auto_dismiss=False,
                      size_hint=(0.5, 0.45),
                      )

        popup.add_widget(gridlayout)
        botao_nao.bind(on_press=popup.dismiss)
        botao_sim.bind(on_press=popup.dismiss)

        popup.open()

    def cancelar_viagem(self, num_viagem):
        # buscando linha da viagem que quer deletar
        self.contador = 1
        self.viagem_cancelar = None
        for linha in self.datas_reservadas:
            print(linha)
            if self.contador == num_viagem:
                self.viagem_cancelar = linha
            self.contador += 1

        with open("database/viagens_reservadas.csv", "r") as f:
            lines = f.readlines()
        with open("database/viagens_reservadas.csv", "w") as f:
            for line in lines:
                if line.strip("\n") not in f"{self.viagem_cancelar}":
                    print("Escrevendo linha")
                    f.write(line)
                else:
                    print("Não escrevendo linha que quero deletar")

        self.recarregar_viagens_planejadas()

    def recarregar_viagens_planejadas(self):
        app.tela_menu_viagens_planejadas()

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
                self.datas_ida = open("database/terra-lua.csv").readlines()
                for linha in self.datas_ida:
                    data = ler_datas(linha)

                    btn = Button(text=f"[{self.contador}]\nInício da viagem: {data[0]}\nChegada na Lua: {data[1]}",
                                 on_press=lambda instance, c=self.contador: self.salvar_ida("lua", c),
                                 background_normal="",
                                 background_color=[0.8, 0.8, 0.8, 0.5],
                                 halign="center",
                                 valign="middle"
                                 )
                    self.ids.viagens_grid.add_widget(btn)
                    self.contador += 1

            case "marte":
                print("Carregando ida: Marte")
                self.datas_ida = open("database/terra-marte.csv").readlines()
                for linha in self.datas_ida:
                    data = ler_datas(linha)
                    btn = Button(text=f"[{self.contador}]\nInício da viagem: {data[0]}\nChegada em Marte: {data[1]}",
                                 on_press=lambda instance, c=self.contador: self.salvar_ida("marte", c),
                                 background_normal="",
                                 background_color=[0.8, 0.8, 0.8, 0.5],
                                 halign="center",
                                 valign="middle"
                                 )
                    self.ids.viagens_grid.add_widget(btn)
                    self.contador += 1

            case "jupiter":
                print("Jupiter")
                self.datas_ida = open("database/terra-jupiter.csv").readlines()
                for linha in self.datas_ida:
                    data = ler_datas(linha)
                    btn = Button(text=f"[{self.contador}]\nInício da viagem: {data[0]}\nChegada em Jupiter: {data[1]}",
                                 on_press=lambda instance, c=self.contador: self.salvar_ida("jupiter", c),
                                 background_normal="",
                                 background_color=[0.8, 0.8, 0.8, 0.5],
                                 halign="center",
                                 valign="middle"
                                 )
                    self.ids.viagens_grid.add_widget(btn)
                    self.contador += 1

    def salvar_ida(self, destino: str, num_ida: int):
        match destino:
            case "marte":
                print("Salvando ida: Marte")
                self.data_ida_escolhida = ler_datas(self.datas_ida[num_ida - 1])
                print("ida escolhida: " + self.data_ida_escolhida[0] + " " + self.data_ida_escolhida[1])
                self.ids.viagens_grid.clear_widgets()
                self.carregar_datas_retorno("marte")

            case "lua":
                self.data_ida_escolhida = ler_datas(self.datas_ida[num_ida - 1])
                self.ids.viagens_grid.clear_widgets()
                self.carregar_datas_retorno("lua")

            case "jupiter":
                self.data_ida_escolhida = ler_datas(self.datas_ida[num_ida - 1])
                self.ids.viagens_grid.clear_widgets()
                self.carregar_datas_retorno("jupiter")

    def carregar_datas_retorno(self, destino: str):
        # mostrar resumo das datas escolhidas pelo usuario ate agora
        self.ids.resumo_viagem.font_size = "20sp"
        self.ids.resumo_viagem.text = f"Data de ida escolhida: {self.data_ida_escolhida[0]}" \
                                      f"\nData de chegada no destino: {self.data_ida_escolhida[1]}"\
                                      f"\n\nAgora selecione as datas de retorno:"

        cor_inviavel = [0.255, 0, 0, 1]
        cor_viavel = [0, 0.255, 0, 1]
        print("Carregando datas retorno")
        self.contador = 1
        match destino:
            case "marte":
                print("Marte")
                self.datas_retorno = open("database/marte-terra.csv").readlines()

                for linha in self.datas_retorno:  # gerar botões com as datas de retorno
                    data = ler_datas(linha)
                # logica de ver se a data de partida do planeta x é maior ou igual que a data de chegada no planeta x
                    viagem_experimental = Viagem(
                        "planeta_x",
                        self.data_ida_escolhida[0],
                        self.data_ida_escolhida[1],
                        data[0],
                        data[1]
                    )
                    if viagem_experimental.verificar_viabilidade():  # se for viavel...
                        btn = Button(text=f"[{self.contador}]\nData de partida: {data[0]}\n"
                                          f"Data de chegada na Terra: {data[1]}",
                                     on_press=lambda instance, c=self.contador: self.salvar_retorno("marte", c),
                                     background_color=cor_viavel,
                                     background_normal="",
                                     halign="center",
                                     valign="middle"
                                     )

                    else:
                        btn = Button(text=f"[{self.contador}]\nData de partida: {data[0]}\n"
                                          f"Data de chegada na Terra: {data[1]}",
                                     on_press=lambda instance, c=self.contador: self.salvar_retorno("marte", c),
                                     background_color=cor_inviavel,
                                     background_normal="",
                                     halign="center",
                                     valign="middle"
                                     )
                    self.ids.viagens_grid.add_widget(btn)
                    self.contador += 1

            case "lua":
                self.datas_retorno = open("database/lua-terra.csv").readlines()

                for linha in self.datas_retorno:
                    data = ler_datas(linha)
                    viagem_experimental = Viagem(
                        "planeta_x",
                        self.data_ida_escolhida[0],
                        self.data_ida_escolhida[1],
                        data[0],
                        data[1]
                    )
                    if viagem_experimental.verificar_viabilidade():
                        btn = Button(text=f"[{self.contador}]\nData de partida: {data[0]}\n"
                                          f"Data de chegada na Terra: {data[1]}",
                                     on_press=lambda instance, c=self.contador: self.salvar_retorno("lua", c),
                                     background_color=cor_viavel,
                                     background_normal="",
                                     halign="center",
                                     valign="middle"
                                     )

                    else:
                        btn = Button(text=f"[{self.contador}]\nData de partida: {data[0]}\n"
                                          f"Data de chegada na Terra: {data[1]}",
                                     on_press=lambda instance, c=self.contador: self.salvar_retorno("lua", c),
                                     background_color=cor_inviavel,
                                     background_normal="",
                                     halign="center",
                                     valign="middle"
                                     )
                    self.ids.viagens_grid.add_widget(btn)
                    self.contador += 1

            case "jupiter":
                self.datas_retorno = open("database/jupiter-terra.csv").readlines()

                for linha in self.datas_retorno:
                    data = ler_datas(linha)
                    viagem_experimental = Viagem(
                        "planeta_x",
                        self.data_ida_escolhida[0],
                        self.data_ida_escolhida[1],
                        data[0],
                        data[1]
                    )
                    if viagem_experimental.verificar_viabilidade():
                        btn = Button(text=f"[{self.contador}]\nData de partida: {data[0]}\n"
                                          f"Data de chegada na Terra: {data[1]}",
                                     on_press=lambda instance, c=self.contador: self.salvar_retorno("jupiter", c),
                                     background_color=cor_viavel,
                                     background_normal="",
                                     halign="center",
                                     valign="middle"
                                     )

                    else:
                        btn = Button(text=f"[{self.contador}]\nData de partida: {data[0]}\n"
                                          f"Data de chegada na Terra: {data[1]}",
                                     on_press=lambda instance, c=self.contador: self.salvar_retorno("jupiter", c),
                                     background_color=cor_inviavel,
                                     background_normal="",
                                     halign="center",
                                     valign="middle"
                                     )
                    self.ids.viagens_grid.add_widget(btn)
                    self.contador += 1

    def salvar_retorno(self, destino: str, num_volta: int):
        print("Salvando retorno")
        match destino:
            case "marte":
                print("Marte")
                self.data_retorno_escolhida = ler_datas(self.datas_retorno[num_volta - 1])
                print(
                    "Data retorno escolhida: " + self.data_retorno_escolhida[0] + " " + self.data_retorno_escolhida[1])
                self.ids.viagens_grid.clear_widgets()
                self.salvar_viagem("marte")
            case "lua":
                self.data_retorno_escolhida = ler_datas(self.datas_retorno[num_volta - 1])
                self.ids.viagens_grid.clear_widgets()
                self.salvar_viagem("lua")
            case "jupiter":
                self.data_retorno_escolhida = ler_datas(self.datas_retorno[num_volta - 1])
                self.ids.viagens_grid.clear_widgets()
                self.salvar_viagem("jupiter")

    def salvar_viagem(self, destino: str):
        viagem = Viagem(
            destino,  # destino
            self.data_ida_escolhida[0],  # data inicio
            self.data_ida_escolhida[1],  # data chegada no destino
            self.data_retorno_escolhida[0],  # data partida do destino
            self.data_retorno_escolhida[1]  # data de chegada na Terra
        )
        # Verificação da viabilidade da viagem antes de salvar
        if not viagem.verificar_viabilidade():
            gridlayout = BoxLayout(
                orientation="vertical",
                size=(1, 1)
            )

            aviso = Label(
                text="Você não pode planejar uma viagem que termina antes da data de início!",
                text_size=(250, None),
                halign="center",
                valign="middle"
            )

            botao = Button(
                text='Entendido',
                size_hint=(1, 0.2)
            )

            gridlayout.add_widget(aviso)
            gridlayout.add_widget(botao)

            popup = Popup(title="Atenção!",
                          auto_dismiss=True,
                          size_hint=(0.5, 0.5),
                          )

            popup.add_widget(gridlayout)
            botao.bind(on_press=popup.dismiss)

            popup.open()
        else:
            # Salvando viagem escolhida em formato csv. Datas já conferidas
            open("database/viagens_reservadas.csv", "a").writelines(viagem.converter_csv())
            self.mostrar_popup_resumo(viagem)
        self.retornar_menu()

    def mostrar_popup_resumo(self, viagem: Viagem):
        gridlayout = BoxLayout(
            orientation="vertical",
            size=(1, 1)
        )

        aviso = Label(
            text=f"Resumo da viagem reservada:"
                 f"\n\nData de saída da Terra: {viagem.data_inicio}"
                 f"\nData de chegada em {viagem.destino}: {viagem.data_chegada_destino}"
                 f"\nData de saída de {viagem.destino}: {viagem.data_partida_destino}"
                 f"\nData de chegada na Terra: {viagem.data_chegada_retorno}"
                 f"\n\nDuração da viagem: {viagem.duracao} dias"
                 f"\n\nFaça uma boa viagem!",
            text_size=(250, None),
            halign="center",
            valign="middle"
        )

        botao = Button(
            text='Entendido',
            size_hint=(1, 0.2)
        )

        gridlayout.add_widget(aviso)
        gridlayout.add_widget(botao)

        popup = Popup(title="Informativo",
                      auto_dismiss=True,
                      size_hint=(0.7, 0.5),
                      )

        popup.add_widget(gridlayout)
        botao.bind(on_press=popup.dismiss)

        popup.open()

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
        return self.sm

    def tela_menu_inicial(self):
        self.sm.current = "Menu"

    def tela_menu_viagens_planejadas(self):  # mesma logica que foi aplicada em reservar_viagem.
        for tela in self.sm.screens:
            if "ViagensPlanejadas" in tela.name:
                self.sm.remove_widget(tela)
        self.sm.add_widget(ViagensPlanejadas(name="ViagensPlanejadas"))
        self.sm.current = "ViagensPlanejadas"

    def tela_reservar_viagem(self, destino: str):
        # Criando a tela assim que aperta o botão
        # E se aperto o botão pela segunda vez,
        # o programa vai detectar que ja tem uma tela criada, apagará e criará outra nova
        for tela in self.sm.screens:
            if "ReservarViagem" in tela.name:
                self.sm.remove_widget(tela)

        self.sm.add_widget(ReservarViagem(name="ReservarViagem", destino=destino))
        self.sm.current = "ReservarViagem"


if __name__ == '__main__':
    app = MainApp()
    app.run()
    