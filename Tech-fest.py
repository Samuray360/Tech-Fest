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
    page.window.maximized = True  
    page.window.resizable = True
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    title = ft.Text("Physics Calculator", color="black", size=30,)

    # Input Fields
    voltage_input = ft.TextField(label="Voltage (V)", width=200, color="black")
    current_input = ft.TextField(label="Current (A)", width=200, color="black")
    resistance_input = ft.TextField(label="Resistance (Ω)", width=200, color="black")
    capacitances_input = ft.TextField(label="Enter capacitances (comma-separated)", width=300, color="black")
    resistances_input = ft.TextField(label="Enter resistances (comma-separated)", width=300, color="black")
    current_magnetic_field = ft.TextField(label="Current (A)", width=200, color="black")
    distance_magnetic_field = ft.TextField(label="Distance (m)", width=200, color="black")
    charge1 = ft.TextField(label="Charge 1 (C)", width=200, color="black")
    charge2 = ft.TextField(label="Charge 2 (C)", width=200, color="black")
    distance = ft.TextField(label="Distance (m)", width=200, color="black")
    charge1_electric_field = ft.TextField(label="Charge (C)", width=200, color="black")
    distance_electric_field = ft.TextField(label="Distance (m)", width=200, color="black")
    capacitance_img = ft.Image(src="Capacitancia_paralelo.png", width=300, height=200, visible=False)
    resistance_img = ft.Image(src="Resistencia_paralelo.png", width=300, height=200, visible=False)

    # Result Texts
    ohms_result_text = ft.Text("", size=14, color="black")
    capacitance_result_text = ft.Text("", size=14, color="black")
    resistance_result_text = ft.Text("", size=14, color="black")
    electric_force_result_text = ft.Text("", size=14, color="black")
    magnetic_field_result_text = ft.Text("", size=14, color="black")
    electric_field_result_text = ft.Text("", size=14, color="black")

    # Text Explanations
    ohmslaw_explanation = ft.Container(
        content=ft.Column([
            ft.Text("Ohm's Law", size=24, weight="bold"),
            ft.Text("Ohm's Law relates voltage (V), current (I), and resistance (R) in a circuit."),
            ft.Text("Formula: V = I x R")
        ]),
        bgcolor="#849bff", visible=False, padding=10, border_radius=10
    )
    capacitance_explanation = ft.Container(
        content=ft.Column([
            ft.Text("Capacitance", size=24, weight="bold"),
            ft.Text("Capacitance is the ability to store electric charge per unit voltage."),
            ft.Text("Formula: C = Q / V")
        ]),
        bgcolor="#849bff", visible=False, padding=10, border_radius=10
    )
    resistance_explanation = ft.Container(
        content=ft.Column([
            ft.Text("Resistance", size=24, weight="bold"),
            ft.Text("Resistance measures how much a material opposes electric current."),
            ft.Text("Formula: R = ρ x (L / A)")
        ]),
        bgcolor="#849bff", visible=False, padding=10, border_radius=10
    )
    electric_force_explanation = ft.Container(
        content=ft.Column([
            ft.Text("Electric Force", size=24, weight="bold"),
            ft.Text("Electric force is the interaction between charged particles."),
            ft.Text("Like charges repel; opposite charges attract."),
            ft.Text("Coulomb's Law: F = k * |q1 * q2| / r²"),
            ft.Text("Where:"),
            ft.Text("• F is the electric force"),
            ft.Text("• q1 and q2 are the charges"),
            ft.Text("• r is the distance between charges"),
            ft.Text("• k ≈ 8.99 × 10⁹ N·m²/C² (Coulomb's constant)")
        ]),
        bgcolor="#849bff", visible=False, padding=10, border_radius=10
    )
    magneticfield_explanation = ft.Container(
        content=ft.Column([
            ft.Text("Magnetic Field", size=24, weight="bold"),
            ft.Text("The magnetic field describes the magnetic influence of electric currents."),
            ft.Text("Formula (Straight Wire): B = (μ₀ × I) / (2πr)")
        ]),
        bgcolor="#849bff", visible=False, padding=10, border_radius=10
    )
    electricfield_explanation = ft.Container(
        content=ft.Column([
            ft.Text("Electric Field", size=24, weight="bold"),
            ft.Text("Electric fields show the force per unit charge in space."),
            ft.Text("Formula (Point Charge): E = k * q / r²")
        ]),
        bgcolor="#849bff", visible=False, padding=10, border_radius=10
    )

    # Explanation Management
    current_explanation = ft.Ref[ft.Container]()

    def show_explanation(explanation_container):
        if current_explanation.current:
            current_explanation.current.visible = False
        current_explanation.current = explanation_container
        explanation_container.visible = True
        page.update()

    def hide_explanation(e=None):
        if current_explanation.current:
            current_explanation.current.visible = False
            current_explanation.current = None
        page.update()

    # Add Hide Button to Explanations
    for exp in [ohmslaw_explanation, capacitance_explanation, resistance_explanation,
                electric_force_explanation, magneticfield_explanation, electricfield_explanation]:
        exp.content.controls.append(
            ft.ElevatedButton(
                "Hide",
                on_click=hide_explanation,
                style=ft.ButtonStyle(bgcolor="#849bff", color="white", shape=ft.RoundedRectangleBorder(radius=20))
            )
        )

    # Dropdown for Configurations
    configuration_dropdown = ft.Dropdown(
        label="Configuration",
        options=[ft.dropdown.Option("Series"), ft.dropdown.Option("Parallel")],
        value="Parallel",
        width=200,
        color="black",
        on_change=lambda _: change_capacitance_img()
    )
    configuration_dropdown_r = ft.Dropdown(
        label="Configuration",
        options=[ft.dropdown.Option("Series"), ft.dropdown.Option("Parallel")],
        value="Parallel",
        width=200,
        color="black",
        on_change=lambda _: change_resistance_img()
    )

    def change_capacitance_img():
        capacitance_img.src = "Capacitancia_paralelo.png" if configuration_dropdown.value == "Parallel" else "Capacitancia_serie.png"
        capacitance_img.visible = True
        page.update()

    def change_resistance_img():
        resistance_img.src = "Resistencia_paralelo.png" if configuration_dropdown_r.value == "Parallel" else "Resistencia_serie.png"
        resistance_img.visible = True
        page.update()

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
            capacitance_result_text.value = "Error: Invalid input. Please enter numeric valuesaccident."
        page.update()

    def on_calculate_resistance(e):
        try:
            resistances = [float(r.strip()) for r in resistances_input.value.split(",")]
            result = calculate_resistance(resistances, configuration_dropdown_r.value)
            resistance_result_text.value = f"Total Resistance: {result:.2f} Ω" if isinstance(result, float) else result
        except ValueError:
            resistance_result_text.value = "Error: Invalid input. Please enter numeric values."
        page.update()

    def on_calculate_electric_force(e):
        try:
            q1 = float(charge1.value)
            q2 = float(charge2.value)
            d = float(distance.value)
            result = calculate_electric_force(q1, q2, d)
            electric_force_result_text.value = f"Electric Force: {result:.2e} N" if isinstance(result, float) else result
        except ValueError:
            electric_force_result_text.value = "Error: Invalid input. Please enter numeric values."
        page.update()

    def on_calculate_magnetic_field(e):
        try:
            i = float(current_magnetic_field.value)
            d = float(distance_magnetic_field.value)
            result = calculate_magnetic_field(i, d)
            magnetic_field_result_text.value = f"Magnetic Field: {result:.2e} T" if isinstance(result, float) else result
        except ValueError:
            magnetic_field_result_text.value = "Error: Invalid input. Please enter numeric values."
        page.update()

    def on_calculate_electric_field(e):
        try:
            q = float(charge1_electric_field.value)
            d = float(distance_electric_field.value)
            result = calculate_electric_field(q, d)
            electric_field_result_text.value = f"Electric Field: {result:.2e} N/C" if isinstance(result, float) else result
        except ValueError:
            electric_field_result_text.value = "Error: Invalid input. Please enter numeric values."
        page.update()

    # Buttons
    ohms_calculate_button = ft.ElevatedButton(
        "Calculate", on_click=calculate_ohms_law,
        style=ft.ButtonStyle(bgcolor="#849bff", color="white", shape=ft.RoundedRectangleBorder(radius=20))
    )
    capacitance_calculate_button = ft.ElevatedButton(
        "Calculate", on_click=on_calculate_capacitance,
        style=ft.ButtonStyle(bgcolor="#849bff", color="white", shape=ft.RoundedRectangleBorder(radius=20))
    )
    resistance_calculate_button = ft.ElevatedButton(
        "Calculate", on_click=on_calculate_resistance,
        style=ft.ButtonStyle(bgcolor="#849bff", color="white", shape=ft.RoundedRectangleBorder(radius=20))
    )
    electric_force_calculate_button = ft.ElevatedButton(
        "Calculate", on_click=on_calculate_electric_force,
        style=ft.ButtonStyle(bgcolor="#849bff", color="white", shape=ft.RoundedRectangleBorder(radius=20))
    )
    magneticfield_calculate_button = ft.ElevatedButton(
        "Calculate", on_click=on_calculate_magnetic_field,
        style=ft.ButtonStyle(bgcolor="#849bff", color="white", shape=ft.RoundedRectangleBorder(radius=20))
    )
    electricfield_calculate_button = ft.ElevatedButton(
        "Calculate", on_click=on_calculate_electric_field,
        style=ft.ButtonStyle(bgcolor="#849bff", color="white", shape=ft.RoundedRectangleBorder(radius=20))
    )

    # Pages
    home_view = ft.Container(
    content=ft.Column([
        title,
        ft.ResponsiveRow([
            ft.Column([
                ft.ElevatedButton(
                    "Ohm's Law", on_click=lambda e: show_page(ohms_law_page, ohmslaw_explanation),
                    width=400, height=120, style=ft.ButtonStyle(bgcolor="#849bff", color="white", shape=ft.RoundedRectangleBorder(radius=20))
                ),
                ft.ElevatedButton(
                    "Capacitance", on_click=lambda e: show_page(capacitance_page, capacitance_explanation),
                    width=400, height=120, style=ft.ButtonStyle(bgcolor="#849bff", color="white", shape=ft.RoundedRectangleBorder(radius=20))
                ),
                ft.ElevatedButton(
                    "Resistance", on_click=lambda e: show_page(resistance_page, resistance_explanation),
                    width=400, height=120, style=ft.ButtonStyle(bgcolor="#849bff", color="white", shape=ft.RoundedRectangleBorder(radius=20))
                ),
            ], spacing=20, alignment=ft.MainAxisAlignment.CENTER, col={"sm": 6, "md": 6, "lg": 6}),
            ft.Column([
                ft.ElevatedButton(
                    "Electric Force", on_click=lambda e: show_page(electric_force_page, electric_force_explanation),
                    width=400, height=120, style=ft.ButtonStyle(bgcolor="#849bff", color="white", shape=ft.RoundedRectangleBorder(radius=20))
                ),
                ft.ElevatedButton(
                    "Magnetic Field", on_click=lambda e: show_page(magneticfield_page, magneticfield_explanation),
                    width=400, height=120, style=ft.ButtonStyle(bgcolor="#849bff", color="white", shape=ft.RoundedRectangleBorder(radius=20))
                ),
                ft.ElevatedButton(
                    "Electric Field", on_click=lambda e: show_page(electricfield_page, electricfield_explanation),
                    width=400, height=120, style=ft.ButtonStyle(bgcolor="#849bff", color="white", shape=ft.RoundedRectangleBorder(radius=20))
                ),
            ], spacing=20, alignment=ft.MainAxisAlignment.CENTER, col={"sm": 6, "md": 6, "lg": 6}),
        ], alignment=ft.MainAxisAlignment.CENTER, spacing=20),
    ], alignment=ft.MainAxisAlignment.CENTER, spacing=30),
    bgcolor="#FCFBF4",
    width=page.window.width,
    height=page.window.height,
    visible=True,
    alignment=ft.alignment.center,
    padding=ft.padding.symmetric(vertical=50, horizontal=20)
)

    ohms_law_page = ft.Container(
        content=ft.Column([
            ft.Text("Ohm's Law Calculation", size=20, color="black"),
            voltage_input,
            current_input,
            resistance_input,
            ohms_calculate_button,
            ohms_result_text,
            ft.ElevatedButton(
                "Show Explanation", on_click=lambda e: show_explanation(ohmslaw_explanation),
                style=ft.ButtonStyle(bgcolor="#849bff", color="white", shape=ft.RoundedRectangleBorder(radius=20))
            ),
            ohmslaw_explanation,
            ft.ElevatedButton(
                "Back", on_click=lambda e: show_page(home_view, None),
                style=ft.ButtonStyle(bgcolor="#849bff", color="white", shape=ft.RoundedRectangleBorder(radius=20))
            )
        ], alignment=ft.alignment.center),
        bgcolor="#FCFBF4",
        width=page.window.width,
        height=page.window.height,
        visible=False,
        alignment=ft.alignment.center
    )

    capacitance_page = ft.Container(
        content=ft.Column([
            ft.Text("Capacitance Calculation", size=20, color="black"),
            capacitances_input,
            configuration_dropdown,
            capacitance_img,
            capacitance_calculate_button,
            capacitance_result_text,
            ft.ElevatedButton(
                "Show Explanation", on_click=lambda e: show_explanation(capacitance_explanation),
                style=ft.ButtonStyle(bgcolor="#849bff", color="white", shape=ft.RoundedRectangleBorder(radius=20))
            ),
            capacitance_explanation,
            ft.ElevatedButton(
                "Back", on_click=lambda e: show_page(home_view, None),
                style=ft.ButtonStyle(bgcolor="#849bff", color="white", shape=ft.RoundedRectangleBorder(radius=20))
            )
        ], alignment=ft.alignment.center),
        bgcolor="#FCFBF4",
        width=page.window.width,
        height=page.window.height,
        visible=False,
        alignment=ft.alignment.center
    )

    resistance_page = ft.Container(
        content=ft.Column([
            ft.Text("Resistance Calculation", size=20, color="black"),
            resistances_input,
            configuration_dropdown_r,
            resistance_img,
            resistance_calculate_button,
            resistance_result_text,
            ft.ElevatedButton(
                "Show Explanation", on_click=lambda e: show_explanation(resistance_explanation),
                style=ft.ButtonStyle(bgcolor="#849bff", color="white", shape=ft.RoundedRectangleBorder(radius=20))
            ),
            resistance_explanation,
            ft.ElevatedButton(
                "Back", on_click=lambda e: show_page(home_view, None),
                style=ft.ButtonStyle(bgcolor="#849bff", color="white", shape=ft.RoundedRectangleBorder(radius=20))
            )
        ], alignment=ft.alignment.center),
        bgcolor="#FCFBF4",
        width=page.window.width,
        height=page.window.height,
        visible=False,
        alignment=ft.alignment.center
    )

    electric_force_page = ft.Container(
        content=ft.Column([
            ft.Text("Electric Force Calculation", size=20, color="black"),
            charge1,
            charge2,
            distance,
            electric_force_calculate_button,
            electric_force_result_text,
            ft.ElevatedButton(
                "Show Explanation", on_click=lambda e: show_explanation(electric_force_explanation),
                style=ft.ButtonStyle(bgcolor="#849bff", color="white", shape=ft.RoundedRectangleBorder(radius=20))
            ),
            electric_force_explanation,
            ft.ElevatedButton(
                "Back", on_click=lambda e: show_page(home_view, None),
                style=ft.ButtonStyle(bgcolor="#849bff", color="white", shape=ft.RoundedRectangleBorder(radius=20))
            )
        ], alignment=ft.alignment.center),
        bgcolor="#FCFBF4",
        width=page.window.width,
        height=page.window.height,
        visible=False,
        alignment=ft.alignment.center
    )

    magneticfield_page = ft.Container(
        content=ft.Column([
            ft.Text("Magnetic Field Calculation", size=20, color="black"),
            current_magnetic_field,
            distance_magnetic_field,
            magneticfield_calculate_button,
            magnetic_field_result_text,
            ft.ElevatedButton(
                "Show Explanation", on_click=lambda e: show_explanation(magneticfield_explanation),
                style=ft.ButtonStyle(bgcolor="#849bff", color="white", shape=ft.RoundedRectangleBorder(radius=20))
            ),
            magneticfield_explanation,
            ft.ElevatedButton(
                "Back", on_click=lambda e: show_page(home_view, None),
                style=ft.ButtonStyle(bgcolor="#849bff", color="white", shape=ft.RoundedRectangleBorder(radius=20))
            )
        ], alignment=ft.alignment.center),
        bgcolor="#FCFBF4",
        width=page.window.width,
        height=page.window.height,
        visible=False,
        alignment=ft.alignment.center
    )

    electricfield_page = ft.Container(
        content=ft.Column([
            ft.Text("Electric Field Calculation", size=20, color="black"),
            charge1_electric_field,
            distance_electric_field,
            electricfield_calculate_button,
            electric_field_result_text,
            ft.ElevatedButton(
                "Show Explanation", on_click=lambda e: show_explanation(electricfield_explanation),
                style=ft.ButtonStyle(bgcolor="#849bff", color="white", shape=ft.RoundedRectangleBorder(radius=20))
            ),
            electricfield_explanation,
            ft.ElevatedButton(
                "Back", on_click=lambda e: show_page(home_view, None),
                style=ft.ButtonStyle(bgcolor="#849bff", color="white", shape=ft.RoundedRectangleBorder(radius=20))
            )
        ], alignment=ft.alignment.center),
        bgcolor="#FCFBF4",
        width=page.window.width,
        height=page.window.height,
        visible=False,
        alignment=ft.alignment.center
    )

    # Navigation Function
    def show_page(page_to_show, explanation_container):
        for p in [home_view, ohms_law_page, capacitance_page, resistance_page,
                  electric_force_page, magneticfield_page, electricfield_page]:
            p.visible = False
        page_to_show.visible = True
        hide_explanation()
        if explanation_container:
            show_explanation(explanation_container)
        page.update()

    # Stack Views
    views = ft.Stack(controls=[
        home_view, ohms_law_page, capacitance_page, resistance_page,
        electric_force_page, magneticfield_page, electricfield_page
    ])
    page.add(views)

ft.app(target=main)