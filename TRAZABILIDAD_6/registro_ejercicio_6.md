# Trazabilidad del ejercicio 6

## 2026-11-19 — Preparación

- Revisada `Guia_Ejercicio_6_IaC_IA_BRR.docx`.
- Confirmado que el ejercicio 5 está fusionado en `main` y que el árbol local estaba limpio.
- Creada la rama local `politica-ejercicio-6` desde `main` en `81ee5a7`.
- No se ha hecho commit ni push, según la instrucción del usuario.

## 2026-11-19 — Implementación local

- Añadido `politica_plan.py` en la raíz. Lee el JSON de un plan por entrada estándar y verifica exactamente dos direcciones esperadas, recursos gestionados `terraform_data`, acción `create`, entradas conocidas y no sensibles, nombres, entornos permitidos y coincidencia de entorno.
- Actualizado `.github/workflows/validacion.yml`: desactivado `tofu_wrapper`; ambos planes se guardan como `.tfplan` temporales, se convierten con `tofu show -json` y se pasan a Python. Añadidos dos pasos de política y sus resultados al resumen. Se conservan formato, validación, escenarios, `always()` y publicación del resumen.
- Añadida a `README.md` la sección `Política del laboratorio`, con la regla, la diferencia respecto a `tofu validate` y los límites.
- No se cambió `main.tf`; permanece con ambas fichas en el mismo entorno.
- Los `.tfplan` están ignorados por `.gitignore` existente y no se adjuntan como artefactos.
- No se ejecutó `tofu apply`.
- Las ejecuciones verde/roja/corregida requieren commits y push para GitHub Actions; no se han realizado por instrucción expresa.
- `git diff --check` terminó correctamente; el editor no informó errores en los archivos modificados. Se confirmó que los nombres de plan `.tfplan` están ignorados por Git.
- No se pudieron ejecutar el validador ni `tofu plan` en local: Python y OpenTofu no están instalados en este equipo. Tampoco se pueden verificar nuevas ejecuciones de Actions sin publicar la rama.

## 2026-11-19 — Publicación autorizada

- El usuario autorizó ahora completar el ejercicio mediante commits y push, sustituyendo la restricción anterior de no publicar.
- Se publicará el validador y el workflow desde `politica-ejercicio-6`. Después se comprobarán las ejecuciones en GitHub Actions.
- Para demostrar la regla, se probará en un commit separado un entorno distinto solo para `module.ayuda`; tras verificar el rechazo, se restaurará el valor correcto en un commit posterior.

## Prueba negativa deliberada

- En `main.tf`, solo la instancia `ayuda` usa temporalmente `entorno = "desarrollo"` mientras `portal` conserva `var.entorno`.
- Commit de prueba: `0909588` (`Prueba negativa: rechazar entornos distintos`), publicado en la rama.
- GitHub Actions, ejecución 30 (`44510526349`): formato, validación y plan predeterminado pasaron; la política falló con `portal y ayuda deben pertenecer al mismo entorno`. Los pasos posteriores de integración quedaron omitidos por el fallo; el resumen y el artefacto de evidencia se publicaron correctamente.
- El fallo fue el rechazo intencionado de la política, no un error de formato ni de validación de OpenTofu.
- Restaurado `main.tf` para que ambas instancias reciban `var.entorno`; se publicará la corrección y se verificará la ejecución verde.
