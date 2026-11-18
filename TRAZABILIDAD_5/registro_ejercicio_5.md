# Trazabilidad del ejercicio 5

## 2026-11-18 — Preparación y rama de trabajo

- Revisadas `GUIAS/Guia_Alumnado_Ejercicio_5.docx` y `Guia_Ejercicio_5_IaC_IA_Modalidad_Local_BRR.docx`.
- Confirmado que el PR #2 del ejercicio 4 se fusionó en `main`.
- El checkout local estaba limpio en `automatizacion-ejercicio-4`. `main` local estaba en `821aeef`, por detrás del remoto.
- Actualizado `main` mediante fast-forward hasta `cb801d9` (merge del ejercicio 4).
- Creada la rama `arquitectura-ejercicio-5` desde `cb801d9`.
- Verificado el escenario de integración existente: `entorno = "integracion"` y `nombre_aplicacion = "portal-interno"`.
- No se ha hecho commit ni push.

## 2026-11-18 — Implementación inicial del módulo

- Añadida la carpeta `modulo_ficha/` con `main.tf`, `variables.tf` y `outputs.tf`. El módulo define una ficha ficticia, exige nombre y entorno, valida sus valores y expone `resumen`.
- Sustituido el recurso de la raíz por `module.portal` y `module.ayuda`, que reutilizan la misma fuente local.
- Actualizada la salida raíz para reunir los resúmenes de ambas instancias.
- Ampliado `tofu fmt -check -diff` con `-recursive`; se conservaron el resto de pasos del workflow del ejercicio 4.
- Se mantienen sin cambios `variables.tf` de la raíz y `escenario-integracion.tfvars`.
- Añadida al final de `README.md` la sección `Arquitectura ficticia`, explicando reutilización, escenarios, comprobaciones y límites del laboratorio.
- Predicción por configuración: planes de dos fichas, `portal-demo` / `pruebas` y `portal-ayuda` / `pruebas` por defecto; `portal-interno` / `integracion` y `portal-ayuda` / `integracion` en el escenario de integración.
- `git diff --check` no detectó errores de espacios. El panel Problems no reportó errores en los archivos HCL ni en el workflow.
- No se ha ejecutado `tofu fmt`, `tofu validate` ni `tofu plan`: OpenTofu no está instalado en este equipo. La validación ejecutable y los planes de Actions requieren publicar los cambios.
- No se ha hecho commit ni push. No se ejecutará `tofu apply`.

## 2026-11-18 — Revisión técnica y límites de validación

- Revisado el diseño del módulo: `source` enlaza la carpeta local, `nombre` y `entorno` son entradas requeridas y `module.portal.resumen` referencia la salida de esa instancia.
- Revisadas las predicciones de ambas instancias para valores predeterminados e integración. Son predicciones, no resultados de plan comprobados.
- Confirmado que omitir `nombre` en `module.ayuda` dejaría sin suministrar una entrada obligatoria. El error esperado es de argumento requerido, distinto de un error de formato o de una condición de validación de valor.
- `git diff --check` pasó; Problems no informa errores en los seis archivos HCL/YAML revisados. `variables.tf` de raíz y `escenario-integracion.tfvars` siguen sin cambios.
- OpenTofu no está instalado. No se pudo ejecutar `fmt`, `validate` ni los planes localmente.
- El ensayo rojo y su corrección verde no se han ejecutado. Para comprobarlos en GitHub Actions hace falta publicar commits, acción que no se ha realizado por instrucción expresa.
- El PR del ejercicio 5 tampoco se ha creado; requiere publicar la rama. No se hizo commit ni push.
