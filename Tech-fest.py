import flet as ft


def main(page: ft.Page):
    page.title = "Fisic calculator"
    page.bgcolor = "white"
    page.window.height = 1200
    page.window.width = 1200
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.add()
    ft.app(target=main)