import sys

def parse_line(line):
    fields = []
    field = ""
    in_quotes = False

    for char in line:
        if char == '"':
            in_quotes = not in_quotes
        elif char == ';' and not in_quotes:
            fields.append(field.strip())
            field = ""
        else:
            field += char
    fields.append(field.strip())  # Anhadir ultimo campo
    return fields

def main():
    compositores = set()
    map_obras_periodo = {}

    next(sys.stdin)  # Saltar encabezado

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        campos = parse_line(line)
        if len(campos) < 7:
            continue  # Saltar malas lineas

        obra = campos[0]
        periodo = campos[3]
        compositor = campos[4]

        compositores.add(compositor)

        if periodo not in map_obras_periodo:
            map_obras_periodo[periodo] = set()
        map_obras_periodo[periodo].add(obra)

    # Mostrar resultados
    print("--Resultados--\n")

    print("Compositores ordenados alfabeticamente:\n")
    for compositor in sorted(compositores):
        print(compositor)

    print("\nNúmero obras por período:\n")
    for periodo in map_obras_periodo:
        print(f"{periodo}: {len(map_obras_periodo[periodo])}")

    print("\nObras por período:\n")
    for periodo in map_obras_periodo:
        print(f"{periodo}:")
        for obra in sorted(map_obras_periodo[periodo]):
            print(f"  - {obra}")

if __name__ == "__main__":
    main()
