# codigo-limpio
solucion del problema calculador declaracion de renta 

Enlace para los audios de la entrevista: https://drive.google.com/drive/folders/1Px86WvVIzanwdtUpdDr4zCUoKNaw0uHq?usp=drive_link

Documento de excel con los casos de uso: https://udemedellin-my.sharepoint.com/:x:/r/personal/dtaborda789_soyudemedellin_edu_co/Documents/calculadora%20de%20impuestos.xlsx?d=wea0377cbd11e4fd199019b71ff3f5436&csf=1&web=1&e=6WGpY6

📄 – Cálculo de Base Gravable para Impuesto de Renta
📌 Descripción
Este documento explica el cálculo de la base sobre la que se paga impuesto de renta para personas naturales a partir de sus ingresos, deducciones y beneficios tributarios.
Incluye ejemplos prácticos de tres casos con diferentes características económicas y familiares.

📥 Entradas
El sistema recibe las siguientes variables para cada caso:

Sueldo mensual → Salario fijo percibido mensualmente por la persona.

Otros ingresos → Ganancias adicionales no incluidas en el sueldo (honorarios, rentas, inversiones, etc.).

Aporte a pensión → Valor anual aportado al sistema de pensiones (obligatorio).

Intereses por crédito de vivienda → Intereses pagados durante el año por un préstamo hipotecario, deducibles según la ley.

Gastos de medicina → Gastos médicos deducibles.

Personas a cargo → Número de dependientes económicos que pueden dar lugar a deducciones.

Patrimonio → Valor total del patrimonio del contribuyente.

Compras o gastos normales → Gastos anuales ordinarios no deducibles.

Dinero consignado a su cuenta → Total anual consignado en cuentas bancarias.

⚙️ Proceso de cálculo
El procedimiento para determinar la base gravable se desarrolla en los siguientes pasos:

Calcular el ingreso total anual a partir del sueldo mensual y otros ingresos.

Determinar las deducciones por ley (aporte a pensión e intereses por crédito de vivienda).

Identificar las deducciones personales (gastos médicos y beneficios por personas a cargo).

Calcular la renta exenta equivalente al 25% del ingreso neto después de deducciones.

Restar la renta exenta al ingreso neto para obtener la base sobre la que se pagará impuesto.

📤 Salidas
El cálculo entrega los siguientes resultados para cada caso:

Ingreso total anual

Deducciones por ley

Deducciones personales

Renta exenta (25%)

Base sobre la que se paga impuesto


¿Para qué sirve cada carpeta?


Calculadora.py = sirve para realizar cos calculos y validar el tipo de dato. 


Interfaz_Calculadora.py = es la encargada de recolectar todos los datos necesarios para realizar los respectivos cálculos.


test_calculadora.py = 



Escrito por los estudiantes David Taborda y Juan Ocampo.

