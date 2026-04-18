# Slovník pro uložení již spočítaných výrazů (cache)
# Např.: "5 10 +" -> 15
cache = {}

# Výpis začátku relace
print("** RPN session started **")

# Nekonečný cyklus - program běží, dokud uživatel nezadá prázdný vstup
while True:
    # Výzva uživateli + načtení vstupu
    expr = input("Write RPN expression: ")

    # Pokud uživatel zadá prázdný řádek → ukončení programu
    if expr == "":
        break

    # Kontrola, jestli už jsme tento výraz počítali
    if expr in cache:
        # Pokud ano, nevypočítáváme znovu, jen vypíšeme uložený výsledek
        print(f"Cached: {cache[expr]}")
        continue  # přeskočí zbytek a jde na další vstup

    # Zásobník (stack) pro výpočet RPN
    stack = []

    # Rozdělení vstupu podle mezer (např. "2 3 +" -> ["2", "3", "+"])
    for token in expr.split():

        # Pokud je token operátor
        if token in ["+", "-", "*", "/", "//"]:
            # Vezmeme poslední dvě hodnoty ze zásobníku
            b = stack.pop()
            a = stack.pop()

            # Provedeme operaci podle typu operátoru
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                stack.append(a / b)
            elif token == "//":
                stack.append(a // b)

        else:
            # Pokud to není operátor, jedná se o číslo

            # Pokud obsahuje tečku → desetinné číslo (float)
            if "." in token:
                stack.append(float(token))
            else:
                # Jinak celé číslo (int)
                stack.append(int(token))

    # Po zpracování výrazu zůstane ve stacku jediný výsledek
    result = stack[0]

    # Uložení výsledku do cache
    cache[expr] = result

    # Výpis výsledku ve správném formátu
    print(f"Result: {result}")

# Výpis ukončení relace
print("** RPN session ended **")