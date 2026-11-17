# Trazabilidad del ejercicio 2

## 2026-11-17 — Inspección inicial de la parte B

- Revisados `variables.tf`, `main.tf`, `outputs.tf`, `.github/workflows/validacion.yml` y `.gitignore`.
- Revisada la guía `GUIAS/Guia_Alumnado_Ejercicio_2.docx`.
- Rama actual: `demo-ejercicio-2-local`.
- Estado de Git antes de crear esta bitácora: limpio.
- `origin`: `git@github.com:jmmartinezz/prueba-IaC.git`.
- Confirmado que `entorno` tiene `default = "pruebas"`.
- No se modificaron archivos de infraestructura ni el workflow. No se ejecutó OpenTofu.

## 2026-11-17 — Implementación de la parte B

- Confirmado que `escenario-integracion.tfvars` no existía y que el workflow aún tenía un único paso `Mostrar plan`.
- Añadido `escenario-integracion.tfvars` en la raíz con `entorno = "integracion"` y `nombre_aplicacion = "portal-interno"`.
- Reemplazado `Mostrar plan` por dos pasos: plan con valores por defecto y plan con `-var-file=escenario-integracion.tfvars`.
- Se conservaron intactos los pasos anteriores del workflow.
- No se modificaron `variables.tf`, `main.tf`, `outputs.tf` ni `.gitignore`.
- No se ejecutó OpenTofu, `apply` ni `destroy`. No se hizo commit ni push.
- `git diff --check` no reportó errores de espacios en los cambios rastreados; el contenido del nuevo `.tfvars` se revisó directamente.
- El estado de Git mostró únicamente el workflow modificado y los nuevos archivos `.tfvars` y de trazabilidad.

## 2026-11-17 — Comprobación previa a publicación de la parte B

- Rama comprobada: `demo-ejercicio-2-local`.
- `origin` comprobado: `git@github.com:jmmartinezz/prueba-IaC.git`; no coincide con `mpvicenteselae/iac-ia-laboratorio-demo-mario`.
- `git diff --check` no reportó errores.
- No había archivos preparados para commit. No se prepararon archivos porque el remoto no coincide con el solicitado.
- No se hizo commit ni push.

## 2026-11-17 — Preparación de publicación de la parte B

- Rama comprobada nuevamente: `demo-ejercicio-2-local`.
- Verificadas las etiquetas públicas `actions/checkout@v7` y `opentofu/setup-opentofu@v2`; ambas existen. Los avisos del editor no indican que falten esas versiones.
- `git diff --check` pasó sin errores.
- Ejecutado `git add .`; `git diff --cached --name-only` mostró solo `.github/workflows/validacion.yml`, `TRZABILIDAD_2/registro_ejercicio_2.md` y `escenario-integracion.tfvars`.
- Remoto `origin` comprobado: `git@github.com:jmmartinezz/prueba-IaC.git`.
- Commit y push solicitados por el usuario; no se ejecutó OpenTofu.
