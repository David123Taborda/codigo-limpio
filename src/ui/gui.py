from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.core.window import Window
import sys
import os

# Tamaño fijo de ventana
Window.size = (600, 900)

# Asegurar importaciones desde src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from controller.CalculadoraController import CalculadoraController


class CalculadoraScreen(BoxLayout):
    def __init__(self, controller, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=15, **kwargs)
        self.controller = controller

        self.inputs = {}
        campos = [
            "Sueldo mensual",
            "Otros ingresos",
            "Aporte a pensión",
            "Intereses crédito vivienda",
            "Gastos médicos",
            "Personas a cargo",
            "Patrimonio"
        ]

        for campo in campos:
            fila = BoxLayout(orientation='horizontal', size_hint_y=None, height=60, spacing=10)

            etiqueta = Label(
                text=campo,
                size_hint_x=0.5,
                halign="left",
                valign="middle",
                text_size=(250, None),  # define el ancho del texto para que haga salto de línea
                shorten=False,
            )
            etiqueta.bind(size=etiqueta.setter('text_size'))  # importante para el wrapping
            fila.add_widget(etiqueta)

            entrada = TextInput(multiline=False, size_hint_x=0.5)
            self.inputs[campo] = entrada
            fila.add_widget(entrada)

            self.add_widget(fila)

        # Resultado
        self.resultado_label = Label(
            text="Resultados aparecerán aquí",
            size_hint_y=None,
            height=40
        )
        self.add_widget(self.resultado_label)

        # Botones
        for texto, accion in [
            ("Calcular", self.calcular_impuesto),
            ("Ver historial", self.mostrar_historial),
            ("Modificar último resultado", self.modificar_ultimo_resultado)
        ]:
            btn = Button(text=texto, size_hint_y=None, height=60)
            btn.bind(on_press=lambda x, f=accion: f())
            self.add_widget(btn)

    def calcular_impuesto(self):
        try:
            datos = {campo: float(self.inputs[campo].text or 0) for campo in self.inputs}
            resultado = self.controller.calcular_impuesto(datos)
            self.resultado_label.text = f"Impuesto calculado: ${resultado:,.2f}"
        except ValueError:
            self.resultado_label.text = "Error: Ingrese solo números válidos."

    def mostrar_historial(self):
        historial = self.controller.obtener_historial_resultados()
        contenido = "\n".join(historial) if historial else "No hay resultados guardados aún."
        popup = Popup(title="Historial",
                      content=Label(text=contenido),
                      size_hint=(0.8, 0.8))
        popup.open()

    def modificar_ultimo_resultado(self):
        popup = Popup(title="Modificar último resultado",
                      content=Label(text="Funcionalidad en construcción"),
                      size_hint=(0.8, 0.4))
        popup.open()


class CalculadoraApp(App):
    def build(self):
        controller = CalculadoraController()
        return CalculadoraScreen(controller)


if __name__ == "__main__":
    CalculadoraApp().run()
