import flet as ft

# Capacitance calculation function from your previous version
def calculate_capacitance(capacitances, configuration):
    # Step 1: Check if the list is empty
    if len(capacitances) == 0:
        return "Error: At least one capacitance value is required."
    
    # Step 2: Check if all values are positive
    for c in capacitances:
        if c <= 0:
            return "Error: All capacitance values must be positive."
    
    # Step 3: Calculate based on configuration
    if configuration == "Parallel":
        # Initialize total capacitance for parallel
        total = 0.0
        # Loop through each capacitance and add it to total
        for c in capacitances:
            total = total + c
        return total
    
    elif configuration == "Series":
        # Initialize sum of reciprocals for series
        sum_of_reciprocals = 0.0
        # Loop through each capacitance, calculate reciprocal, and add to sum
        for c in capacitances:
            reciprocal = 1.0 / c
            sum_of_reciprocals = sum_of_reciprocals + reciprocal
        # Check for division by zero (shouldn't happen with positive values, but good practice)
        if sum_of_reciprocals == 0:
            return "Error: Sum of reciprocals is zero."
        # Calculate total capacitance as 1 / sum_of_reciprocals
        total = 1.0 / sum_of_reciprocals
        return total
    
    else:
        return "Error: Configuration must be 'Series' or 'Parallel'."

def main(page: ft.Page):
    page.title = "Physics Calculator"
    page.bgcolor = "#FCFBF4"
    page.window.height = 750
    page.window.width = 800
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START

    title = ft.Text("Physics Calculator", color="black", height=50)

    # **Ohm's Law Components**
    voltage_input = ft.TextField(label="Voltage (V)", width=150)
    current_input = ft.TextField(label="Current (I)", width=150)
    resistance_input = ft.TextField(label="Resistance (R)", width=150)
    ohms_result_text = ft.Text("")

    def calculate_ohms_law(e):
        try:
            v = voltage_input.value.strip()
            i = current_input.value.strip()
            r = resistance_input.value.strip()

            if v and i and not r:
                resistance_result = float(v) / float(i)
                ohms_result_text.value = f"Resistance = {resistance_result:.2f} Ohms"
            elif v and r and not i:
                current_result = float(v) / float(r)
                ohms_result_text.value = f"Current = {current_result:.2f} Amps"
            elif i and r and not v:
                voltage_result = float(i) * float(r)
                ohms_result_text.value = f"Voltage = {voltage_result:.2f} Volts"
            else:
                ohms_result_text.value = "Enter exactly two values"
        except ZeroDivisionError:
            ohms_result_text.value = "Error: Cannot divide by zero"
        except:
            ohms_result_text.value = "Error: Invalid input"
        page.update()

    ohms_calculate_button = ft.ElevatedButton("Calculate", on_click=calculate_ohms_law)

    # **Capacitance Components**
    capacitances_input = ft.TextField(label="Enter capacitances (comma-separated)", width=300)
    configuration_dropdown = ft.Dropdown(
        label="Configuration",
        options=[ft.dropdown.Option("Series"), ft.dropdown.Option("Parallel")],
        value="Parallel",
        width=200
    )
    capacitance_result_text = ft.Text("")

    def on_calculate_capacitance(e):
        input_str = capacitances_input.value.strip()
        if not input_str:
            capacitance_result_text.value = "Error: Please enter at least one capacitance value."
            page.update()
            return
        try:
            capacitances = [float(c.strip()) for c in input_str.split(",")]
        except ValueError:
            capacitance_result_text.value = "Error: Invalid input. Please enter numeric values."
            page.update()
            return
        configuration = configuration_dropdown.value
        result = calculate_capacitance(capacitances, configuration)
        # Handle the result: float (success) or string (error)
        if isinstance(result, float):
            capacitance_result_text.value = f"Total Capacitance: {result:.2f} F"
        else:
            capacitance_result_text.value = result
        page.update()

    capacitance_calculate_button = ft.ElevatedButton("Calculate", on_click=on_calculate_capacitance)

    # **Page Definitions**
    home_view = ft.Container(
        content=ft.Column([title]),
        bgcolor="#FCFBF4",
        width=page.width,
        height=600,
        visible=True
    )

    ohms_law_page = ft.Container(
        content=ft.Column([
            ft.Text("Ohm's Law Calculation"),
            voltage_input,
            current_input,
            resistance_input,
            ohms_calculate_button,
            ohms_result_text,
            ft.ElevatedButton("Back", on_click=lambda e: back(e))
        ]),
        bgcolor="#FCFBF4",
        width=page.width,
        height=600,
        visible=False
    )

    capacitance_page = ft.Container(
        content=ft.Column([
            ft.Text("Capacitance Calculation"),
            capacitances_input,
            configuration_dropdown,
            capacitance_calculate_button,
            capacitance_result_text,
            ft.ElevatedButton("Back", on_click=lambda e: back(e))
        ]),
        bgcolor="#FCFBF4",
        width=page.width,
        height=600,
        visible=False
    )

    # **Navigation Functions**
    def show_ohms_law(e):
        home_view.visible = False
        ohms_law_page.visible = True
        capacitance_page.visible = False
        page.update()

    def show_capacitance(e):
        home_view.visible = False
        ohms_law_page.visible = False
        capacitance_page.visible = True
        page.update()

    def back(e):
        home_view.visible = True
        ohms_law_page.visible = False
        capacitance_page.visible = False
        page.update()

    # Add navigation buttons to home view
    home_view.content.controls.append(
        ft.Column([
            ft.ElevatedButton("Ohm's Law", on_click=show_ohms_law, width=200, height=50),
            ft.ElevatedButton("Capacitance", on_click=show_capacitance, width=200, height=50)
        ], spacing=40)
    )

    # Stack all views
    views = ft.Stack(
        controls=[home_view, ohms_law_page, capacitance_page]
    )

    # Add to page
    page.add(views)

ft.app(target=main)