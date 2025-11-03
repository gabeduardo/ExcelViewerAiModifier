import json
import re
from typing import List
from app.model import chain

# Cargar reglas desde el archivo
with open("app/rules.json", "r", encoding="utf-8") as f:
    RULES_JSON = json.load(f)

def extract_json_block(text: str) -> str:
    """
    Extrae el bloque JSON de una respuesta ahorita cohere que puede estar envuelta en markdown (```json ... ```)
    """
    match = re.search(r"```json\s*(.*?)\s*```", text, re.DOTALL)
    if match:
        return match.group(1)
    return text.strip()  # fallback si no hay delimitadores

def apply_rules_with_llm(data: List[List[str]]) -> List[List[str]]:
    if not data:
        print(" No hay datos para modificar")
        return []

    # Serializar datos y reglas
    sheet_json = json.dumps(data)
    rules_json = json.dumps(RULES_JSON)

    # Construir input para el prompt
    prompt_input = {
        "rules_json": rules_json,
        "sheet_data": sheet_json
    }

    #  Logs para debug
    print(" Prompt enviado al LLM:")
    print(json.dumps(prompt_input, indent=2)[:1000])

    try:
        response = chain.invoke(prompt_input)
        print(" Respuesta cruda del LLM:")
        print(response[:1000])

        json_block = extract_json_block(response)
        enriched = json.loads(json_block)

        print(f" Modificación completada con LLM: {len(enriched) - 1} filas procesadas")
        return enriched

    except json.JSONDecodeError as e:
        print(" Error al parsear la respuesta del LLM como JSON")
        print(" Bloque extraído:", json_block[:1000])
        raise Exception(f"Error parsing LLM response: {e}")

    except Exception as e:
        print(" Error inesperado durante el enriquecimiento")
        raise Exception(f"Error en apply_rules_with_llm: {e}")