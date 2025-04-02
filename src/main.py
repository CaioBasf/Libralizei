# Importando a biblioteca
import flet as ft

# Definindo a função principal
def main(page : ft.Page):

    # Titulo da página 
    page.title = "Meu primeiro projeto em flet"

    # Controle de texto de texto
    text = ft.Text(value="Meu primeiro aplicativo em flet", color="red")

    # Anexando e atualizando para a página
    page.controls.append(text)
    page.update()

# Iniciando o App
ft.app(main)