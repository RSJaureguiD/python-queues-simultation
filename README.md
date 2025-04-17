# Consigna

Resolver el siguiente ejercicio en algún lenguaje de programación (como Python).

La entrega consta de:

1. Archivo fuente de programación (incluir archivo de entrada si fuera necesario)
2. Informe con detalle de librerías utilizadas para el desarrollo y salida obtenido del desarrollo

## Ejercicio:

Una empresa de aire acondicionado tiene el servicio de reparación de sistema central de refrigeración en 5 clientes. El equipo que repara los sistemas de refrigeración recibe 2 solicitudes promedio diarias de reparación que siguen una distribución de Poisson y pueden reparar en promedio 12 máquinas por día con distribución exponencial entre tiempos de reparación. Se pide:

1. Cantidad media de quipos rotos
2. Tiempo medio que los equipos esperan para ser reparados
3. Probabilidad de que 2 o más equipos estén fuera de servicio

# Requerimientos

- Python 3.12

## Librerías

- **numpy**:

Es la única librería que el script requiere instalar. Esta es utilizada para calculos matemáticos como el uso de la función exponencial.

- **math**:

Es la librería estándar de python para realizar cálculos matemáticos. En este caso se utiliza para calcular el factorial de un número.

- **enum**:

Es una librería estándar de python que permite crear enumeraciones. En este caso se utiliza para definir estratégias de calculo de probabilidades, pudiendo seleccionar el calculo por defecto, o el recursivo.

- **unittest**:

Es una librería estándar de python para realizar pruebas unitarias. En este caso se utiliza para probar el correcto funcionamiento de las clases creadas y los modelos.

# Instrucciones

## Con uv

1. Instalar uv: 

    - [Instrucciones](https://docs.astral.sh/uv/getting-started/installation/#__tabbed_1_2)

2. Cargar versión de python:

```bash
uv python install 3.12
```

3. Sincronizar el entorno:

```bash
uv python sync
```

4. Correr el script:

```bash
uv run main.py
```

Alternativamente, correr el archivo `start.bat` luego de haber instalado uv y sincronizado el entorno. Este archivo ejecuta el script main.py en el entorno virtual creado.

## Sin uv

1. Instalar python 3.12

    - [Instrucciones](https://www.python.org/downloads/)

2. Crear un entorno virtual

```bash
python -m venv .venv
```

3. Activar el entorno virtual

```bash
# Windows
.venv\Scripts\activate
# Linux
source .venv/bin/activate
```

4. Instalar las librerías necesarias

```bash
pip install numpy
```

5. Correr el script

```bash
python main.py
```

# Ejemplo de salida

```bash
D:\path\to\dir>.\.venv\Scripts\python.exe .\main.py

Resultados obtenidos al aplicar el modelo M/M/1 FIFO/-/5:
=========================================================

Ejercicio a)
Cantidad media de equipos rotos: 0.18 equipos por hora

Ejercicio b)
Tiempo medio que los equipos esperan para ser reparados: 137.02 minutos

Ejercicio c)
Probabilidad de que 2 o más equipos estén fuera de servicio: 2.06 %

=========================================================
```