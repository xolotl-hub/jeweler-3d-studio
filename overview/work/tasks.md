# Tarea Activa (`overview/work/tasks.md`)

> Espacio de trabajo activo para la tarea en ejecución. Escribir aquí antes de modificar código.

## 🎯 Tarea Siguiente (Pendiente — próxima sesión)

- **ID:** `[w22]` (planificada)
- **Descripción:** Construir geometría BMesh completa del diamante redondo brillante. El usuario aportará datos JSON de la malla de JewelCraft (verts + faces). Reemplazar `primitive_cone_add` en `J3D_OT_add_gem` (`core/gems.py`) con BMesh real que incluya corona, filetín y pabellón. Aplicar material BSDF diamante (IOR 2.417) y estimar quilates.

## 🏷️ Clasificación

- [ ] **Problema (Bug):** Comportamiento inesperado o fallo funcional.
- [X] **Mejora (Feature):** Nueva capacidad o refactor de valor.
- [ ] **Deuda / Refactor:** Limpieza de código o estructuración técnica.

## <ctrl42> Rutas de Trabajo y Posibles Soluciones

### Hipótesis / Diagnóstico inicial
- El operador actual usa `bpy.ops.mesh.primitive_cone_add` que solo genera el pabellón (parte inferior cónica).
- La corona (parte superior facetada con tabla) requiere BMesh con vértices específicos para cada capa de facetas.

### Input requerido del usuario
- JSON con `verts` y `faces` del diamante redondo de JewelCraft:
```python
import bpy, json
obj = bpy.context.active_object
data = {
    "verts": [list(v.co) for v in obj.data.vertices],
    "faces": [list(p.vertices) for p in obj.data.polygons]
}
print(json.dumps(data))
```

### Alternativas de solución
1. **Opción A (preferida):** Recibir datos JSON de JewelCraft → reconstruir en BMesh.
2. **Opción B:** `bpy.ops.wm.append()` desde `assets/gems/gems.blend`.
3. **Opción C:** Geometría paramétrica pura calculada matemáticamente (sin referencia externa).

### Ruta elegida
- **Opción A:** Preferida — el usuario trae los datos JewelCraft en la próxima sesión.
