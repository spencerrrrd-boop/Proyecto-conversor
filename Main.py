# Conversor de Monedas

def exchange_money(presupuesto, tasa_cambio):
    """
    Convierte dinero de USD a otra moneda usando la tasa de cambio.
    """
    return presupuesto / tasa_cambio


def main():
    print("=== Conversor de Monedas ===")

    # Tasas de cambio (1 unidad de moneda extranjera = X USD)
    tasas_cambio = {
        "Japón (Yen)": 0.0075,
        "México (Peso mexicano)": 0.058,
        "Colombia (Peso colombiano)": 0.00025
    }

    print("\nPaíses disponibles:")
    for i, pais in enumerate(tasas_cambio.keys(), start=1):
        print(f"{i}. {pais}")

    # Pedir datos al usuario
    opcion = int(input("\nElige un país (1-3): "))
    presupuesto = float(input("Introduce la cantidad en USD: "))

    lista_paises = list(tasas_cambio.keys())
    pais_seleccionado = lista_paises[opcion - 1]
    tasa = tasas_cambio[pais_seleccionado]

    resultado = exchange_money(presupuesto, tasa)

    print(f"\n{presupuesto} USD equivalen a {resultado:.2f} en {pais_seleccionado}.")


if __name__ == "__main__":
    main()