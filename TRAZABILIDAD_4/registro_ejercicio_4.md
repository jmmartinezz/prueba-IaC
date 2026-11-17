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
