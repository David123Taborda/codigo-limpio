import sys
sys.path.append("src")
import kivy 
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


from src.model.Calculadora import (
    calcular_ingreso_total_anual,
    calcular_deducciones_por_ley,
    calcular_deducciones_personales,
    calcular_renta_exenta,
    calcular_base_gravable,
    ErrorValorNegativo,
    ErrorTipoDato,
)

class CalculadoraScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.inputs = {}


        campos = [
            ('Sueldo mensual', 'sueldo'),
            ('Otros ingresos', 'otros_ingresos'),
            ('Aporte a pensión', 'aporte_pension'),
            ('Intereses crédito vivienda', 'credito_vivienda'),
            ('Gastos médicos', 'gasto_medicina'),
            ('Personas a cargo', 'personas_a_cargo'),
            ('Patrimonio', 'patrimonio')
        ]
        for texto, clave in campos:
            box = BoxLayout(orientation='horizontal', size_hint_y=None, height=30)
            box.add_widget(Label(text=texto, size_hint_x=0.6))
            entrada = TextInput(multiline=False, input_filter='float')
            self.inputs[clave] = entrada
            box.add_widget(entrada)
            self.add_widget(box)

        # Botón para calcular
        btn = Button(text='Calcular', size_hint_y=None, height=40)
        btn.bind(on_press=self.calcular)
        self.add_widget(btn)


        self.resultado = Label(text='', size_hint_y=None, height=120)
        self.add_widget(self.resultado)

    def calcular(self, instance):
        try:

            sueldo = float(self.inputs['sueldo'].text or 0)
            otros_ingresos = float(self.inputs['otros_ingresos'].text or 0)
            aporte_pension = float(self.inputs['aporte_pension'].text or 0)
            credito_vivienda = float(self.inputs['credito_vivienda'].text or 0)
            gasto_medicina = float(self.inputs['gasto_medicina'].text or 0)
            personas_a_cargo = int(float(self.inputs['personas_a_cargo'].text or 1))
            patrimonio = float(self.inputs['patrimonio'].text or 0)

            ingresos_totales = calcular_ingreso_total_anual(
                sueldo, otros_ingresos, personas_a_cargo, patrimonio
            )
            deducciones_ley = calcular_deducciones_por_ley(aporte_pension)
            deducciones_personales = calcular_deducciones_personales(
                credito_vivienda, gasto_medicina
            )
            renta_exenta = calcular_renta_exenta(ingresos_totales, deducciones_ley)
            base_gravable = calcular_base_gravable(
                ingresos_totales, deducciones_ley, deducciones_personales, renta_exenta
            )

            self.resultado.text = (
                f"Ingreso total anual: {ingresos_totales:.2f}\n"
                f"Deducciones por ley: {deducciones_ley:.2f}\n"
                f"Deducciones personales: {deducciones_personales:.2f}\n"
                f"Renta exenta (25%): {renta_exenta:.2f}\n"
                f"Base gravable para impuesto: {base_gravable:.2f}"
            )
        except (ValueError, ErrorValorNegativo, ErrorTipoDato) as e:
            self.resultado.text = f"Error: {str(e)}"

class CalculadoraApp(App):
    def build(self):
        return CalculadoraScreen()

if __name__ == '__main__':
    CalculadoraApp().run()