from flask import Blueprint, render_template, redirect, url_for, flash, request
from src.db_conection import crear_tabla

database_bp = Blueprint('database', __name__, url_prefix='/database')


@database_bp.route('/crear-tablas', methods=['GET', 'POST'])
def crear_tablas():
    """Opción en el menú para crear las tablas de la BD"""
    if request.method == 'POST':
        try:
            crear_tabla()
            flash('✅ Tablas creadas exitosamente en la base de datos', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            flash(f'❌ Error al crear tablas: {str(e)}', 'error')

    return render_template('crear_tablas.html')
