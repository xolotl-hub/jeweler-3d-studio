# Trabajo: índice maestro y backlog canónico

> **Backlog canónico único.** Concentra los IDs de `tarea`, `bug` y `deuda`. El detalle se distribuye en `overview/work/tasks.md` (tarea activa), `overview/work/pendientes.md` (seguimiento) y `overview/work/deuda_tecnica.md` (deuda ordenada por prioridad Alta/Media/Baja).

| ID | Tipo | Estado | Resumen | Archivo de Detalle |
|---|---|---|---|---|
| w12 | tarea | en progreso | Herramienta Talla (Tallas US con medias tallas, por defecto 7.0, Curva/Cilindro, ventana de ajuste) | `overview/work/tasks.md` |
| w9 | tarea | en progreso | Arquitectura UI limpia de 6 paneles y subpaneles con operador de prueba `j3d.dummy_cube` | `overview/work/tasks.md` |
| w7 | tarea | en progreso | 1 botón simple en Gemas y Engastes (`j3d.add_gem`) y 1 botón simple en Cortadores y Garras (`j3d.add_cutters`) | `overview/work/tasks.md` |

Tipos: `tarea`, `bug`, `deuda`. Estados: `pendiente`, `en progreso`, `bloqueado`, `hecho`, `no verificado`.

---

## ✅ Completados (Historial)

<!-- Mover aquí tareas, bugs o deudas completadas conservando su ID -->

| ID | Tipo | Resuelto por (Agente) | Causa Raíz / Resumen Solución | Fecha |
|---|---|---|---|---|
| w1 | tarea | Gemini 3.6 Flash (Medium) | Auditoría completa de extensión Blender 4.2+ (Manifiesto, UI context safety, registro modular). Corregido `core/__init__.py`. | 2026-08-26 |
| w2 | tarea | Gemini 3.6 Flash (Medium) | Generador paramétrico procedural de mallas 3D para gemas en `core/gems.py` con facetas reales (6 cortes), materiales BSDF y estimador de quilates. | 2026-08-27 |
| w3 | tarea | Gemini 3.6 Flash (Medium) | Visor modal interactivo de gemas, presets de tamaño rápido (1.0 a 6.5mm) y operador de edición `j3d.edit_gem`. | 2026-08-27 |
| w4 | tarea | Gemini 3.6 Flash (Medium) | Refactorización de UI a sub-paneles nativos de Blender (`bl_parent_id`), resolviendo el anidamiento visual de cajas. | 2026-08-27 |
| w5 | tarea | Gemini 3.6 Flash (Medium) | Visor modal emergente con `template_icon_view`, iconos PNG de cortes, recuadro de previsualización grande y botones OK/Cancel. | 2026-08-27 |
| w6 | tarea | Gemini 3.6 Flash (Medium) | Estructura de paneles independientes de nivel superior en la pestaña Jeweler 3D (idéntico a Jewelcraft). | 2026-08-27 |
| w7 | tarea | Gemini 3.6 Flash (Medium) | Simplificación de UI a 1 botón funcional ultra-simple por sección (Anillo, Gema, Cortador, Métricas). | 2026-08-27 |
| w8 | tarea | Gemini 3.6 Flash (Medium) | Eliminación del panel `VIEW3D_PT_j3d_gems` ("Gemas y Engastes") de `ui/panels.py`. | 2026-08-27 |
| w9 | tarea | Gemini 3.6 Flash (Medium) | Estructura limpia de 6 paneles y subpaneles con operador base `j3d.dummy_cube` para construcción progresiva. | 2026-08-27 |
| w10 | tarea | Gemini 3.6 Flash (Medium) | Arquitectura completa de 6 paneles y 13 sub-paneles en `ui/panels.py` + Registro del backlog `p1`-`p7` en `pendientes.md`. | 2026-08-27 |
| w11 | tarea | Gemini 3.6 Flash (Medium) | Configuración de `bl_options = {'DEFAULT_CLOSED'}` en sub-paneles excepto Visor de Gemas. | 2026-08-27 |
| w12 | tarea | Gemini 3.6 Flash (Medium) | Herramienta Talla implementada en `core/ring.py` (Tallas US 3.0-13.5 con medias tallas, default US 7.0, selector doble Curva/Cilindro y panel emergente de ajuste). | 2026-08-27 |

---

## 📋 Historial de Intentos

<!-- Formato por entrada:
### [ID] Descripción breve del bug/tarea

| Fecha | Agente | Intento | Resultado |
|---|---|---|---|
| YYYY-MM-DD | Modelo vX | Descripción del intento | fallido / parcial / exitoso |

**✅ Resuelto por:** Agente (Modelo vX) — YYYY-MM-DD
- **Causa raíz:** …
- **Solución aplicada:** …

Reglas:
- Mismo día → actualizar la fila existente de esa fecha (no duplicar).
- Diferente día → nueva fila con fecha + firma del Agente.
- Al resolver → retirar inmediatamente de la tabla activa y trasladar a `## ✅ Completados (Historial)` conservando su ID.
- Nunca borrar intentos previos.
-->
