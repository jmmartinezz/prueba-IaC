import json
import sys


EXPECTED_INPUTS = {"nombre", "entorno"}
EXPECTED_RESOURCES = {
    'module.fichas["portal"].terraform_data.ficha': "portal",
    'module.fichas["ayuda"].terraform_data.ficha': "ayuda",
}
ALLOWED_ENVIRONMENTS = {"desarrollo", "pruebas", "integracion"}


def reject(reason):
    print(f"POLÍTICA RECHAZADA: {reason}", file=sys.stderr)
    raise SystemExit(1)


def is_marked(marker, field):
    if marker is True:
        return True
    if not isinstance(marker, dict):
        return False

    input_marker = marker.get("input")
    if input_marker is True:
        return True
    return isinstance(input_marker, dict) and input_marker.get(field) is True


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
        reject(f"{address} debe contener solo nombre y entorno")

    unknown = change.get("after_unknown", {})
    sensitive = change.get("after_sensitive", {})
    for field in EXPECTED_INPUTS:
        value = inputs[field]
        if not isinstance(value, str):
            reject(f"{address}.{field} debe ser una cadena conocida")
        if is_marked(unknown, field):
            reject(f"{address}.{field} no puede ser desconocido")
        if is_marked(sensitive, field):
            reject(f"{address}.{field} no puede ser sensible")

    if not inputs["nombre"].startswith("portal-"):
        reject(f"{address}.nombre debe empezar por portal-")
    if EXPECTED_RESOURCES[address] == "ayuda" and inputs["nombre"] != "portal-ayuda":
        reject("la ficha de ayuda debe llamarse portal-ayuda")
    environments[EXPECTED_RESOURCES[address]] = inputs["entorno"]

if seen_addresses != set(EXPECTED_RESOURCES):
    reject("el plan debe incluir las fichas portal y ayuda")

if any(value not in ALLOWED_ENVIRONMENTS for value in environments.values()):
    reject("el entorno debe ser desarrollo, pruebas o integracion")
if environments["portal"] != environments["ayuda"]:
    reject("portal y ayuda deben pertenecer al mismo entorno")

print("POLÍTICA APROBADA: dos fichas ficticias, mismo entorno y sin operaciones reales.")
