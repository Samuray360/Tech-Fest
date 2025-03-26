import flet as ft

def main(page: ft.Page):
    page.title = "Physic's Calculator"
    page.bgcolor = "#FCFBF4"
    page.window.height = 750
    page.window.width = 800
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START

    title = ft.Text("Physic's Calculator", color="black", height=50) 
    user_input = ft.TextField(label="Enter Value")

    def ohms_law(e):
        def calculate(e):
            try:
                v = voltage.value.strip()
                i = current.value.strip()
                r = resistance.value.strip()

                if r and i and not v:
                    voltage_result = float(i) * float(r)
                    result.value = f"Voltage = {voltage_result:.2f} Volts"
                    voltage.value = str(voltage_result)

                elif v and i and not r:
                    resistance_result = float(v) / float(i)
                    result.value = f"Resistance = {resistance_result:.2f} Ohms"
                    resistance.value = str(resistance_result)

                elif v and r and not i:
                    current_result = float(v) / float(r)
                    result.value = f"Current = {current_result:.2f} Amps"
                    current.value = str(current_result)

                else:
                    result.value = "Enter exactly 2 values"

            except ZeroDivisionError:
                result.value = "Error: Cannot divide by zero"
            except:
                result.value = "Error: Invalid input"

            page.update()

        voltage = ft.TextField(label="Voltage (V)", width=150)
        current = ft.TextField(label="Current (I)", width=150)
        resistance = ft.TextField(label="Resistance (R)", width=150)
        result = ft.Text("")

        dialog = ft.AlertDialog(
            title=ft.Text("Ohm's Law"),
            content=ft.Column([
                voltage,
                current,
                resistance,
                ft.ElevatedButton("Calculate", on_click=calculate),
                result
            ]),
            actions=[ft.TextButton("Close", on_click=lambda e: setattr(dialog, "open", False) or page.update())]
        )

        page.dialog = dialog
        dialog.open = True
        page.update()

    # Pages
    ohms_law_page = ft.Container(
        content=ft.Column([
            ft.Text("Ohm's Law Calculation"),
            user_input,
        ]),
        bgcolor="#FCFBF4",
        width=page.width,
        height=600,
        visible=False
    )

    capacitance_page = ft.Container(
        content=ft.Column([
            ft.Text("Capacitance Calculation"),
            user_input,
        ]),
        width=page.width,
        height=600,
        bgcolor="#FCFBF4",
        visible=False
    )

    resistance_page = ft.Container(
        content=ft.Column([
            ft.Text("Resistance Calculation"),
            user_input,
        ]),
        bgcolor="#FCFBF4",
        width=page.width,
        height=600,
        visible=False
        
    )

    # Home view
    home_view = ft.Container(
        content=ft.Column([title]),
        bgcolor="#FCFBF4",
        width=page.width,
        height=600,
        visible=True
    )

    # Functions to Switch Views (Fixed)
    def ohms_law_view(e):
        home_view.visible = False
        ohms_law_page.visible = True
        capacitance_page.visible = False
        resistance_page.visible = False
        page.update()

    def capacitance_view(e):
        home_view.visible = False
        ohms_law_page.visible = False
        capacitance_page.visible = True
        resistance_page.visible = False
        page.update()

    def resistance_view(e):
        home_view.visible = False
        ohms_law_page.visible = False
        capacitance_page.visible = False
        resistance_page.visible = True
        page.update()
    def back(e):
        home_view.visible = True
        ohms_law_page.visible = False
        capacitance_page.visible = False
        resistance_page.visible = False
        page.update

    # Buttons
    ohms_law_button = ft.ElevatedButton(
        "Ohm's Law", on_click=ohms_law_view, width=200, height=50,
        style=ft.ButtonStyle(bgcolor="#849bff", color="white")
    )

    capacitance_button = ft.ElevatedButton(
        "Capacitance", on_click=capacitance_view, width=200, height=50,
        style=ft.ButtonStyle(bgcolor="#849bff", color="white")
    )

    resistance_button = ft.ElevatedButton(
        "Resistance", on_click=resistance_view, width=200, height=50,
        style=ft.ButtonStyle(bgcolor="#849bff", color="white")
    )
    back_button=ft.ElevatedButton(
        "back",on_click=back,style=ft.ButtonStyle(bgcolor="#849bff", color="white")
    )

    button_column = ft.Column([ohms_law_button, capacitance_button, resistance_button,], spacing=40)

    # Update Home View to include buttons
    home_view.content.controls.append(button_column)
    ohms_law_page.content.controls.append(back_button)
    capacitance_page.content.controls.append(back_button)
    resistance_page.content.controls.append(back_button)

    # Stack all views
    Views = ft.Stack(
        controls=[home_view, resistance_page, capacitance_page, ohms_law_page]
    )

    # Add components to the page
    page.add(Views)

ft.app(target=main)
