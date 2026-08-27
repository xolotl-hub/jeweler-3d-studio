# Tarea Activa (`overview/work/tasks.md`)

> Espacio de trabajo activo para la tarea en ejecución. Escribir aquí antes de modificar código.

## 🎯 Tarea Actual

- **ID:** `[wX]`
- **Descripción:** 

## 🏷️ Clasificación

- [ ] **Problema (Bug):** Comportamiento inesperado o fallo funcional.
- [ ] **Mejora (Feature):** Nueva capacidad o refactor de valor.
- [ ] **Deuda / Refactor:** Limpieza de código o estructuración técnica.


## <ctrl42> Rutas de Trabajo y Posibles Soluciones

### Hipótesis / Diagnóstico inicial
- Realizar análisis exhaustivo de `bl_manifest.toml`, `__init__.py`, `core/*.py`, `ui/*.py`, y `assets/node_groups/` evaluando:
  1. Cumplimiento con estándar Blender 4.2+ (extensiones y manifiesto manifest v1.0.0).
  2. Modulidad y registros/desregistros en `__init__.py`.
  3. Manejo seguro de `bpy.context` en UI (Paneles, Dialogs, Gizmos).
  4. Robustez de operadores (modal dialogs, cutters, ring, gems, prongs, pave, metrics).
  5. Calidad de código (concurrencia de tipos, docstrings, imports y ausencia de archivos >250L).

### Alternativas de solución
1. **Opción A:** Ejecutar auditoría estática directa archivo por archivo y documentar hallazgos en `deuda_tecnica.md` o corregir anomalías leves si existen.

### Ruta elegida
- **Opción A:** Auditoría estática archivo por archivo alineada al protocolo `$blender:audit`.

