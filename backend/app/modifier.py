import json
from typing import List

with open("app/rules.json", "r", encoding="utf-8") as f:
    RULES_JSON = json.load(f)

def apply_rules_with_llm(data: List[List[str]]) -> List[List[str]]:
    if not data:
        print("🧠 No se recibieron datos para modificar")
        return []

    coberturas_por_tipo = RULES_JSON.get("coberturas_por_tipo", {})
    columnas_a_agregar = RULES_JSON.get("reglas_asignacion", {}).get("columnas_a_agregar", [])
    columna_referencia = RULES_JSON.get("reglas_asignacion", {}).get("mapeo_columnas", {}).get("columna_referencia", "TIPO DE UNIDAD")

    header = data[0]
    print("🧠 Encabezado recibido:", header)
    print("🧠 Columna de referencia esperada:", columna_referencia)
    print("🧠 Columnas a agregar:", columnas_a_agregar)

    try:
        ref_index = header.index(columna_referencia)
    except ValueError:
        print("❌ Columna de referencia no encontrada. Encabezado:", header)
        raise Exception(f"Columna de referencia '{columna_referencia}' no encontrada")

    try:
        insert_index = header.index("NO.SERIE") + 1
    except ValueError:
        insert_index = len(header)
        print("⚠️ Columna 'NO.SERIE' no encontrada, insertando al final")

    new_header = header[:insert_index] + columnas_a_agregar + header[insert_index:]
    new_rows = []

    for row in data[1:]:
        tipo_unidad = row[ref_index].upper().strip()
        tipo_key = "TRACTOS" if tipo_unidad.startswith("TRACTO") else "REMOLQUES"
        tipo_data = coberturas_por_tipo.get(tipo_key, {})
        coberturas = tipo_data.get("coberturas", {})

        nuevos_valores = []
        for col in columnas_a_agregar:
            cobertura, campo = col.rsplit(" ", 1)
            valor = coberturas.get(cobertura, {}).get(campo, "")
            nuevos_valores.append(valor)

        new_row = row[:insert_index] + nuevos_valores + row[insert_index:]
        new_rows.append(new_row)

    print(f"✅ Modificación completada: {len(new_rows)} filas procesadas")
    return [new_header] + new_rows