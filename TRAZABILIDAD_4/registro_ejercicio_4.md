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

## 2026-11-17 — Ejecución correcta inicial

- Publicado el commit `f633c6a` (`Ejercicio 4: resumir y conservar evidencias`) en `automatizacion-ejercicio-4`.
- [Ejecución verde 44088518774](https://github.com/jmmartinezz/prueba-IaC/actions/runs/44088518774): trabajo `comprobar` completado con éxito.
- Completados con éxito `Inicializar`, `Comprobar formato`, `Validar`, ambos planes, `Resumir comprobaciones` y `Publicar evidencia`.
- Artefacto `evidencia-iac-44088518774-1`, disponible hasta el 2026-11-24. `tofu apply` no se ejecutó.

## 2026-11-17 — Preparación del fallo controlado

- Cambiada temporalmente la ruta del plan de integración a `escenario-inexistente.tfvars`, que no se crea.
- Publicado el commit `c49bda6` (`Prueba: ruta de escenario inexistente`) solo en `automatizacion-ejercicio-4`.
- [Ejecución roja 44088677263](https://github.com/jmmartinezz/prueba-IaC/actions/runs/44088677263): falló `Plan del escenario integracion`; `Formato`, `Validación` y `Plan predeterminado` fueron `success`, y el resumen y la publicación de evidencia también fueron `success`.
- Mensaje del log: `Given variables file escenario-inexistente.tfvars does not exist.`
- El resumen reflejó `Plan de integración | failure`; se publicó `evidencia-iac-44088677263-1` hasta el 2026-11-24.
- `always()` permitió ejecutar los pasos de diagnóstico, sin convertir el trabajo fallido en éxito.

## 2026-11-17 — Corrección del fallo controlado

- Restaurada la ruta `-var-file=escenario-integracion.tfvars`.
- Publicado el commit `646f96c` (`Corregir ruta de escenario`) en `automatizacion-ejercicio-4`.
- [Ejecución verde corregida 44088903265](https://github.com/jmmartinezz/prueba-IaC/actions/runs/44088903265): trabajo `comprobar` y los cuatro resultados, resumen y publicación completados con éxito.
- Artefacto `evidencia-iac-44088903265-1`, disponible hasta el 2026-11-24.
- `evidencia.txt` contiene el SHA analizado y los cuatro estados; no representa aprobación de despliegue. No se ejecutó `tofu apply`.
