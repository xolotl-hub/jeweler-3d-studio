"""
Jeweler 3D Studio - Core Gems Module
Dummy operator for clean UI testing.
"""

import bpy
from bpy.types import Operator


class J3D_OT_dummy_cube(Operator):
    """Añadir Cubo de Prueba"""
    bl_idname = "j3d.dummy_cube"
    bl_label = "Añadir Cubo"
    bl_description = "Añade un cubo básico de prueba a la escena"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context: bpy.types.Context) -> set[str]:
        bpy.ops.mesh.primitive_cube_add(size=0.005, location=context.scene.cursor.location)
        self.report({'INFO'}, "Cubo básico creado.")
        return {'FINISHED'}


classes = (
    J3D_OT_dummy_cube,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
