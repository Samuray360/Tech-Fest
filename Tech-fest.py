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

def calculate_magnetic_field(current, distance):
    """Calculates the magnetic field due to a straight current-carrying wire."""
    mu_0 = 1.2566370614359173e-6  # Permeability of free space in T·m/A
    if not isinstance(current, (int, float)) or not isinstance(distance, (int, float)):
        return "Error: Current and distance must be numeric."

    if distance <= 0:
        return "Error: Distance must be positive."

    try:
        return (mu_0 * current) / (2 * 3.141592653589793 * distance)
    except Exception:
        return "Error: Invalid current or distance."

def calculate_electric_force(charge1, charge2, distance):
    """Calculates the electric force between two point charges."""
    k = 8.99e9  # Coulomb's constant in N·m²/C²
    if not isinstance(charge1, (int, float)) or not isinstance(charge2, (int, float)) or not isinstance(distance, (int, float)):
        return "Error: Charges and distance must be numeric."

    if distance <= 0:
        return "Error: Distance must be positive."

    try:
        return k * abs(charge1 * charge2) / (distance ** 2)
    except Exception:
        return "Error: Invalid charges or distance."

def calculate_electric_field(charge, distance):
    """Calculates the electric field due to a point charge."""
    k = 8.99e9  # Coulomb's constant in N·m²/C²
    if not isinstance(charge, (int, float)) or not isinstance(distance, (int, float)):
        return "Error: Charge and distance must be numeric."

    if distance <= 0:
        return "Error: Distance must be positive."

    try:
        return k * charge / (distance ** 2)
    except Exception:
        return "Error: Invalid charge or distance."


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
    page.window.width = page.width
    page.window.height = page.height
    page.window.resizable = False
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    title = ft.Text("Physics Calculator", color="black", size=30) 
    explanation=""
    # Input Fields
    voltage_input = ft.TextField(label="Voltage (V)", width=200,color="black")
    current_input = ft.TextField(label="Current (A)", width=200,color="black")
    resistance_input = ft.TextField(label="Resistance (Ω)", width=200,color="black")
    capacitances_input = ft.TextField(label="Enter capacitances (comma-separated)", width=300,color="black")
    resistances_input = ft.TextField(label="Enter resistances (comma-separated)", width=300,color="black")
    capacitance_img=ft.Image(src="Capacitancia_paralelo.png",width=300,height=200)
    resistance_img=ft.Image(src="Resistencia_paralelo.png",width=300,height=200)

    # Text explanations
    ohmslaw_explanation= ft.Container(
                content=ft.Column([ft.Text("Ohm's Law", size=24, weight="bold"),
                ft.Text("Ohm's Law relates voltage (V), current (I), and resistance (R) in a circuit."),
                ft.Text("Formula: V = I x R")]),
                bgcolor="#849bff",visible=False
                )
    Capacitance_explanation=ft.Container(
                content=ft.Column([ft.Text("Capacitance", size=24, weight="bold"),
                ft.Text("Capacitance is the ability to store electric charge per unit voltage."),
                ft.Text("Formula: C = Q / V")]),
                bgcolor="#849bff",visible=False
                )
    Resistance_explanation=ft.Container(
                content=ft.Column([ft.Text("Resistance", size=24, weight="bold"),
                ft.Text("Resistance measures how much a material opposes electric current."),
                ft.Text("Formula: R = p x (L / A)")]),
                bgcolor="#849bff",visible=False
    )
    vectors_explanation=ft.Container(
                content=ft.Column([ft.Text("Vectors", size=24, weight="bold"),
                ft.Text("Vectors have both magnitude and direction."),
                ft.Text("Magnitude Formula: |v| = √(vx² + vy² + vz²)"),
                ft.Text("Dot Product: A • B = AxBx + AyBy + AzBz"),
                ft.Text("Cross Product: A x B = (AyBz - AzBy)i - (AxBz - AzBx)j + (AxBy - AyBx)k")]),
                bgcolor="#849bff",visible=False
    )
    magneticfield_explanation=ft.Container(
                content=ft.Column([ft.Text("Magnetic Field", size=24, weight="bold"),
                ft.Text("The magnetic field describes the magnetic influence of electric currents."),
                ft.Text("Formula (Straight Wire): B = (μ₀ × I) / (2πr)")]),
                bgcolor="#849bff",visible=False
    )
    electricfield_explanation=ft.Container(
                content=ft.Column([ft.Text("Electric Field", size=24, weight="bold"),
                ft.Text("Electric fields show the force per unit charge in space."),
                ft.Text("Formula (Point Charge): E = F/Q")]),
                bgcolor="#849bff",visible=False
    )
    explanation_add=ft.Stack(controls=[ohmslaw_explanation,Capacitance_explanation,Resistance_explanation,vectors_explanation,magneticfield_explanation,electricfield_explanation])
    
    explanations = {
        "ohms_law": ohmslaw_explanation,
        "capacitance": Capacitance_explanation,
        "resistance": Resistance_explanation,
        "vectors": vectors_explanation,
        "magneticfield": magneticfield_explanation,
        "electricfield": electricfield_explanation
    }

    def show_explanation():  
        global explanation
        
        for exp in explanations.values():
            exp.visible = False
       
        if explanation in explanations:
            explanations[explanation].visible = True
        page.update()
    
    def hide_explanation(e=None):  # Optional event parameter
        for exp in explanations.values():
            exp.visible = False
        page.update()

    hide_button = ft.ElevatedButton(
        "Hide",
        on_click=hide_explanation,
        style=ft.ButtonStyle(bgcolor="#849bff", color="white", shape=ft.RoundedRectangleBorder(radius=20))
    )
    show_explanation_button = ft.ElevatedButton(
        "Explanation",
        on_click=show_explanation,
        style=ft.ButtonStyle(bgcolor="#849bff", color="white", shape=ft.RoundedRectangleBorder(radius=20))
    )

    # Add unique hide buttons to each explanation
    for exp in explanations.values():
        exp.content.controls.append(
            ft.ElevatedButton(
                "Hide",
                on_click=hide_explanation,
                style=ft.ButtonStyle(bgcolor="#849bff", color="white", shape=ft.RoundedRectangleBorder(radius=20))
            )
        )

    hide_button=ft.ElevatedButton("Hide", on_click=hide_explanation,style=ft.ButtonStyle(bgcolor="#849bff", color="white", shape=ft.RoundedRectangleBorder(radius=20)))
    
    show_explanation_button=ft.ElevatedButton("Explanation", on_click=show_explanation,style=ft.ButtonStyle(bgcolor="#849bff", color="white", shape=ft.RoundedRectangleBorder(radius=20)))
    
    ohmslaw_explanation.content.controls.append(hide_button)
    Capacitance_explanation.content.controls.append(hide_button)
    Resistance_explanation.content.controls.append(hide_button)
    vectors_explanation.content.controls.append(hide_button)
    magneticfield_explanation.content.controls.append(hide_button)
    electricfield_explanation.content.controls.append(hide_button)

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
    vectors_calculate_button = ft.ElevatedButton("Calculate", on_click=on_calculate_resistance,style=ft.ButtonStyle(bgcolor="#849bff", color="white", shape=ft.RoundedRectangleBorder(radius=20)))
    magneticfield_calculate_button = ft.ElevatedButton("Calculate", on_click=on_calculate_resistance,style=ft.ButtonStyle(bgcolor="#849bff", color="white", shape=ft.RoundedRectangleBorder(radius=20)))
    electricfield_calculate_button = ft.ElevatedButton("Calculate", on_click=on_calculate_resistance,style=ft.ButtonStyle(bgcolor="#849bff", color="white", shape=ft.RoundedRectangleBorder(radius=20)))
    
    # Pages
    home_view = ft.Container(
        content=ft.Column([title],alignment=ft.alignment.center),
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
            ohmslaw_explanation,
            ohms_calculate_button,
            ohms_result_text,
            show_explanation_button,
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
            Capacitance_explanation,
            capacitance_img,
            capacitance_result_text,
            show_explanation_button,
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
            Resistance_explanation,
            resistance_result_text,
            show_explanation_button,
            ft.ElevatedButton("Back", on_click=lambda e: show_home(e),style=ft.ButtonStyle(bgcolor="#849bff", color="white", shape=ft.RoundedRectangleBorder(radius=20)))
        ],alignment=ft.alignment.center),
        bgcolor="#FCFBF4",
        width=page.width,
        height=page.height,
        visible=False,
        alignment=ft.alignment.center
    )
    
    vectors_page = ft.Container(
        content=ft.Column([
            ft.Text("Vectors Calculation", size=20,color="black"),
            vectors_calculate_button,
            vectors_explanation,
            show_explanation_button,
            ft.ElevatedButton("Back", on_click=lambda e: show_home(e),style=ft.ButtonStyle(bgcolor="#849bff", color="white", shape=ft.RoundedRectangleBorder(radius=20)))
        ],alignment=ft.alignment.center),
        bgcolor="#FCFBF4",
        width=page.width,
        height=page.height,
        visible=False,
        alignment=ft.alignment.center
    )
    
    magneticfield_page = ft.Container(
        content=ft.Column([
            ft.Text("Magnetic Field Calculation", size=20,color="black"),
           magneticfield_calculate_button,
           magneticfield_explanation,
           show_explanation_button,
            ft.ElevatedButton("Back", on_click=lambda e: show_home(e),style=ft.ButtonStyle(bgcolor="#849bff", color="white", shape=ft.RoundedRectangleBorder(radius=20)))
        ],alignment=ft.alignment.center),
        bgcolor="#FCFBF4",
        width=page.width,
        height=page.height,
        visible=False,
        alignment=ft.alignment.center
    )

    electricfield_page=ft.Container(
        content=ft.Column([
            ft.Text("Electric Field Calculation", size=20,color="black"),
            electricfield_calculate_button,
            electricfield_explanation,
            show_explanation_button,
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
        magneticfield_page.visible=False
        electricfield_page.visible=False
        vectors_page.visible=False
        page.update()

    def show_ohms_law(e):
        explanation="ohms_law"
        home_view.visible = False
        ohms_law_page.visible = True
        capacitance_page.visible = False
        resistance_page.visible = False
        magneticfield_page.visible=False
        electricfield_page.visible=False
        vectors_page.visible=False
        page.update()

    def show_capacitance(e):
        explanation="capacitance"
        home_view.visible = False
        ohms_law_page.visible = False
        capacitance_page.visible = True
        resistance_page.visible = False
        magneticfield_page.visible=False
        electricfield_page.visible=False
        vectors_page.visible=False
        page.update()

    def show_resistance(e):
        explanation="resistance"
        home_view.visible = False
        ohms_law_page.visible = False
        capacitance_page.visible = False
        resistance_page.visible = True
        magneticfield_page.visible=False
        electricfield_page.visible=False
        vectors_page.visible=False
        page.update()

    def show_vectors(e):
        explanation="vectors"
        home_view.visible = False
        ohms_law_page.visible = False
        capacitance_page.visible = False
        resistance_page.visible = False
        magneticfield_page.visible=False
        electricfield_page.visible=False
        vectors_page.visible=True
        page.update()
    
    def show_magneticfield(e):
        explanation="magneticfield"
        home_view.visible = False
        ohms_law_page.visible = False
        capacitance_page.visible = False
        resistance_page.visible = False
        vectors_page.visible=False
        electricfield_page.visible=False
        magneticfield_page.visible=True

        page.update()
    
    def show_electricfield(e):
        explanation="electricfield"
        home_view.visible = False
        ohms_law_page.visible = False
        capacitance_page.visible = False
        resistance_page.visible = False
        vectors_page.visible=False
        magneticfield_page.visible=False
        electricfield_page.visible=True

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
    vectors_button = ft.ElevatedButton(
        "Vectors", on_click=show_vectors, width=200, height=50,
        style=ft.ButtonStyle(bgcolor="#849bff", color="white", shape=ft.RoundedRectangleBorder(radius=20))
    )
    magneticfield_button = ft.ElevatedButton(
        "Magnetic Field", on_click=show_magneticfield, width=200, height=50,
        style=ft.ButtonStyle(bgcolor="#849bff", color="white", shape=ft.RoundedRectangleBorder(radius=20))
    )
    electricfield_button = ft.ElevatedButton(
        "Electric Field", on_click=show_electricfield, width=200, height=50,
        style=ft.ButtonStyle(bgcolor="#849bff", color="white", shape=ft.RoundedRectangleBorder(radius=20))
    )
    
    button_column = ft.Row([
        ft.Column([
            ohms_law_button,
            capacitance_button,
            resistance_button,
            vectors_button,
            magneticfield_button,
            electricfield_button,
        ])
    ])

    home_view.content.controls.append(button_column)

    views = ft.Stack(controls=[home_view, ohms_law_page, capacitance_page, resistance_page,vectors_page,magneticfield_page,electricfield_page])
    final_view=ft.Stack(controls=[views,explanation_add])
    page.add(final_view)
    
ft.app(target=main)
