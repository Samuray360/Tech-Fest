import flet as ft

def main(page: ft.Page):
    page.title = "Physics Calculator"
    page.bgcolor = "#FCFBF4"
    page.window.height = 750
    page.window.width = 800
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    title = ft.Text("Physics Calculator", color="black", size=30)

    def ohms_law(e):
        def calculate(e):
            try:
                v = voltage.value.strip()
                i = current.value.strip()
                r = resistance.value.strip()
                
                filled_count = sum(1 for x in [v, i, r] if x)
                
                if filled_count != 2:
                    result.value = "Enter exactly 2 values"
                else:
                    v = float(v) if v else None
                    i = float(i) if i else None
                    r = float(r) if r else None
                    
                    if r and i:  
                        voltage_result = i * r
                        result.value = f"Voltage = {voltage_result:.2f} Volts"
                        voltage.value = str(voltage_result)
                    elif v and i:  
                        resistance_result = v / i
                        result.value = f"Resistance = {resistance_result:.2f} Ohms"
                        resistance.value = str(resistance_result)
                    elif v and r:  
                        current_result = v / r
                        result.value = f"Current = {current_result:.2f} Amps"
                        current.value = str(current_result)
                        
            except ZeroDivisionError:
                result.value = "Error: Cannot divide by zero"
            except ValueError:
                result.value = "Error: Invalid numbers"
            
            page.update()

        
        voltage = ft.TextField(label="Voltage (V)", width=150, height=40, text_size=12)
        current = ft.TextField(label="Current (A)", width=150, height=40, text_size=12)
        resistance = ft.TextField(label="Resistance (Ω)", width=150, height=40, text_size=12)
        result = ft.Text("", size=14)  
        
        dialog = ft.AlertDialog(
            title=ft.Text("Ohm's Law", size=16),  
            content=ft.Column([
                voltage,
                current,
                resistance,
                ft.ElevatedButton("Calculate", on_click=calculate, width=120, height=35),  
                result
            ], spacing=5, width=200),  
            actions=[ft.TextButton("Close", on_click=lambda e: setattr(dialog, "open", False) or page.update(), height=30)],
            actions_alignment=ft.MainAxisAlignment.END
        )
        
        page.overlay.append(dialog)
        dialog.open = True
        page.update()
        
    def capacitance():  
        pass
        
    def resistance():  
        pass

    ohms_law_button = ft.ElevatedButton(
        "Ohms law",
        on_click=ohms_law,
        width=200,
        height=50,
        style=ft.ButtonStyle(bgcolor="#849bff", color="white", shape=ft.RoundedRectangleBorder(radius=20))
    )
    capacitance_button = ft.ElevatedButton(
        "Capacitance",
        on_click=capacitance,
        width=200,
        height=50,
        style=ft.ButtonStyle(bgcolor="#849bff", color="white", shape=ft.RoundedRectangleBorder(radius=20))
    )
    resistance_button = ft.ElevatedButton(
        "Resistance",
        on_click=resistance,
        width=200,
        height=50,
        style=ft.ButtonStyle(bgcolor="#849bff", color="white", shape=ft.RoundedRectangleBorder(radius=20))
    )

    button_column = ft.Column([ohms_law_button, capacitance_button, resistance_button], spacing=40)

    page.add(title, button_column)

ft.app(target=main)