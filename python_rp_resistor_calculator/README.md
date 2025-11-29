# Calculadora de Valor de Resistencias de 4 Bandas

Este proyecto en Python implementa una sencilla calculadora para determinar el valor y la tolerancia de resistencias de 4 bandas a partir de sus códigos de color. Es una herramienta útil para ingenieros, estudiantes de electrónica y aficionados que necesitan decodificar rápidamente el valor de una resistencia.

## Características

-   Calcula el valor en Ohms (Ω), Kilo-ohms (kΩ) o Mega-ohms (MΩ) automáticamente.
-   Muestra la tolerancia de la resistencia.
-   Interfaz de consola interactiva y fácil de usar.
-   Validación de entrada para asegurar códigos de color correctos.

## Uso

1.  **Navega al directorio del proyecto:**
    ```bash
    cd /path/to/python_rp/python_rp_resistor_calculator/
    ```
2.  **Ejecuta el script:**
    ```bash
    python3 python_rp_resistor_calculator.py
    ```
3.  Sigue las instrucciones en la consola para introducir las abreviaturas de dos letras de los colores de las bandas de la resistencia.

## Ejemplo de Entrada/Salida

```
=========================================
| CALCULADORA DE VALOR DE RESISTENCIAS |
=========================================

Por favor, introduce las abreviaturas de 2 letras para cada banda de la resistencia.

Consideraciones importantes para las entradas:
-   Para las **Bandas 1 y 2 (dígitos significativos)**: Solo se aceptan colores del 0 al 9 (bk-wh).
-   Para la **Banda 3 (multiplicador)**: Se aceptan todos los colores. 'bk' a 'wh' representan potencias de 10 (10^0 a 10^9). 'go' (Gold) multiplica por 0.1, y 'si' (Silver) multiplica por 0.01.
-   Para la **Banda 4 (tolerancia)**: Solo se aceptan 'go' (Gold) para ±5% y 'si' (Silver) para ±10%.

TABLA DE ABREVIATURAS DE COLORES:
------------------------------------------
| Color  | Abr. |         Color  | Abr. |
|--------|------|----------------|------|
| Black  |  bk  |         Blue   |  bl  |
| Brown  |  br  |         Violet |  vi  |
| Red    |  re  |         Grey   |  gy  |
| Orange |  or  |         White  |  wh  |
| Yellow |  ye  |         Gold   |  go  |
| Green  |  gr  |         Silver |  si  |
------------------------------------------

Introduce la abreviatura para la Banda 1 (dígito significativo): ye
Introduce la abreviatura para la Banda 2 (dígito significativo): vi
Introduce la abreviatura para la Banda 3 (multiplicador): re
Introduce la abreviatura para la Banda 4 (tolerancia): go

Resistencia: 4.70 kΩ ±5%
```

## Requisitos

-   Python 3.x

## Contribuciones

Si deseas mejorar esta calculadora o añadir nuevas funcionalidades (por ejemplo, soporte para resistencias de 5 o 6 bandas), ¡no dudes en contribuir!
```
