# Ask user to enter the amount
# if answer is 0, negative number or not a number, print invalid
# ask to select the currencies for conversion
# show the amount

# Store the three currencies in a tuple
# Instead of loop inside a loop, we create seperate loops for various scenarious of invalid input
# use dictionary to store combinations of currencies ( exchange rates)
# converted_amount
# format specifier :.2f - 2 digits after the decimal point
# Refactoring - Break down to functions with a single responsibility


def get_amount():
    while True:
        try:
            amount = float(input("Enter the amount: "))
            if amount <= 0:
                raise ValueError()
            return amount
        except ValueError:
            print("Invalid amount")


def get_currency(label):
    currencies = ("USD", "CAD", "EUR")
    while True:
        currency = input(f"{label} (USD/EUR/CAD): ").upper()
        if currency not in currencies:
            print("Invalid input")
        else:
            return currency


def convert(amount, source_currency, target_currency):
    exchange_rates = {
        "USD": {"EUR": 0.90, "CAD": 1.36},
        "EUR": {"USD": 1.11, "CAD": 1.51},
        "CAD": {"USD": 0.74, "EUR": 0.66}
    }

    if source_currency == target_currency:
        return amount
    return amount * exchange_rates[source_currency][target_currency]


def main():
    amount = get_amount()
    source_currency = get_currency("Source")
    target_currency = get_currency("Target")
    converted_amount = convert(amount, source_currency, target_currency)
    print(
        f"{amount} {source_currency} is equal to {
            converted_amount:.2f} {target_currency}."
    )


if __name__ == "__main__":
    main()
