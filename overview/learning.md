# Mejoras pendientes para el Core (.agents)

Lista directa de mejoras identificadas para promover al repositorio global `.agents`.

## 📌 Propuestas de mejora

- **[rules]** `git init` es un prerrequisito obligatorio antes de ejecutar `git submodule add` en repositorios recién creados.
- **[rules]** La carga secuencial de `core/__init__.py` debe usar `hasattr(mod, "register")` / `hasattr(mod, "unregister")` para no fallar en módulos helper sin clases `bpy`.
- **[rules]** Durante `$boot`, la detección de `.skill/` debe actualizar `overview/commands_project.md` de forma determinista entre los delimitadores `<!-- SKILLS_START -->` y `<!-- SKILLS_END -->`.
- **[python-blender-addon-agent-skill]** En Blender 4.2+ (Extension Spec), la presencia de `bl_info` en `__init__.py` está prohibida y sustituida 100% por `bl_manifest.toml`. Enfatizar su purga en `$blender:audit`.
- **[python-blender-addon-agent-skill]** Exigir `@classmethod poll()` en todo `bpy.types.Operator`, incluyendo operadores de diálogo modal o exportadores I/O.

---

## 📜 Histórico de mejoras aplicadas


