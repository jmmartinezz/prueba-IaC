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
- Commit inicial: `b648f5f` (`Ejercicio 8: etiquetas y responsables gobernados`). [Actions #42](https://github.com/jmmartinezz/prueba-IaC/actions/runs/44727415683) falló en `tofu fmt -check -diff -recursive`; OpenTofu pidió cambiar `entorno           = "integracion"` a `entorno = "integracion"`. Al detenerse en formato, se omitieron validación, planes y políticas. No fue un rechazo de política.
- Corrección de formato: commit `c673f92` (`Correccion: formato de escenario integracion`). [Actions #43](https://github.com/jmmartinezz/prueba-IaC/actions/runs/44727529888): formato, validación, ambos planes y ambas políticas pasaron.

## Prueba negativa deliberada

- Se cambió únicamente el responsable de integración a `equipo-lab`, dejando intactos el entorno y el resto de la configuración.
- Commit: `424493a` (`Prueba negativa: responsable no aprobado`).
- [Actions #44](https://github.com/jmmartinezz/prueba-IaC/actions/runs/44727666295): formato, validación, plan predeterminado, política predeterminada y plan de integración pasaron. La política de integración rechazó con `POLÍTICA RECHAZADA: responsable no aprobado para integracion`; el resumen y el artefacto de evidencia se publicaron correctamente.
- El rechazo es intencionado y confirma que la regla de responsable corresponde a la política del plan, no a `tofu validate`.

## Restauración y documentación

- Se restauró `responsable = "equipo-integracion"` en `escenario-integracion.tfvars`.
- Se añadió en `README.md` la explicación de las etiquetas, la asignación del responsable por entorno, el resultado esperado de la prueba negativa y los límites del laboratorio.
- Commit de restauración y documentación: `6ab2b35` (`Ejercicio 8: restaurar responsable y documentar`).
- [Actions #45](https://github.com/jmmartinezz/prueba-IaC/actions/runs/44727800407): todos los pasos pasaron, incluidas las dos políticas; se publicó el artefacto de evidencia.
- La rama remota conserva el responsable correcto para integración. No se ejecutó `tofu apply`.
- [Actions #46](https://github.com/jmmartinezz/prueba-IaC/actions/runs/44727948753) pasó tras publicar esta trazabilidad en la rama.

## Pull request y estado de integración

- Se creó el [pull request #6](https://github.com/jmmartinezz/prueba-IaC/pull/6), `Taller final ejercicio 8`, desde `taller-final-ejercicio-8` hacia `catalogo-ejercicio-7`.
- [Actions #47](https://github.com/jmmartinezz/prueba-IaC/actions/runs/44727987354), disparado por el pull request, pasó.
- GitHub muestra el PR #6 como fusionado el 2026-11-20 en `catalogo-ejercicio-7`, mediante el commit de merge `990cde7`. [Actions #48](https://github.com/jmmartinezz/prueba-IaC/actions/runs/44728035133) pasó en esa rama.
- La guía permitía dejar el PR abierto o en borrador, no fusionarlo. La fusión no era necesaria para completar el ejercicio; se registra como una desviación. No se ha intentado revertirla.
- `main` no recibió ese merge y permanece en `7f2460b`. No se hizo ningún cambio directo en `main`.

## Reversión posterior solicitada

- El usuario pidió revertir el efecto del merge del PR #6.
- En `catalogo-ejercicio-7` se creó el commit `d81c39b` con `git revert -m 1 990cde7`. Es un commit nuevo que restaura el contenido anterior al merge, sin reescribir ni borrar el historial.
- El push a `origin/catalogo-ejercicio-7` terminó correctamente. [Actions #50](https://github.com/jmmartinezz/prueba-IaC/actions/runs/44730427886) pasó: formato, validación, los dos planes y las políticas quedaron verdes.
- GitHub mantiene el PR #6 marcado como fusionado en el historial; el commit de reversión deshace sus cambios en `catalogo-ejercicio-7`. `main` no se modificó.
