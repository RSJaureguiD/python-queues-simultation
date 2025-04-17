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

# Solución

Dado el problema se destaca la siguiente información:

- Tenemos 1 equipo de reparación.
- Arrivos exponenciales, y tiempos de reparación exponenciales.
- La capacidad del sistema es indeterminada.
- La población es dificil de determinar. Se mencionan 5 clientes pero no se sabe cuantos equipos tienen cada uno. Como minimo se asume que cada cliente tiene al menos 1 equipo, por lo que la población mínima es 5. Sin embargo, no se sabe si hay más equipos por cliente. Por lo tanto, se puede incluso considerar una población infinita. Para este ejercicio asumimos una población de 5 equipos, ya que es la información más concreta que se tiene.
- Se reciben 2 maquinas por día
- Se pueden reparar 12 máquinas por día.
- Se asume las maquinas se reparan en el orden de llegada

Este analisis lleva a considerar un modelo M/M/1 FIFO/-/5, tasa de servicio de 12 por dia. La tasa de llegada individual la podemos calcular como $\lambda_{ind} = \lambda_0 = \dfrac{\lambda_n}{m} = \dfrac{2}{5} = 0.4$ por día.

## Parametros del modelo

1. Modelo M/M/1 FIFO/-/5
2. Tasa de llegada: $\lambda = 2$ por día $\Rightarrow \lambda_{ind} = \dfrac{2}{5}$ por día $= \dfrac{1}{60}$ por hora.
3. Tasa de servicio: $\mu = 12$ por día $\Rightarrow \mu = \dfrac{1}{2}$ por hora.

# Programa

## Requerimientos

- Python 3.12

### Librerías

- **numpy**:

Es la única librería que el script requiere instalar. Esta es utilizada para calculos matemáticos como el uso de la función exponencial.

- **math**:

Es la librería estándar de python para realizar cálculos matemáticos. En este caso se utiliza para calcular el factorial de un número.

- **enum**:

Es una librería estándar de python que permite crear enumeraciones. En este caso se utiliza para definir estratégias de calculo de probabilidades, pudiendo seleccionar el calculo por defecto, o el recursivo.

- **unittest**:

Es una librería estándar de python para realizar pruebas unitarias. En este caso se utiliza para probar el correcto funcionamiento de las clases creadas y los modelos.

## Instrucciones

### Con uv

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

### Sin uv

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

## Ejemplo de salida

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