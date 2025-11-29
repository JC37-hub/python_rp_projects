#===================================================
# RESISTOR VALUE CALCULATOR
# -------------------------
#
# This program calculates and displays the value of a 4-band resistor
# in Ohms, kOhms, or MOhms, including its tolerance.
#
# Program: resistor_calculator.py
# Author : Juan Carlos with Natsuki assistance
# Date   : Nov 28, 2025
#===================================================

# --- Data Structures ---
COLOR_VALUES = {
    'bk': 0, 'br': 1, 're': 2, 'or': 3, 'ye': 4,
    'gr': 5, 'bl': 6, 'vi': 7, 'gy': 8, 'wh': 9
}

MULTIPLIERS = {
    'bk': 1,      # 10^0
    'br': 10,     # 10^1
    're': 100,    # 10^2
    'or': 1000,   # 10^3 (kilo)
    'ye': 10000,
    'gr': 100000,
    'bl': 1000000, # 10^6 (mega)
    'vi': 10000000,
    'gy': 100000000,
    'wh': 1000000000,
    'go': 0.1,    # x0.1
    'si': 0.01    # x0.01
}

TOLERANCES = {
    'go': '±5%',
    'si': '±10%'
}

# Define valid colors for each band type for easier validation
VALID_DIGIT_COLORS = set(COLOR_VALUES.keys()) # For Band 1 and 2
VALID_MULTIPLIER_COLORS = set(MULTIPLIERS.keys()) # For Band 3
VALID_TOLERANCE_COLORS = set(TOLERANCES.keys()) # For Band 4

def display_intro_and_table():
    """Displays the welcome message and the color code reference table."""
    print("=========================================")
    print("| CALCULADORA DE VALOR DE RESISTENCIAS |")
    print("=========================================\n")

    print("Por favor, introduce las abreviaturas de 2 letras para cada banda de la resistencia.\n")

    print("Consideraciones importantes para las entradas:")
    print("-   Para las **Bandas 1 y 2 (dígitos significativos)**: Solo se aceptan colores del 0 al 9 (bk-wh).")
    print("-   Para la **Banda 3 (multiplicador)**: Se aceptan todos los colores. 'bk' a 'wh' representan potencias de 10 (10^0 a 10^9). 'go' (Gold) multiplica por 0.1, y 'si' (Silver) multiplica por 0.01.")
    print("-   Para la **Banda 4 (tolerancia)**: Solo se aceptan 'go' (Gold) para ±5% y 'si' (Silver) para ±10%.\n")

    print("TABLA DE ABREVIATURAS DE COLORES:")
    print("------------------------------------------")
    print("| Color  | Abr. |         Color  | Abr. |")
    print("|--------|------|----------------|------|")
    print("| Black  |  bk  |         Blue   |  bl  |")
    print("| Brown  |  br  |         Violet |  vi  |")
    print("| Red    |  re  |         Grey   |  gy  |")
    print("| Orange |  or  |         White  |  wh  |")
    print("| Yellow |  ye  |         Gold   |  go  |")
    print("| Green  |  gr  |         Silver |  si  |")
    print("------------------------------------------\n")

def get_band_input(band_num, valid_options_set, band_type_description):
    """
    Prompts the user for a band color input and validates it.
    Converts input to lowercase for case-insensitivity.
    """
    while True:
        prompt_message = f"Introduce la abreviatura para la Banda {band_num} ({band_type_description}): "
        user_input = input(prompt_message).lower() # Convert to lowercase immediately

        if user_input in valid_options_set:
            return user_input
        else:
            print(f"Error: '{user_input}' no es una abreviatura válida para la Banda {band_num}. Por favor, revisa la tabla.")

def calculate_and_display_resistor_value():
    """Guides the user through input, calculation, and display of resistor value."""
    # Get inputs for each band with appropriate validation
    band1_color = get_band_input(1, VALID_DIGIT_COLORS, "dígito significativo")
    band2_color = get_band_input(2, VALID_DIGIT_COLORS, "dígito significativo")
    band3_color = get_band_input(3, VALID_MULTIPLIER_COLORS, "multiplicador")
    band4_color = get_band_input(4, VALID_TOLERANCE_COLORS, "tolerancia")

    # Calculate base value from first two bands
    first_digit = COLOR_VALUES[band1_color]
    second_digit = COLOR_VALUES[band2_color]
    base_value = (first_digit * 10) + second_digit

    # Apply multiplier from third band
    multiplier = MULTIPLIERS[band3_color]
    resistor_ohms = base_value * multiplier

    # Get tolerance from fourth band
    tolerance_str = TOLERANCES[band4_color]

    # Format resistance value (kOhm, MOhm)
    formatted_resistance = ""
    if resistor_ohms >= 1_000_000:
        formatted_resistance = f"{resistor_ohms / 1_000_000:.2f} MΩ"
    elif resistor_ohms >= 1_000:
        formatted_resistance = f"{resistor_ohms / 1_000:.2f} kΩ"
    else:
        formatted_resistance = f"{resistor_ohms:.2f} Ω" # Display Ohms with 2 decimal places for consistency

    print(f"\nResistencia: {formatted_resistance} {tolerance_str}")

def main():
    display_intro_and_table()

    while True:
        calculate_and_display_resistor_value()

        # Ask if the user wants to continue
        while True:
            continue_choice = input("\n¿Quieres calcular otra resistencia? (s/n): ").lower()
            if continue_choice in ['s', 'n']:
                break
            else:
                print("Por favor, introduce 's' para sí o 'n' para no.")

        if continue_choice == 'n':
            print("Gracias por usar la Calculadora de Valores de Resistencia. ¡Hasta pronto!")
            break

if __name__ == "__main__":
    main()
