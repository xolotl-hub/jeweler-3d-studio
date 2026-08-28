# Registro de Aprendizajes y Reglas (`overview/learning.md`)

Este archivo consolida las reglas, aprendizajes y buenas prácticas identificadas durante el desarrollo, de forma agnóstica y centralizada.

---

## python-agent-rules

### 1. Gestión Rigurosa de Unidades Físicas
- Al realizar conversiones de escala entre sistemas de unidades (ej. milímetros a metros `mm / 1000.0`), verificar siempre cómo interpreta el entorno ejecutor el vector de dimensión resultante.
- Garantizar que las variables de dimensión incluyan explícitamente la unidad en el nombre (`inner_dia_mm`, `radius_m`).

### 2. Arquitectura Modular y Desacoplada
- Mantener estrictamente separada la interfaz gráfica de usuario (UI) de los algoritmos y operadores core (`core/*.py` vs `ui/*.py`).
- Registrar y limpiar propiedades globales de manera determinista sin dejar efectos secundarios no deseados al deshabilitar módulos.

---

## python-blender-addon-agent-rules

### 1. Primitivos Nativos de Blender
- Preferir el uso de los operadores nativos del software (`bpy.ops.curve.primitive_bezier_circle_add`, `bpy.ops.mesh.primitive_cylinder_add`) sobre construcciones manuales con BMesh cuando el requerimiento sea generar objetos base con comportamiento idéntico al primitivo estándar.

### 2. Escalado de Objetos y `transform_apply`
- Al generar primitivos paramétricos mediante operadores, instanciar el objeto con radio base 1.0, aplicar la escala real en metros mediante `obj.scale = (r_m, r_m, z_m)` y congelar transformaciones inmediatamente ejecutando `bpy.ops.object.transform_apply(scale=True)` para asegurar dimensiones físicas reales exactas en la escena.

### 3. Ventana de Re-Ajuste ("Adjust Last Operation" / Redo Panel)
- Configurar siempre `bl_options = {'REGISTER', 'UNDO'}` en las clases `bpy.types.Operator` para activar el panel emergente nativo de ajuste en la esquina inferior izquierda del Viewport.

### 4. Control de Ruido Visual en Subpaneles
- Configurar `bl_options = {'DEFAULT_CLOSED'}` en subpaneles (`bl_parent_id`) para mantener la barra lateral colapsada por defecto.

### 5. Context Safety en Dibujo de UI
- Evitar asignar `col.operator_context` directamente en elementos de `UILayout` para prevenir fallos silenciosos de dibujo en los bindings C/Python del software.

### 6. Manifiesto y Empaquetado
- En Blender 4.2+ (Extension Spec), la presencia de `bl_info` en `__init__.py` está sustituida 100% por `blender_manifest.toml`.
- Al empaquetar la extensión en `.zip`, asegurar una estructura plana excluyendo carpetas wrapper raíz y directorios `__pycache__/`.

---

## 📌 Histórico de aprendizajes generales

- `git init` es un prerrequisito obligatorio antes de ejecutar `git submodule add` en repositorios recién creados.
- La carga secuencial de `core/__init__.py` debe usar `hasattr(mod, "register")` / `hasattr(mod, "unregister")` para no fallar en módulos helper sin clases `bpy`.
- Exigir `@classmethod poll()` en todo `bpy.types.Operator`, incluyendo operadores de diálogo modal o exportadores I/O.
