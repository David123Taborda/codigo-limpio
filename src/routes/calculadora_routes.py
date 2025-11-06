from flask import Blueprint, render_template, request, redirect, url_for, flash
from src.controller.CalculadoraController import CalculadoraController
from src.db_conection import obtener_historial, modificar_resultado, eliminar_resultado

calculadora_bp = Blueprint('calculadora', __name__, url_prefix='/calculadora')
controller = CalculadoraController()


@calculadora_bp.route('/calcular', methods=['GET', 'POST'])
def calcular():
    """Funcionalidad principal: Calcular e insertar base gravable"""
    if request.method == 'POST':
        try:
            sueldo = float(request.form.get('sueldo', 0))
            otros_ingresos = float(request.form.get('otros_ingresos', 0))
            aporte_pension = float(request.form.get('aporte_pension', 0))
            credito_vivienda = float(request.form.get('credito_vivienda', 0))
            gasto_medicina = float(request.form.get('gasto_medicina', 0))
            personas_a_cargo = int(request.form.get('personas_a_cargo', 0))
            patrimonio = float(request.form.get('patrimonio', 0))

            resultado = controller.procesar_calculo(
                sueldo, otros_ingresos, aporte_pension, credito_vivienda,
                gasto_medicina, personas_a_cargo, patrimonio
            )

            flash('✅ Cálculo realizado exitosamente', 'success')
            return render_template('resultado.html', resultado=resultado)

        except ValueError as e:
            flash(f'❌ Error en los datos ingresados: {str(e)}', 'error')
        except Exception as e:
            flash(f'❌ Error al procesar: {str(e)}', 'error')

    return render_template('calcular.html')


@calculadora_bp.route('/buscar', methods=['GET'])
def buscar():
    """Funcionalidad para buscar/listar historial"""
    try:
        historial = obtener_historial()
        return render_template('buscar.html', historial=historial)
    except Exception as e:
        flash(f'❌ Error al obtener historial: {str(e)}', 'error')
        return render_template('buscar.html', historial=[])


@calculadora_bp.route('/modificar/<int:registro_id>', methods=['GET', 'POST'])
def modificar(registro_id):
    """Funcionalidad para modificar un registro"""
    if request.method == 'POST':
        try:
            nuevo_valor = float(request.form.get('base_gravable'))
            if modificar_resultado(registro_id, nuevo_valor):
                flash('✅ Registro modificado exitosamente', 'success')
                return redirect(url_for('calculadora.buscar'))
            else:
                flash('❌ No se pudo modificar el registro', 'error')
        except Exception as e:
            flash(f'❌ Error al modificar: {str(e)}', 'error')

    # Obtener el registro actual para mostrarlo
    historial = obtener_historial()
    registro = None
    for r in historial:
        if r[0] == registro_id:
            registro = r
            break

    return render_template('modificar.html', registro=registro)


@calculadora_bp.route('/eliminar/<int:registro_id>', methods=['POST'])
def eliminar(registro_id):
    """Funcionalidad para eliminar un registro"""
    try:
        if controller.eliminar_resultado(registro_id):
            flash('✅ Registro eliminado exitosamente', 'success')
        else:
            flash('❌ No se pudo eliminar el registro', 'error')
    except Exception as e:
        flash(f'❌ Error al eliminar: {str(e)}', 'error')

    return redirect(url_for('calculadora.buscar'))
