# Mejoras pendientes para el Core (.agents)

Lista directa de mejoras identificadas para promover al repositorio global `.agents`.

## 📌 Propuestas de mejora

### [rules]

- `git init` es un prerrequisito obligatorio antes de ejecutar `git submodule add` en repositorios recién creados.
- La carga secuencial de `core/__init__.py` debe usar `hasattr(mod, "register")` / `hasattr(mod, "unregister")` para no fallar en módulos helper sin clases `bpy`.
- Durante `$boot`, la detección de `.skill/` debe actualizar `overview/commands_project.md` de forma determinista entre los delimitadores `<!-- SKILLS_START -->` y `<!-- SKILLS_END -->`.
- Al generar el zip de distribución de una extensión, excluir siempre `__pycache__/` y archivos `.pyc`; incluirlos no rompe la carga pero incrementa el tamaño innecesariamente.
- El zip de descarga directa de GitHub (`repo-main.zip`) **no es válido** para instalar extensiones Blender 4.2+: la carpeta raíz queda nombrada `repo-main/` y Blender no encuentra el manifiesto. Siempre empaquetar el zip seleccionando los archivos internos directamente (estructura plana en raíz).

### [python-blender-addon-agent-skill]

- En Blender 4.2+ (Extension Spec), la presencia de `bl_info` en `__init__.py` está prohibida y sustituida 100% por `blender_manifest.toml`. Enfatizar su purga en `$blender:audit`.
- El nombre oficial del manifiesto en Blender 4.2+ Extensions es **`blender_manifest.toml`** (no `bl_manifest.toml`). Usar el nombre incorrecto produce error "Missing manifest" al instalar. Verificar nombre exacto en `$blender:audit` y `$blender:manifest`.
- Exigir `@classmethod poll()` en todo `bpy.types.Operator`, incluyendo operadores de diálogo modal o exportadores I/O.

---

## 📜 Histórico de mejoras aplicadas
