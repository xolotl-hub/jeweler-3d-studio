# Pendientes (`overview/work/pendientes.md`)

> Elementos identificados durante la planificación de arquitectura UI para seguimiento en sesiones futuras.

## 📌 Lista de Pendientes

| ID | Fecha detección | Origen / Contexto | Descripción | Estado |
|---|---|---|---|---|
| p1 | 2026-08-27 | Arquitectura UI | Implementación paramétrica del Panel 1: Anillo y Talla (Tallas US 4-13, perfiles Media Caña/Plano/Confort). | `pendiente` |
| p2 | 2026-08-27 | Arquitectura UI | Visor Modal 3D de Gemas con previsualización, mallas facetadas (6 cortes), materiales BSDF y estimador ct. | `pendiente` |
| p3 | 2026-08-27 | Arquitectura UI | Módulo de Engastes: Garras paramétricas (Prongs), Bisel cerrado (Bezel) y distribución Pavé. | `pendiente` |
| p4 | 2026-08-27 | Arquitectura UI | Módulo de Cortadores Booleanos: Asientos de filetín, perforaciones de luz y cortes en V. | `pendiente` |
| p5 | 2026-08-27 | Arquitectura UI | Módulo de Canastas y Galerías: Generador de biseles inferiores y soportes para piedras centrales. | `pendiente` |
| p6 | 2026-08-27 | Visión Administrativa | Cotizador Administrativo ($/g metal + gemas + mano de obra) y Generador de Ficha Técnica (HTML/PDF). | `pendiente` |
| p7 | 2026-08-27 | Visión Administrativa | Verificador de Seguridad para Impresión 3D/Fundición (Grosor mínimo < 0.8mm y compensación de merma %). | `pendiente` |
| **p8** | **2026-08-27** | **Bug Escala - Herramienta Talla** | **⚠️ IMPORTANTE: La conversión mm→metros en `core/ring.py` no produce el tamaño correcto en escena Blender (metros). Estrategia actual: crear primitivo radio=1.0 y escalar con `transform_apply`. Verificar y validar que la escena en metros produce las dimensiones físicas correctas antes de continuar con más herramientas.** | **`pendiente`** |

- **Estados:** `pendiente`, `en progreso`, `promovido_a_task`, `descartado`, `hecho`.

---

## ✅ Completados (Historial)

| ID | Fecha Resolución | Origen / Contexto | Descripción / Solución | Agente |
|---|---|---|---|---|
