import pandas as pd
from io import BytesIO
from typing import List, Dict

# Extrae nombres de hojas desde archivo Excel en bytes
def get_sheet_names(file_bytes: bytes) -> List[str]:
    excel_file = BytesIO(file_bytes)
    xls = pd.ExcelFile(excel_file)
    return xls.sheet_names

# Extrae datos de una hoja como matriz (lista de listas)
def extract_sheet_data(contents: bytes, sheet_name: str) -> List[List[str]]:
    import openpyxl
    from io import BytesIO

    wb = openpyxl.load_workbook(BytesIO(contents), data_only=True)
    sheet = wb[sheet_name]

    data = []
    for row in sheet.iter_rows(values_only=True):
        if row and any(cell is not None and str(cell).strip() for cell in row):
            data.append([str(cell).strip() if cell is not None else "" for cell in row])

    # Buscar encabezado
    for i, row in enumerate(data):
        if "TIPO DE UNIDAD" in row:
            print(f"🧠 Encabezado encontrado en fila {i}: {row}")
            return data[i:]  # devolver desde el encabezado en adelante

    print("❌ Encabezado 'TIPO DE UNIDAD' no encontrado")
    return []

# Escribe un nuevo Excel desde un diccionario {sheet_name: data}
def write_excel(sheets_data: Dict[str, List[List[str]]]) -> bytes:
    output = BytesIO()
    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        for sheet_name, data in sheets_data.items():
            df = pd.DataFrame(data)
            df.to_excel(writer, index=False, header=False, sheet_name=sheet_name)
    output.seek(0)
    return output.read()