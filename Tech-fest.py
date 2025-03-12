import flet as ft


def main(page: ft.Page):
    page.title = "Physic's calculator"
    page.bgcolor = "#FCFBF4"
    page.window.height = 750
    page.window.width = 800
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START

    title=ft.Text("Physic's calculator",color="black",height=50) 
    
    def ohms_law():#diego
        return
    def capacitance():#carlos , ethan
        return
    def resistance():#carlos , ethan
        return


    
    ohms_law_button=ft.ElevatedButton("Ohms law",on_click=ohms_law,width=200,height=50,style=ft.ButtonStyle(bgcolor="#849bff",color="white"),)
    capacitance_button=ft.ElevatedButton("Capacitance",on_click=capacitance,width=200,height=50,style=ft.ButtonStyle(bgcolor="#849bff",color="white"))
    resistance_button=ft.ElevatedButton("Resistance",on_click=resistance,width=200,height=50,style=ft.ButtonStyle(bgcolor="#849bff",color="white"))

    button_column=ft.Column([ohms_law_button,capacitance_button,resistance_button],spacing=40)




    page.add(title,button_column)

ft.app(target=main)