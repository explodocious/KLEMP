import requests


def temperature_converter():
    print("========= TEMPERATURE CONVERTER ========")
    print("1. Celsius")
    print("2. Fahrenheit")
    print("3. Kelvin")
    print("4. Rankine")
    print("5. Reaumur")
    print("6. Delisle")
    choice1 = input("\nSelect the first unit to convert from: ")
    choice2 = input("Select the second unit to convert to: ")
    try:
        value = float(input("Enter the value to convert: "))
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return
    # convert everything to Celsius first
    if choice1 == "1":
        celsius = value
    elif choice1 == "2":
        celsius = (value - 32) * 5 / 9
    elif choice1 == "3":
        celsius = value - 273.15
    elif choice1 == "4":
        celsius = (value - 491.67) * 5 / 9
    elif choice1 == "5":
        celsius = value * 5 / 4
    elif choice1 == "6":
        celsius = 100 - value * 2 / 3
    else:
        print("Invalid choice for the first unit.")
        return

    # convert from Celsius to the target unit
    if choice2 == "1":
        result = celsius
    elif choice2 == "2":
        result = celsius * 9 / 5 + 32
    elif choice2 == "3":
        result = celsius + 273.15
    elif choice2 == "4":
        result = celsius * 9 / 5 + 491.67
    elif choice2 == "5":
        result = celsius * 4 / 5
    elif choice2 == "6":
        result = (100 - celsius) * 3 / 2
    else:
        print("Invalid choice for the second unit.")
        return

    print(f"\nResult: {value} {choice1} = {result} {choice2}")



def distance_converter():
    print("========= DISTANCE CONVERTER ========")
    print("1. Meters")
    print("2. Kilometers")
    print("3. Miles")
    print("4. Yards")
    print("5. Feet")
    print("6. Inches")
    choice1 = input("\nSelect the first unit to convert from: ")
    choice2 = input("Select the second unit to convert to: ")
    try:
        value = float(input("Enter the value to convert: "))
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return
    # convert everything to meters first
    if choice1 == "1":
        meters = value
    elif choice1 == "2":
        meters = value * 1000
    elif choice1 == "3":
        meters = value * 1609.34
    elif choice1 == "4":
        meters = value * 0.9144
    elif choice1 == "5":
        meters = value * 0.3048
    elif choice1 == "6":
        meters = value * 0.0254
    else:
        print("Invalid choice for the first unit.")
        return

    # convert from meters to the target unit
    if choice2 == "1":
        result = meters
    elif choice2 == "2":
        result = meters / 1000
    elif choice2 == "3":
        result = meters / 1609.34
    elif choice2 == "4":
        result = meters / 0.9144
    elif choice2 == "5":
        result = meters / 0.3048
    elif choice2 == "6":
        result = meters / 0.0254
    else:
        print("Invalid choice for the second unit.")
        return

    print(f"\nResult: {value} {choice1} = {result} {choice2}")

def weight_converter():
    print("========= WEIGHT CONVERTER ========")
    print("1. Grams")
    print("2. Kilograms")
    print("3. Pounds")
    print("4. Ounces")
    choice1 = input("\nSelect the first unit to convert from: ")
    choice2 = input("Select the second unit to convert to: ")
    try:
        value = float(input("Enter the value to convert: "))
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return
    # convert everything to grams first
    if choice1 == "1":
        grams = value
    elif choice1 == "2":
        grams = value * 1000
    elif choice1 == "3":
        grams = value * 453.592
    elif choice1 == "4":
        grams = value * 28.3495
    else:
        print("Invalid choice for the first unit.")
        return

    # convert from grams to the target unit
    if choice2 == "1":
        result = grams
    elif choice2 == "2":
        result = grams / 1000
    elif choice2 == "3":
        result = grams / 453.592
    elif choice2 == "4":
        result = grams / 28.3495
    else:
        print("Invalid choice for the second unit.")
        return

    print(f"\nResult: {value} {choice1} = {result} {choice2}")

def search_currency(currency_list, search):
    results = []

    search = search.lower().strip()

    for currency in currency_list:
        code = currency["iso_code"]
        name = currency["name"]

        if search in code.lower() or search in name.lower():
            results.append(currency)

    return results


def choose_currency(currency_list, message):
    while True:
        search = input(message).strip()

        if not search:
            print("Please enter a currency name or code.")
            continue

        results = search_currency(currency_list, search)

        if not results:
            print("No currencies found. Try another search.")
            continue

        print("\n=== SEARCH RESULTS ===")

        for i, currency in enumerate(results, start=1):
            print(
                f"{i}. {currency['iso_code']} - "
                f"{currency['name']}"
            )

        try:
            choice = int(input("\nSelect currency: "))
        except ValueError:
            print("Invalid choice.")
            continue

        if not 1 <= choice <= len(results):
            print("Invalid choice.")
            continue

        return results[choice - 1]["iso_code"]


def currency_converter():
    print("========= CURRENCY CONVERTER ========")

    try:
        response = requests.get(
            "https://api.frankfurter.dev/v2/currencies",
            timeout=10
        )

        response.raise_for_status()
        currency_list = response.json()

    except requests.RequestException:
        print("Could not retrieve currency list.")
        return

    if not isinstance(currency_list, list):
        print("Invalid currency data received from server.")
        return

    print(f"\nAvailable currencies: {len(currency_list)}")

    from_currency = choose_currency(
        currency_list,
        "\nSearch currency to convert FROM: "
    )

    to_currency = choose_currency(
        currency_list,
        "\nSearch currency to convert TO: "
    )

    try:
        value = float(
            input("\nEnter the value to convert: ")
        )
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    if value < 0:
        print("Amount cannot be negative.")
        return

    if from_currency == to_currency:
        print("\n========= RESULT =========")
        print(
            f"{value:,.2f} {from_currency} = "
            f"{value:,.2f} {to_currency}"
        )
        return

    url = (
        f"https://api.frankfurter.dev/v2/rate/"
        f"{from_currency}/{to_currency}"
    )

    try:
        response = requests.get(
            url,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        rate = data["rate"]
        date = data["date"]

        result = value * rate

    except requests.RequestException:
        print("Could not retrieve exchange rate.")
        return

    except (KeyError, TypeError, ValueError):
        print("Invalid data received from exchange server.")
        return

    print("\n========= RESULT =========")

    print(
        f"{value:,.2f} {from_currency}"
        f" = "
        f"{result:,.2f} {to_currency}"
    )

    print(
        f"Exchange rate: "
        f"1 {from_currency} = "
        f"{rate} {to_currency}"
    )

    print(f"Rate date: {date}")
def time_converter():
    print("========= TIME CONVERTER ========")
    print("1. Seconds")
    print("2. Minutes")
    print("3. Hours")
    print("4. Days")
    choice1 = input("\nSelect the first unit to convert from: ")
    choice2 = input("Select the second unit to convert to: ")
    try:
        value = float(input("Enter the value to convert: "))
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return
    # convert everything to seconds first
    if choice1 == "1":
        seconds = value
    elif choice1 == "2":
        seconds = value * 60
    elif choice1 == "3":
        seconds = value * 3600
    elif choice1 == "4":
        seconds = value * 86400
    else:
        print("Invalid choice for the first unit.")
        return
    # convert from seconds to the target unit
    if choice2 == "1":
        result = seconds
    elif choice2 == "2":
        result = seconds / 60
    elif choice2 == "3":
        result = seconds / 3600
    elif choice2 == "4":
        result = seconds / 86400
    else:
        print("Invalid choice for the second unit.")
        return
    

    print(f"\nResult: {value} {choice1} = {result} {choice2}")
def convert():
    print("========= CONVERTER ========")
    print("1. Temperature converter")
    print("2. Distance converter ")
    print("3. Weight converter")
    print("4. Currency converter")
    print("5. Time converter")

    choice = input("\nSelect: ")
    if choice == "1":
        temperature_converter()
    elif choice == "2":
        distance_converter()
    elif choice == "3":
        weight_converter()
    elif choice == "4":
        currency_converter()
    elif choice == "5":
        time_converter()