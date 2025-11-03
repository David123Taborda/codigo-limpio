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
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from src.controller.CalculadoraController import CalculadoraController


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
            ("Modificar último resultado", self.modificar_ultimo_resultado),
            ("Eliminar último resultado", self.eliminar_ultimo_resultado)
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
        if historial:
            # Formatear cada registro del historial
            contenido = "\n".join([
                f"ID: {r[0]} | Base: ${r[5]:,.2f} | Fecha: {r[6]}"
                for r in historial
            ])
        else:
            contenido = "No hay resultados guardados aún."
        
        popup = Popup(title="Historial",
                      content=Label(text=contenido),
                      size_hint=(0.8, 0.8))
        popup.open()

    def modificar_ultimo_resultado(self):
        """Modificar el último resultado de la base de datos"""
        historial = self.controller.obtener_historial_resultados()
        if not historial:
            popup = Popup(title="Error",
                          content=Label(text="No hay resultados para modificar"),
                          size_hint=(0.6, 0.3))
            popup.open()
            return
        
        # Crear popup con input para nuevo valor
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        layout.add_widget(Label(text=f"Modificar último resultado (ID: {historial[0][0]})"))
        layout.add_widget(Label(text=f"Base gravable actual: ${historial[0][5]:,.2f}"))
        
        nuevo_valor_input = TextInput(hint_text="Nuevo valor", multiline=False)
        layout.add_widget(nuevo_valor_input)
        
        btn_box = BoxLayout(orientation='horizontal', size_hint_y=None, height=50, spacing=10)
        
        def guardar_cambio(instance):
            try:
                nuevo_valor = float(nuevo_valor_input.text)
                if self.controller.modificar_ultimo_resultado(nuevo_valor):
                    self.resultado_label.text = f"✅ Resultado modificado a ${nuevo_valor:,.2f}"
                else:
                    self.resultado_label.text = "❌ Error al modificar"
                popup_mod.dismiss()
            except ValueError:
                self.resultado_label.text = "❌ Ingrese un valor numérico válido"
        
        btn_guardar = Button(text="Guardar")
        btn_guardar.bind(on_press=guardar_cambio)
        btn_box.add_widget(btn_guardar)
        
        btn_cancelar = Button(text="Cancelar")
        btn_cancelar.bind(on_press=lambda x: popup_mod.dismiss())
        btn_box.add_widget(btn_cancelar)
        
        layout.add_widget(btn_box)
        
        popup_mod = Popup(title="Modificar Resultado",
                          content=layout,
                          size_hint=(0.7, 0.5))
        popup_mod.open()
    
    def eliminar_ultimo_resultado(self):
        """Eliminar el último resultado de la base de datos"""
        historial = self.controller.obtener_historial_resultados()
        if not historial:
            popup = Popup(title="Error",
                          content=Label(text="No hay resultados para eliminar"),
                          size_hint=(0.6, 0.3))
            popup.open()
            return
        
        id_a_eliminar = historial[0][0]
        
        # Popup de confirmación
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        layout.add_widget(Label(text=f"¿Eliminar resultado ID {id_a_eliminar}?"))
        layout.add_widget(Label(text=f"Base gravable: ${historial[0][5]:,.2f}"))
        
        btn_box = BoxLayout(orientation='horizontal', size_hint_y=None, height=50, spacing=10)
        
        def confirmar_eliminar(instance):
            if self.controller.eliminar_resultado(id_a_eliminar):
                self.resultado_label.text = f"🗑️ Resultado ID {id_a_eliminar} eliminado"
            else:
                self.resultado_label.text = "❌ Error al eliminar"
            popup_del.dismiss()
        
        btn_si = Button(text="Sí, eliminar")
        btn_si.bind(on_press=confirmar_eliminar)
        btn_box.add_widget(btn_si)
        
        btn_no = Button(text="Cancelar")
        btn_no.bind(on_press=lambda x: popup_del.dismiss())
        btn_box.add_widget(btn_no)
        
        layout.add_widget(btn_box)
        
        popup_del = Popup(title="Confirmar Eliminación",
                          content=layout,
                          size_hint=(0.7, 0.4))
        popup_del.open()


class CalculadoraApp(App):
    def build(self):
        controller = CalculadoraController()
        return CalculadoraScreen(controller)


if __name__ == "__main__":
    CalculadoraApp().run()
