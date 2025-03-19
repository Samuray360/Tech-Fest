import flet as ft

def main(page: ft.Page):
    page.title = "Physic's calculator"
    page.bgcolor = "#FCFBF4"
    page.window.height = 750
    page.window.width = 800
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START

    title=ft.Text("Physic's calculator",color="black",height=50) 
    user_input=ft.TextField()
    
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
    def equivalent_formula():
        ft.Column([
            ft.Container(
            print(1),
            ft.Divider(height=1,color="black"),
            user_input
            )
        ])
    ohms_law_page=ft.Container(
       
        width=page.width,
        height=page.width,
        
    )
    capacitance_page=ft.Container(   
        equivalent_formula(),
        width=page.width,
        height=page.width,
    )
    resistance_page=ft.Container(   
        equivalent_formula(),
        width=page.width,
        height=page.width,
    )

  

    def ohms_law_view():#diego
        ohms_law_page.visible=True
        capacitance_page.visible=False
        resistance_page.visible=False
    def capacitance_view():#carlos , ethan
        ohms_law_page.visible=False
        capacitance_page.visible=True
        resistance_page.visible=False
        equivalent_formula
        return
    def resistance_view():#carlos , ethan
        ohms_law_page.visible=False
        capacitance_page.visible=False
        resistance_page.visible=True
        equivalent_formula
        return
    
  

    
    ohms_law_button=ft.ElevatedButton("Ohms law",on_click=ohms_law_view,width=200,height=50,style=ft.ButtonStyle(bgcolor="#849bff",color="white"),)
    capacitance_button=ft.ElevatedButton("Capacitance",on_click=capacitance_view,width=200,height=50,style=ft.ButtonStyle(bgcolor="#849bff",color="white"))
    resistance_button=ft.ElevatedButton("Resistance",on_click=resistance_view,width=200,height=50,style=ft.ButtonStyle(bgcolor="#849bff",color="white"))

    button_column=ft.Column([ohms_law_button,capacitance_button,resistance_button],spacing=40)

    page.add(title,button_column)

ft.app(target=main)