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
## ¿Cómo lo hago funcionar?
Para correr el proyecto debes hacer los siguientes pasos:
  1. clonar y guardar el repositorio en documentos (recomendacion).
  2. Luego abrir carpeta e ir a la ubicacion de este repositorio.
  3. En el buscador de la carpeta digitar el comando "cmd" le das enter.
  4. Se te abrira la terminal ya ubicada en la carpeta donde se encuentra este repositorio.
  5. Luego copia y pega el enlace que se encuentra abajo de estos pasos.
  6. Disfruta del programa.

direccion para copiar y pegar en la terminal 

`
C:/Python313/python.exe d:/Documents/codigo-limpio/src/view/Interfaz_Calculadora.py

`

Para correr las pruebas del proyecto, puedes seguir los pasos anteriores para correr el proyecto y solo debes cambiar el enlace que te dejare abajo:
direccion para copiar y pegar en la terminal. 

`
python -m unittest tests/test_Calculadora.py

`

## ¿Para qué sirve cada carpeta?


Calculadora.py = sirve para realizar cos calculos y validar el tipo de dato. 


Interfaz_Calculadora.py = Este programa pide al usuario datos como sueldo, otros ingresos, gastos médicos, aportes a pensión, etc., y luego calcula automáticamente su ingreso total anual, las deducciones permitidas y la base gravable (la parte del ingreso sobre la que se pagan impuestos). También maneja errores si se ingresan valores inválidos.



test_calculadora.py = sirve para probar automaticamente que una funcion que calcula ingresos anuales devuelva los resultados correctos con datos validos y muestra errores cuando los datos son invalidos. 



Escrito por los estudiantes David Taborda y Juan Ocampo.

