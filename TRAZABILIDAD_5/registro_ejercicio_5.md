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
- No se ejecutará `tofu apply`.

## 2026-11-18 — Primera publicación y planes correctos

- Commit `e40b5c6` (`Ejercicio 5: crear módulo reutilizable`) publicado en `arquitectura-ejercicio-5`.
- [Ejecución verde inicial 44295775986](https://github.com/jmmartinezz/prueba-IaC/actions/runs/44295775986): formato recursivo, validación, los dos planes, resumen y publicación de evidencia concluyeron correctamente.
- El plan predeterminado mostró `portal-demo` / `pruebas` y `portal-ayuda` / `pruebas`; integración mostró `portal-interno` / `integracion` y `portal-ayuda` / `integracion`.
- Ambos planes indicaron `2 to add, 0 to change, 0 to destroy`. Son recursos ficticios planificados; no se ejecutó `apply`.
- Artefacto `evidencia-iac-44295775986-1`, disponible hasta el 2026-11-25.

## 2026-11-18 — Fallo controlado por argumento obligatorio

- En el commit `f716c4c` (`Prueba: falta nombre en módulo ayuda`) se quitó solo `nombre = "portal-ayuda"` de la llamada `module.ayuda`.
- [Ejecución roja 44295973401](https://github.com/jmmartinezz/prueba-IaC/actions/runs/44295973401): `Comprobar formato` pasó y `Validar` falló con `The argument "nombre" is required, but no definition was found.` Los dos planes quedaron `skipped`.
- Los pasos de resumen y publicación sí se ejecutaron; el artefacto fue `evidencia-iac-44295973401-1`.
- El fallo fue deliberado para demostrar que la entrada requerida se valida antes de planificar.

## 2026-11-18 — Corrección del argumento y documentación

- Restaurado `nombre = "portal-ayuda"` en `module.ayuda`.
- Commit `9d02f22` (`Corrección: restaurar nombre del módulo`) publicado en `arquitectura-ejercicio-5`.
- [Ejecución verde corregida 44296101774](https://github.com/jmmartinezz/prueba-IaC/actions/runs/44296101774): los pasos de formato recursivo, validación, ambos planes, resumen y publicación de evidencia concluyeron correctamente.
- El plan volvió a prever dos fichas por escenario; no se ejecutó `apply`.
- Añadida a `README.md` la sección `Arquitectura ficticia` para documentar reutilización, escenarios, pipeline, revisión humana y límites de la práctica.
- Commit `6681948` (`Ejercicio 5: documentar arquitectura`) publicado en la rama.
- [Ejecución verde con documentación 44296202040](https://github.com/jmmartinezz/prueba-IaC/actions/runs/44296202040): formato recursivo, validación, ambos planes, resumen y artefacto pasaron.
- Se publicó `evidencia-iac-44296202040-1`, con retención de siete días.

## 2026-11-18 — Revisión técnica y límites de validación

- Revisado el diseño del módulo: `source` enlaza la carpeta local, `nombre` y `entorno` son entradas requeridas y `module.portal.resumen` referencia la salida de esa instancia.
- Las predicciones para valores predeterminados e integración quedaron confirmadas por los planes de la ejecución verde inicial.
- Confirmado que omitir `nombre` en `module.ayuda` dejaría sin suministrar una entrada obligatoria. El error esperado es de argumento requerido, distinto de un error de formato o de una condición de validación de valor.
- `git diff --check` pasó; Problems no informa errores en los seis archivos HCL/YAML revisados. `variables.tf` de raíz y `escenario-integracion.tfvars` siguen sin cambios.
- OpenTofu no está instalado localmente; formato, validación y planes se ejecutaron en GitHub Actions.
- `tofu apply` no se ejecutó. No se han añadido proveedores cloud ni credenciales.
- El PR y la integración en `main` se documentarán después de verificarlos.
