import flet as ft

def calculate_capacitance(capacitances, configuration):
    """Calculates total capacitance based on configuration."""
    if not capacitances:
        return "Error: At least one capacitance value is required."

    for c in capacitances:
        if c <= 0:
            return "Error: All capacitance values must be positive."

    if configuration == "Parallel":
        return sum(capacitances)
    
    elif configuration == "Series":
        return 1.0 / sum(1.0 / c for c in capacitances)

    return "Error: Configuration must be 'Series' or 'Parallel'."

def calculate_resistance(resistances, configuration):
    """Calculates total resistance based on configuration."""
    if not resistances:
        return "Error: At least one resistance value is required."

    for r in resistances:
        if r <= 0:
            return "Error: All resistance values must be positive."

    if configuration == "Parallel":
        return 1.0 / sum(1.0 / r for r in resistances)
    
    elif configuration == "Series":
        return sum(resistances)

    return "Error: Configuration must be 'Series' or 'Parallel'."


def main(page: ft.Page):
    page.title = "Physics Calculator"
    page.bgcolor = "#FCFBF4"
    page.window.width = 500
    page.window.height = 600
    page.window.resizable = False
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    title = ft.Text("Physics Calculator", color="black", size=30) 

    # Input Fields
    voltage_input = ft.TextField(label="Voltage (V)", width=200,color="black")
    current_input = ft.TextField(label="Current (A)", width=200,color="black")
    resistance_input = ft.TextField(label="Resistance (Ω)", width=200,color="black")
    capacitances_input = ft.TextField(label="Enter capacitances (comma-separated)", width=300,color="black")
    resistances_input = ft.TextField(label="Enter resistances (comma-separated)", width=300,color="black")
    capacitance_img=ft.Image(src="Capacitancia_paralelo.png",width=300,height=200)
    resistance_img=ft.Image(src="Resistencia_paralelo.png",width=300,height=200)
    
    def change_capacitance_img():
        match configuration_dropdown.value:
            case "Parallel":
                capacitance_img.src= "Capacitancia_paralelo.png"
            case "Series":
                capacitance_img.src="Capacitancia_serie.png"
        page.update()
    
    configuration_dropdown = ft.Dropdown(
        label="Configuration",
        options=[ft.dropdown.Option("Series"), ft.dropdown.Option("Parallel")],
        value="Parallel",
        width=200,
        color="black",
        on_change= lambda _ : change_capacitance_img()
    )
    configuration_dropdown_r = ft.Dropdown(
        label="Configuration",
        options=[ft.dropdown.Option("Series"), ft.dropdown.Option("Parallel")],
        value="Parallel",
        width=200,
        color="black",
        on_change= lambda _ : change_resistance_img()
    )
    
    def change_resistance_img():
        match configuration_dropdown_r.value:
            case"Parallel":
                resistance_img.src="Resistencia_paralelo.png" 
            case "Series":
                resistance_img.src="Resistencia_serie.png"
        page.update()
            

    # Result Texts
    ohms_result_text = ft.Text("", size=14,color="black")
    capacitance_result_text = ft.Text("", size=14,color="black")
    resistance_result_text = ft.Text("", size=14,color="black")

    # Calculation Functions
    def calculate_ohms_law(e):
        try:
            v, i, r = voltage_input.value, current_input.value, resistance_input.value
            filled_count = sum(1 for x in [v, i, r] if x)

            if filled_count != 2:
                ohms_result_text.value = "Enter exactly 2 values"
            else:
                v = float(v) if v else None
                i = float(i) if i else None
                r = float(r) if r else None
                
                if r and i:  
                    voltage_input.value = f"{i * r:.2f}"
                    ohms_result_text.value = f"Voltage = {i * r:.2f} V"
                elif v and i:  
                    resistance_input.value = f"{v / i:.2f}"
                    ohms_result_text.value = f"Resistance = {v / i:.2f} Ω"
                elif v and r:  
                    current_input.value = f"{v / r:.2f}"
                    ohms_result_text.value = f"Current = {v / r:.2f} A"

        except ZeroDivisionError:
            ohms_result_text.value = "Error: Cannot divide by zero"
        except ValueError:
            ohms_result_text.value = "Error: Invalid input"
        
        page.update()

    def on_calculate_capacitance(e):
        try:
            capacitances = [float(c.strip()) for c in capacitances_input.value.split(",")]
            result = calculate_capacitance(capacitances, configuration_dropdown.value)

            capacitance_result_text.value = f"Total Capacitance: {result:.2f} F" if isinstance(result, float) else result
        except ValueError:
            capacitance_result_text.value = "Error: Invalid input. Please enter numeric values."
        
        page.update()
    def on_calculate_resistance(e):
        try:
            resistances = [float(r.strip()) for r in resistances_input.value.split(",")]
            result = calculate_resistance(resistances, configuration_dropdown_r.value)

            resistance_result_text.value = f"Total Resistance: {result:.2f} F" if isinstance(result, float) else result
        except ValueError:
            resistance_result_text.value = "Error: Invalid input. Please enter numeric values."
        
        page.update()

    # Buttons
    ohms_calculate_button = ft.ElevatedButton("Calculate", on_click=calculate_ohms_law,style=ft.ButtonStyle(bgcolor="#849bff", color="white", shape=ft.RoundedRectangleBorder(radius=20)))
    capacitance_calculate_button = ft.ElevatedButton("Calculate", on_click=on_calculate_capacitance,style=ft.ButtonStyle(bgcolor="#849bff", color="white", shape=ft.RoundedRectangleBorder(radius=20)))
    resistance_calculate_button = ft.ElevatedButton("Calculate", on_click=on_calculate_resistance,style=ft.ButtonStyle(bgcolor="#849bff", color="white", shape=ft.RoundedRectangleBorder(radius=20)))

    # Pages
    home_view = ft.Container(
        content=ft.Column([title]),
        bgcolor="#FCFBF4",
        width=page.width,
        height=page.height,
        visible=True,
        alignment=ft.alignment.center
    )

    ohms_law_page = ft.Container(
        content=ft.Column([
            ft.Text("Ohm's Law Calculation", size=20,color="black"),
            voltage_input,
            current_input,
            resistance_input,
            ohms_calculate_button,
            ohms_result_text,
            ft.ElevatedButton("Back", on_click=lambda e: show_home(e),style=ft.ButtonStyle(bgcolor="#849bff", color="white", shape=ft.RoundedRectangleBorder(radius=20)))
        ],alignment=ft.alignment.center),
        bgcolor="#FCFBF4",
        width=page.width,
        height=page.height,
        visible=False,
        alignment=ft.alignment.center
    )

    capacitance_page = ft.Container(
        content=ft.Column([
            ft.Text("Capacitance Calculation", size=20,color="black"),
            capacitances_input,
            configuration_dropdown,
            capacitance_calculate_button,
            capacitance_img,
            capacitance_result_text,
            ft.ElevatedButton("Back", on_click=lambda e: show_home(e),style=ft.ButtonStyle(bgcolor="#849bff", color="white", shape=ft.RoundedRectangleBorder(radius=20)))
        ],alignment=ft.alignment.center),
        bgcolor="#FCFBF4",
        width=page.width,
        height=page.height,
        visible=False,
        alignment=ft.alignment.center
    )

    resistance_page = ft.Container(
        content=ft.Column([
            ft.Text("Resistance Calculation", size=20,color="black"),
            resistances_input,
            configuration_dropdown_r,
            resistance_calculate_button,
            resistance_img,
            resistance_result_text,
            ft.ElevatedButton("Back", on_click=lambda e: show_home(e),style=ft.ButtonStyle(bgcolor="#849bff", color="white", shape=ft.RoundedRectangleBorder(radius=20)))
        ],alignment=ft.alignment.center),
        bgcolor="#FCFBF4",
        width=page.width,
        height=page.height,
        visible=False,
        alignment=ft.alignment.center
    )

    # Navigation Functions
    def show_home(e):
        home_view.visible = True
        ohms_law_page.visible = False
        capacitance_page.visible = False
        resistance_page.visible = False
        page.update()

    def show_ohms_law(e):
        home_view.visible = False
        ohms_law_page.visible = True
        capacitance_page.visible = False
        resistance_page.visible = False
        page.update()

    def show_capacitance(e):
        home_view.visible = False
        ohms_law_page.visible = False
        capacitance_page.visible = True
        resistance_page.visible = False
        page.update()

    def show_resistance(e):
        home_view.visible = False
        ohms_law_page.visible = False
        capacitance_page.visible = False
        resistance_page.visible = True
        page.update()

    # Navigation Buttons
    ohms_law_button = ft.ElevatedButton(
        "Ohm's Law", on_click=show_ohms_law, width=200, height=50,
        style=ft.ButtonStyle(bgcolor="#849bff", color="white", shape=ft.RoundedRectangleBorder(radius=20))
    )
    capacitance_button = ft.ElevatedButton(
        "Capacitance", on_click=show_capacitance, width=200, height=50,
        style=ft.ButtonStyle(bgcolor="#849bff", color="white", shape=ft.RoundedRectangleBorder(radius=20))
    )
    resistance_button = ft.ElevatedButton(
        "Resistance", on_click=show_resistance, width=200, height=50,
        style=ft.ButtonStyle(bgcolor="#849bff", color="white", shape=ft.RoundedRectangleBorder(radius=20))
    )

    button_column = ft.Column([ohms_law_button, capacitance_button, resistance_button], spacing=40)
    home_view.content.controls.append(button_column)

    views = ft.Stack(controls=[home_view, ohms_law_page, capacitance_page, resistance_page])
    page.add(views)

ft.app(target=main)
