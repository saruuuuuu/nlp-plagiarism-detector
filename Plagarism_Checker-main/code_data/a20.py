def convert_currency(amount, from_currency, to_currency, rates):
    if from_currency not in rates or to_currency not in rates:
        print("Invalid currency code.")
        return None
    return amount * rates[to_currency] / rates[from_currency]

def main():
    rates = {'USD': 1.0, 'EUR': 0.85, 'JPY': 110.0, 'GBP': 0.75, 'INR': 74.0}
    print("Currency Converter")
    print("Supported currencies: USD, EUR, JPY, GBP, INR")

    while True:
        amount = float(input("Enter amount to convert: "))
        from_currency = input("From currency: ").upper()
        to_currency = input("To currency: ").upper()
        
        converted_amount = convert_currency(amount, from_currency, to_currency, rates)
        if converted_amount is not None:
            print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")

        next_conversion = input("Do you want to perform another conversion? (yes/no): ").lower()
        if next_conversion != 'yes':
            print("Exiting the Currency Converter. Goodbye!")
            break

if __name__ == "__main__":
    main()
