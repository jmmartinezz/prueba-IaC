import json
import sys


EXPECTED_INPUTS = {"nombre", "entorno", "etiquetas"}
EXPECTED_TAGS = {"proyecto", "entorno", "responsable"}
EXPECTED_RESOURCES = {
    'module.fichas["portal"].terraform_data.ficha': "portal",
    'module.fichas["ayuda"].terraform_data.ficha': "ayuda",
}
ALLOWED_ENVIRONMENTS = {"desarrollo", "pruebas", "integracion"}
EXPECTED_RESPONSABLES_BY_ENVIRONMENT = {
    "desarrollo": "equipo-lab",
    "pruebas": "equipo-lab",
    "integracion": "equipo-integracion",
}


def reject(reason):
    print(f"POLÍTICA RECHAZADA: {reason}", file=sys.stderr)
    raise SystemExit(1)


def contains_true(value):
    if value is True:
        return True
    if isinstance(value, dict):
        return any(contains_true(item) for item in value.values())
    if isinstance(value, list):
        return any(contains_true(item) for item in value)
    return False


try:
    plan = json.load(sys.stdin)
except json.JSONDecodeError as error:
    reject(f"el plan no contiene JSON válido: {error.msg}")

if not isinstance(plan, dict):
    reject("el plan JSON debe ser un objeto")

changes = plan.get("resource_changes")
if not isinstance(changes, list):
    reject("falta la lista resource_changes")
if len(changes) != len(EXPECTED_RESOURCES):
    reject("se esperan exactamente las fichas portal y ayuda")

environments = {}
seen_addresses = set()

for item in changes:
    if not isinstance(item, dict):
        reject("resource_changes contiene una entrada inválida")

    address = item.get("address")
    if (
        not isinstance(address, str)
        or address not in EXPECTED_RESOURCES
        or address in seen_addresses
    ):
        reject("las direcciones deben ser exactamente portal y ayuda")
    seen_addresses.add(address)

    if item.get("mode") != "managed" or item.get("type") != "terraform_data":
        reject(f"{address} debe ser un recurso terraform_data administrado")

    change = item.get("change")
    if not isinstance(change, dict) or change.get("actions") != ["create"]:
        reject(f"{address} debe tener únicamente la acción create")

    after = change.get("after")
    if not isinstance(after, dict):
        reject(f"{address} no contiene los valores previstos")
    inputs = after.get("input")
    if not isinstance(inputs, dict) or set(inputs) != EXPECTED_INPUTS:
        reject(f"{address} debe contener solo nombre, entorno y etiquetas")

    unknown = change.get("after_unknown", {})
    sensitive = change.get("after_sensitive", {})
    unknown_input = unknown.get("input", {}) if isinstance(unknown, dict) else unknown
    sensitive_input = (
        sensitive.get("input", {}) if isinstance(sensitive, dict) else sensitive
    )
    if contains_true(unknown_input):
        reject(f"{address}.input no puede contener valores desconocidos")
    if contains_true(sensitive_input):
        reject(f"{address}.input no puede contener valores sensibles")

    if not isinstance(inputs["nombre"], str):
        reject(f"{address}.nombre debe ser una cadena conocida")
    if not isinstance(inputs["entorno"], str):
        reject(f"{address}.entorno debe ser una cadena conocida")
    tags = inputs["etiquetas"]
    if not isinstance(tags, dict) or set(tags) != EXPECTED_TAGS:
        reject(f"{address}.etiquetas debe contener proyecto, entorno y responsable")
    if any(not isinstance(value, str) for value in tags.values()):
        reject(f"{address}.etiquetas debe contener cadenas conocidas")

    if not inputs["nombre"].startswith("portal-"):
        reject(f"{address}.nombre debe empezar por portal-")
    if EXPECTED_RESOURCES[address] == "ayuda" and inputs["nombre"] != "portal-ayuda":
        reject("la ficha de ayuda debe llamarse portal-ayuda")

    environment = inputs["entorno"]
    if environment not in ALLOWED_ENVIRONMENTS:
        reject("el entorno debe ser desarrollo, pruebas o integracion")
    if tags["proyecto"] != "nexo-portal":
        reject(f"{address}.etiquetas.proyecto debe ser nexo-portal")
    if tags["entorno"] != environment:
        reject(f"{address}.etiquetas.entorno debe coincidir con el entorno")
    if tags["responsable"] != EXPECTED_RESPONSABLES_BY_ENVIRONMENT[environment]:
        reject(f"responsable no aprobado para {environment}")
    environments[EXPECTED_RESOURCES[address]] = environment

if seen_addresses != set(EXPECTED_RESOURCES):
    reject("el plan debe incluir las fichas portal y ayuda")

if environments["portal"] != environments["ayuda"]:
    reject("portal y ayuda deben pertenecer al mismo entorno")

print(
    "POLÍTICA APROBADA: dos fichas con etiquetas y responsable ficticios correctos."
)
