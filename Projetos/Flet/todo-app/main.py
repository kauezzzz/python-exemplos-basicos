import flet as ft
from bd.connectiondb import DataBase

class AppToDo:
    def __init__(self, page: ft.Page):
        # Inicializa o aplicativo com a página Flet e configura as configurações iniciais
        self.page = page
        self.configurar_pagina()
        self.banco_dados = DataBase()
        self.usuario = None
        self.verificar_usuario()

    def configurar_pagina(self):
        # Configura as propriedades iniciais da página
        self.page.title = 'Aplicativo ToDo'
        self.page.window_width = 400
        self.page.window_height = 750
        self.page.vertical_alignment = ft.MainAxisAlignment.START
        self.page.theme_mode = ft.ThemeMode.DARK # Define o tema escuro
        self.page.padding = 20
        self.definir_cores()

    def definir_cores(self):
        # Define o esquema de cores para o modo escuro
        self.cor = {
            'primaria': '#3498db',
            'secundaria': '#2ecc71',
            'fundo': '#121212',
            'texto': '#ffffff',
            'texto_secundario': '#b3b3b3',
            'destaque': '#e74c3c',
            'item_fundo': '#1e1e1e',
            'borda': '#333333',
            'checkbox': '#3498db',
            'botao': '#3499db' 
        }

    def verificar_usuario(self):
        # Verifica se o usuário já foi definido, caso contrário, pede o nome
        if self.usuario is None:
            self.pedir_nome_usuario()
        else:
            self.main()

    def pedir_nome_usuario(self):
        # Cria e exibe o formulário para o usuário inserir seu nome
        def salvar_usuario(e):
            self.usuario = campo_usuario.value if campo_usuario.value else "Usuário"
            self.page.controle.clear()
            self.main()

            campo_usuario = ft.TextField(
                label="Digite seu nome",
                border_color=self.cor['primaria'],
                focused_border_color=self.cor['secundaria'],
                text_style=ft.TextStyle(color=self.cor['texto']),
                bgcolor=self.cor['item_fundo'],
                border_radius=8,
            )

            botao_confirmar = ft.ElevatedButton(
                text="Confirmar",
                on_click=salvar_usuario,
                style=ft.ButtonStyle(
                    color=self.cor['texto'],
                    bgcolor=self.cor['botao'],
                    shape=ft.RoundedReactangleBorder(radius=8),
                )
            )

            # Adiciona os elementos do formulário à página
            self.page.add(
                ft.Container(
                    content=ft.Column([
                        ft.Text("Digite seu nome", color=self.cor['texto'], size=18),
                        campo_usuario,
                        botao_confirmar
                    ], alignment=ft.MainAxisAlignment.CENTER, spacing=20),
                    padding=20,
                    bgcolor=self.cor['fundo'],
                )
            )

        def main(self):
            # Configura e exibe a interface principal do aplicativo
            self.page.bgcolor = self.cor['fundo']
            self.page.add(
                self.criar_cabecalho(),
                self.criar_secao_entrada(),
                self.criar_abas(),
                self.criar_lista_tarefas()
            )

        def criar_cabecalho(self):
            # Cria o cabeçalho com saudação ao usuário
            return ft.Container(
                content=ft.Column([
                    ft.Text(f'Olá, {self.usuario} 😀', size=24, color=self.cor['text'], weight=ft.FontWeight.BOLD),
                    ft.Text('Gerencie suas tarefas diárias', size=16, color=self.cor['texto_secundario'])
                ], alignment=ft.MainAxisAlignment.CENTER, spacing=5),
                padding=ft.padding.symmetric(vertical=20)
            )
        
        def criar_secao_entrada(self):
            # Cria a seção de entrada para adicionar novas tarefas
            self.entrada_tarefa = ft.TextField(
                hint_text='Adicione uma nova tarefa...',
                expand=True,
                border_color=self.cor['borda'],
                focused_border_color=self.cor['primaria'],
                text_style=ft.TextStyle(color=self.cor['texto']),
                hint_style=ft.TextStyle(color=self.cor['texto_secundario']),
                bgcolor=self.cor['item_fundo'],
                border_radius=8,
            )

            botao_adicionar = ft.IconButton(
                icon=ft.icons.ADD_CIRCLE,
                icon_color=self.cor['botao'],
                icon_size=30,
                on_click=self.adicionar_tarefa,
                style=ft.ButtonStyle(
                    shape=ft.CircleBorder(),
                    bgcolor=self.cor['item_fundo'],
                )
            )