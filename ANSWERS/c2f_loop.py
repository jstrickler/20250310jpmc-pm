while True:
    celsius = input('Enter Celsius temp: ')
    if celsius.lower().startswith('q'):
        break
    if celsius == '':
        continue

    try:
        celsius = float(celsius)
    except (ValueError, TypeError) as err:
        print("Invalid input", err)
        print(f"{err.args = }")
        
    except Exception as err:
        print("did not expect this!", err)

    else:
        fahrenheit = ((9 * celsius) / 5) + 32
        print(f'{celsius:.1f}\u00B0 C is {fahrenheit:.1f}\u00B0 F\n')

# raise SomeError("a message", x, y)
