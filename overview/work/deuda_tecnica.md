# Deuda Técnica (`overview/work/deuda_tecnica.md`)

> Errores, refactors pendientes o problemas no resueltos a nivel de código, ordenados por prioridad de impacto.

## 🔴 Prioridad Alta (Impacto Crítico / Bloqueante)

| ID | Ubicación / Componente | Descripción de la Deuda | Impacto |
|---|---|---|---|
| d1 | `core/gems.py` / `J3D_OT_add_gem` | Geometría del diamante incompleta: solo pabellón (cono primitivo). Falta corona y filetín BMesh real. | El "diamante" no tiene forma real de gema — solo pabellón cónico. |

## 🟡 Prioridad Media (Impacto Moderado / Mantenibilidad)

| ID | Ubicación / Componente | Descripción de la Deuda | Impacto |
|---|---|---|---|
| d2 | `ui/panels.py` (347L) | Archivo supera 250L — candidato a refactor por subpaneles en archivos separados. | Mantenibilidad. |
| d3 | `core/gems.py` | Funciones `create_gem_mesh`, `GEM_TYPES`, `CUT_ITEMS`, `GEM_TYPE_ITEMS` definidas pero no usadas por ningún operador activo. | Código muerto tras refactor de J3D_OT_add_gem. |

## 🟢 Prioridad Baja (Mejora Menor / Estilo)

| ID | Ubicación / Componente | Descripción de la Deuda | Impacto |
|---|---|---|---|
| d4 | `overview/work.md` | Filas de historial con líneas vacías entre entradas — inconsistencia de formato. | Visual / menor. |

---

## ✅ Completados (Historial)

<!-- Mover aquí deuda técnica completada conservando su ID -->

| ID | Ubicación / Componente | Descripción de la Deuda | Solución Aplicada | Agente | Fecha |
|---|---|---|---|---|---|
| - | `ui/panels.py` | `icon='GEM'` no existe en Blender 5.2 — causaba crash silencioso en draw() ocultando botón. | Cambiado a `icon='MESH_ICOSPHERE'`. | Claude Sonnet 4.6 (Thinking) | 2026-09-01 |
| - | `core/ring.py` | `spline.points.add()` en spline BEZIER lanzaba RuntimeError. | Cambiado a `spline.bezier_points.add()`. | Gemini 3.6 Flash (Medium) | 2026-09-01 |
