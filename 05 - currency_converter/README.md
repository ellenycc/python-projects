# Currency Converter

## Goal

The goal of this project is to write a program that converts an amount of money from one currency to another using fixed exchange rates. The user will input the amount and select the currencies for conversion.

## Key Takeaways

1. Use tuples or dictionaries to store values. Tuples can be used to check if something exists in a list (e.g., currencies), while dictionaries can be used to access the value of a key (e.g., exchange rates).

2. To handle invalid input for three scenarios (invalid amount, invalid source currency, and invalid target currency), create separate while loops for each scenario instead of wrapping everything inside the same loop.

3. Use the format specifier `:.2f` to display a floating-point number rounded to two decimal places. For example:

   ```python
   f"{amount} {source_currency} is equal to {converted_amount:.2f} {target_currency}."
   ```

4. Refactor the code by breaking it down into functions with a single responsibility.

5. Use the built-in variable `__name__` to control the execution of code when the script is run directly, but prevent that code from running when the script is imported as a module in another script.

   ```python
   if __name__ == "__main__":
     main()
   ```

   This condition checks if the script is being run directly by the Python interpreter. If it is, then the code under this `if` block will execute. If the script is imported as a module in another script, this block will not execute.
