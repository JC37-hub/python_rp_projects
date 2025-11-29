# Series and Parallel Resistor Calculator

This Python project implements a robust calculator for determining the total resistance of a set of resistors connected in series or in parallel. The tool is designed to facilitate electronics calculations, allowing flexible input of values (Ohms, kΩ, MΩ) and offering comprehensive error handling for a reliable user experience.

## Features

-   **Calculation Modes:** Supports calculations for resistors in series and in parallel.
-   **Flexible Value Input:** Allows entering resistor values directly in Ohms, or using 'k' suffixes for kilo-ohms and 'M' for mega-ohms (e.g., `100`, `1.5k`, `2.2M`).
-   **Robust Validation:** Handles invalid inputs (text instead of numbers, negative values, etc.) and prevents critical errors such as division by zero in parallel calculations.
-   **Clear and Formatted Output:** Presents the total resistance in the most appropriate unit (Ohms, kΩ, MΩ) for easy reading.
-   **Friendly Console Interface:** Includes informative messages, an ASCII diagram of connections, and intuitive flow management.

## Usage

1.  **Navigate to the project directory:**
    ```bash
    cd /path/to/python_rp/python_rp_series_parallel_calculator/
    ```
    (Ensure that the `python_rp_series_parallel_calculator.py` file is in this directory).

2.  **Execute the script:**
    ```bash
    python3 python_rp_series_parallel_calculator.py
    ```

3.  Follow the console prompts to enter the number of resistors, their connection mode, and the value of each resistor.

## Requirements

-   Python 3.x

## Development

Developed by: Juan Carlos with Natsuki assistance
Date: Nov 28, 2025
