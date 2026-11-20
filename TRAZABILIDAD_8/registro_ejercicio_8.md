# Trazabilidad del ejercicio 8

## Preparación

- La guía del ejercicio 8 pide añadir etiquetas ficticias a las fichas y gobernar el responsable permitido según el entorno.
- Rama de trabajo: `taller-final-ejercicio-8`, creada desde `catalogo-ejercicio-7` en `e3fc7bf`.
- El pull request de este ejercicio se dirigirá a `catalogo-ejercicio-7`; no se fusionará automáticamente.
- No se ha ejecutado `tofu apply`.

## Implementación y comprobación inicial

- En `variables.tf` se añadió `responsable`, con valor predeterminado `equipo-lab`.
- `escenario-integracion.tfvars` asigna `equipo-integracion` al escenario de integración.
- `main.tf` transmite el responsable a las instancias de `modulo_ficha`; el módulo lo incorpora a las etiquetas ficticias `proyecto`, `entorno` y `responsable` dentro de `terraform_data.input`.
- `politica_plan.py` exige exactamente las etiquetas y valores previstos, valida el responsable por entorno y conserva las comprobaciones de direcciones, nombres, entorno, valores desconocidos y valores sensibles.
- Commit inicial: `b648f5f` (`Ejercicio 8: etiquetas y responsables gobernados`). Actions, ejecución 42: falló en `tofu fmt -check -diff -recursive`; OpenTofu pidió cambiar `entorno           = "integracion"` a `entorno = "integracion"`. Al detenerse en formato, se omitieron validación, planes y políticas. No fue un rechazo de política.
- Corrección de formato: commit `c673f92` (`Correccion: formato de escenario integracion`). Actions, ejecución 43: formato, validación, ambos planes y ambas políticas pasaron.

## Prueba negativa deliberada

- Se cambió únicamente el responsable de integración a `equipo-lab`, dejando intactos el entorno y el resto de la configuración.
- Commit: `424493a` (`Prueba negativa: responsable no aprobado`).
- Actions, ejecución 44: formato, validación, plan predeterminado, política predeterminada y plan de integración pasaron. La política de integración rechazó con `POLÍTICA RECHAZADA: responsable no aprobado para integracion`; el resumen y el artefacto de evidencia se publicaron correctamente.
- El rechazo es intencionado y confirma que la regla de responsable corresponde a la política del plan, no a `tofu validate`.

## Restauración y documentación

- Se restauró `responsable = "equipo-integracion"` en `escenario-integracion.tfvars`.
- Se añadió en `README.md` la explicación de las etiquetas, la asignación del responsable por entorno, el resultado esperado de la prueba negativa y los límites del laboratorio.
- Commit de restauración y documentación: `6ab2b35` (`Ejercicio 8: restaurar responsable y documentar`).
- Actions, ejecución 45: todos los pasos pasaron, incluidas las dos políticas; se publicó el artefacto de evidencia.
- La rama remota conserva el responsable correcto para integración. No se ejecutó `tofu apply`.
- El número y estado del pull request se anotarán una vez creado en GitHub.
