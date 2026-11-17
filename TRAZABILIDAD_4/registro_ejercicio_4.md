# Trazabilidad del ejercicio 4

## 2026-11-17 — Inspección inicial

- Revisada la guía `GUIAS/Guia_Alumnado_Ejercicio_4.docx`.
- Punto de partida: `main`, commit `821aeef` (integración del ejercicio 3).
- Estado inicial del repositorio: limpio.
- Rama remota `automatizacion-ejercicio-4`: no existía al iniciar la práctica.
- Creada la rama local `automatizacion-ejercicio-4` desde `main`.
- Confirmado que `.github/workflows/validacion.yml` ya ejecutaba formato, validación y dos planes; no se modificaron sus disparadores, permisos, trabajo, instalación ni inicialización.
- La práctica solo planifica. No se ejecutan `tofu apply` ni `tofu destroy`.

## 2026-11-17 — Instrumentación del workflow

- Añadidos los identificadores `formato`, `validar`, `plan_predeterminado` y `plan_integracion` a las cuatro comprobaciones.
- Añadido el paso `Resumir comprobaciones`, condicionado con `always()`. Escribe el SHA y los cuatro estados en el resumen de Actions y en `evidencia.txt`.
- Añadido `Publicar evidencia`, también condicionado con `always()`, para adjuntar `evidencia.txt` durante 7 días.
- El nombre del artefacto incluye `run_id` y `run_attempt`; no se publica el plan.
- La prueba de fallo controlado, sus ejecuciones y los enlaces de evidencia se registrarán en esta bitácora después de verificarlos.

## 2026-11-17 — Ejecución correcta inicial

- Publicado el commit `f633c6a` (`Ejercicio 4: resumir y conservar evidencias`) en `automatizacion-ejercicio-4`.
- [Ejecución verde 44088518774](https://github.com/jmmartinezz/prueba-IaC/actions/runs/44088518774): trabajo `comprobar` completado con éxito.
- Completados con éxito `Inicializar`, `Comprobar formato`, `Validar`, ambos planes, `Resumir comprobaciones` y `Publicar evidencia`.
- Artefacto `evidencia-iac-44088518774-1`, disponible hasta el 2026-11-24. `tofu apply` no se ejecutó.

## 2026-11-17 — Preparación del fallo controlado

- Cambiada temporalmente la ruta del plan de integración a `escenario-inexistente.tfvars`, que no se crea.
- Este cambio deliberado se publicará en la rama de ejercicio para comprobar el estado `failure` en el resumen y el artefacto. La ruta se restaurará después de verificar la ejecución.
