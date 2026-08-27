# Trabajo: índice maestro y backlog canónico

> **Backlog canónico único.** Concentra los IDs de `tarea`, `bug` y `deuda`. El detalle se distribuye en `overview/work/tasks.md` (tarea activa), `overview/work/pendientes.md` (seguimiento) y `overview/work/deuda_tecnica.md` (deuda ordenada por prioridad Alta/Media/Baja).

| ID | Tipo | Estado | Resumen | Archivo de Detalle |
|---|---|---|---|---|

Tipos: `tarea`, `bug`, `deuda`. Estados: `pendiente`, `en progreso`, `bloqueado`, `hecho`, `no verificado`.

---

## ✅ Completados (Historial)

<!-- Mover aquí tareas, bugs o deudas completadas conservando su ID -->

| ID | Tipo | Resuelto por (Agente) | Causa Raíz / Resumen Solución | Fecha |
|---|---|---|---|---|
| w1 | tarea | Gemini 3.6 Flash (Medium) | Auditoría completa de extensión Blender 4.2+ (Manifiesto, UI context safety, registro modular). Corregido `core/__init__.py`. | 2026-08-26 |

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
